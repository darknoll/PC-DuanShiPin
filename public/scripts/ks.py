import requests
import sys
import os
import json
import processor
import urllib.parse
from lxml import html
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

USER_AGENT = 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.96 Safari/537.36'
ORIGIN = 'https://live.kuaishou.com'
API_URL = 'https://live.kuaishou.com/graphql'

class KuaiShouCrawler(object):
    def __init__(self, name):
        self.session = requests.Session()
        self.verify = False
        self.name = name
        self.buffer = []
    
    def get_videos_info(self):
        headers = {
            'user-agent': USER_AGENT,
            'origin': ORIGIN,
            'referer': 'https://live.kuaishou.com/profile/{}'.format(self.name)
        }
        payloads = {
            "operationName": "ProfileFeeds",
            "variables": {
                "principalId": "{}".format(self.name),
                "privacy": "public",
                "pcursor": "0",
                "count": 100000
            },
            "query": "query ProfileFeeds($principalId: String, $privacy: String, $pcursor: String, $count: Int) {\n  getProfileFeeds(principalId: $principalId, privacy: $privacy, pcursor: $pcursor, count: $count) {\n    pcursor\n    live {\n      ...LiveStreamInfo\n      __typename\n    }\n    list {\n      ...WorkInfo\n      __typename\n    }\n    __typename\n  }\n}\n\nfragment LiveStreamInfo on LiveStream {\n  user {\n    id\n    kwaiId\n    eid\n    profile\n    name\n    living\n    __typename\n  }\n  watchingCount\n  src\n  title\n  gameId\n  gameName\n  categoryId\n  liveStreamId\n  playUrls {\n    quality\n    url\n    __typename\n  }\n  followed\n  type\n  living\n  redPack\n  liveGuess\n  anchorPointed\n  latestViewed\n  expTag\n  __typename\n}\n\nfragment WorkInfo on VideoFeed {\n  photoId\n  caption\n  thumbnailUrl\n  poster\n  viewCount\n  likeCount\n  commentCount\n  timestamp\n  workType\n  type\n  playUrl\n  useVideoPlayer\n  imgUrls\n  imgSizes\n  magicFace\n  musicName\n  location\n  liked\n  onlyFollowerCanComment\n  relativeHeight\n  width\n  height\n  user {\n    id\n    eid\n    name\n    profile\n    __typename\n  }\n  expTag\n  __typename\n}\n"
        }
        self.buffer = []
        r = self.session.post(API_URL, headers=headers, json=payloads, stream=True)
        for chunk in r.iter_content(chunk_size=1024):
            if chunk:
                self.buffer.append(chunk)
        r.close()
    
    @staticmethod
    def get_search_suggets(search_key):
        headers = {
            'user-agent': USER_AGENT,
            'origin': ORIGIN,
            'referer': 'https://live.kuaishou.com/search/?keyword={}'.format(urllib.parse.quote(search_key))
        }
        payloads = {
            "operationName": "SearchSuggest",
            "variables": {
                "keyword": search_key
            },
            "query": "query SearchSuggest($keyword: String) {\n  searchSuggest(keyword: $keyword) {\n    users {\n      ussid\n      list {\n        id\n        kwaiId\n        eid\n        profile\n        name\n        living\n        __typename\n      }\n      __typename\n    }\n    categories {\n      id\n      category\n      categoryId\n      title\n      src\n      roomNumber\n      __typename\n    }\n    suggestKeywords {\n      list\n      ussid\n      __typename\n    }\n    __typename\n  }\n}\n"
        }
        r = requests.post(API_URL, headers=headers, json=payloads, verify=False)
        return r.content
    
    @staticmethod
    def get_search_result(search_key):
        headers = {
            'user-agent': USER_AGENT,
            'origin': ORIGIN
        }
        params = {
            'keyword': search_key
        }
        r = requests.get('https://live.kuaishou.com/search/', headers=headers, params=params, verify=False)
        tree = html.fromstring(r.text)
        user_names = tree.xpath('//div[@class="profile-card-user-info-detail"]/div/@title')
        user_urls = tree.xpath('//div[@class="profile-card-user-info"]/a/@href')
        user_images = tree.xpath('//div[@class="profile-card"]//img/@src')
        user_counts = tree.xpath('//p[@class="profile-card-user-info-counts"]/text()')
        user_descs = tree.xpath('//p[@class="profile-card-user-info-description notlive"]/text()')
        user_infos = []
        for i in range(len(user_names)):
            user_info_item = {}
            user_info_item['name'] = user_names[i]
            user_info_item['url'] = user_urls[i]
            user_info_item['image'] = user_images[i]
            user_info_item['counts'] = user_counts[i]
            user_info_item['desc'] = user_descs[i]
            user_infos.append(user_info_item)
        user_info = json.dumps(user_infos)
        return bytes(user_info, 'utf-8')
    
    @staticmethod
    def get_hot_info():
        headers = {
            'user-agent': USER_AGENT,
            'origin': ORIGIN,
            'referer': 'https://live.kuaishou.com/v/hot/'
        }
        payloads = {
            "operationName": "GetVideoFeeds",
            "variables": {
                "pcursor": 0,
                "count": 99
            },
            "query": "query GetVideoFeeds($pcursor: String, $count: Int) {\n  videoFeeds(pcursor: $pcursor, count: $count) {\n    list {\n      user {\n        id\n        eid\n        profile\n        name\n        __typename\n      }\n      ...VideoMainInfo\n      __typename\n    }\n    pcursor\n    __typename\n  }\n}\n\nfragment VideoMainInfo on VideoFeed {\n  photoId\n  caption\n  thumbnailUrl\n  poster\n  viewCount\n  likeCount\n  commentCount\n  timestamp\n  workType\n  type\n  playUrl\n  useVideoPlayer\n  imgUrls\n  imgSizes\n  magicFace\n  musicName\n  location\n  liked\n  onlyFollowerCanComment\n  width\n  height\n  expTag\n  __typename\n}\n"
        }
        r = requests.post(API_URL, headers=headers, json=payloads, verify=False)
        return r.content
        
    
    def download_videos(self, save_dir=''):
        if save_dir == '':
            save_dir = os.path.join(os.getcwd(), self.name)
            if not os.path.isdir(save_dir):
                os.makedirs(save_dir)
        if not os.path.isdir(save_dir):
            raise('your save dir path is not exist!')
        video_dict = {}
        buffer_json = b''.join(self.buffer).decode('utf-8')
        video_dict = json.loads(buffer_json)
        os.chdir(save_dir)
        for video in video_dict['data']['getProfileFeeds']['list']:
            if video['useVideoPlayer']:
                video_url = video['playUrl']
                video_name = video_url.rsplit('/', 1)[1]
                if os.path.exists(os.path.join(save_dir, video_name)):
                    continue
                cmd = 'curl -O {}'.format(video_url)
                os.system(cmd)
    
if __name__ == "__main__":
    name = input('Please input the name: ')
    crawler = KuaiShouCrawler(name)
    crawler.get_videos_info()
    crawler.download_videos()
    isMerge = input('Download Done! Do you Merge thiese videos? (Enter)No, (Others)Yes: ')
    isMerge = isMerge if isMerge!='' else False
    if isMerge:
        processor.merge_videos()
    print('All Done!')

