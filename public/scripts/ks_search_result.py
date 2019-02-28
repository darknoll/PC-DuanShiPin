import sys
import ks

if __name__ == "__main__":
    if len(sys.argv) != 2:
        raise Exception('Usage: python ks_search_overview [search_key]')
    search_key = sys.argv[1]
    search_result = ks.KuaiShouCrawler.get_search_result(search_key)
    sys.stdout.buffer.write(search_result)
    sys.stdout.buffer.flush()