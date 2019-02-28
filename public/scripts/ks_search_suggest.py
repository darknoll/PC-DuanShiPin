import sys
import ks

if __name__ == "__main__":
    if len(sys.argv) != 2:
        raise Exception('Usage: python ks_search_suggest [search_key]')
    search_key = sys.argv[1]
    search_suggest = ks.KuaiShouCrawler.get_search_suggets(search_key)
    sys.stdout.buffer.write(search_suggest)
    sys.stdout.buffer.flush()
