import sys
import ks

if __name__ == "__main__":
    if len(sys.argv) !=2 :
        raise Exception('Usage: python ks_video_info [userID]')
    userID = sys.argv[1]
    crawler = ks.KuaiShouCrawler(userID)
    crawler.get_videos_info()
    video_dict = b''.join(crawler.buffer)
    sys.stdout.buffer.write(video_dict)
    sys.stdout.buffer.flush()    