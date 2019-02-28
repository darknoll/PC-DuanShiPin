import sys
import ks

if __name__ == "__main__":
    hot_info = ks.KuaiShouCrawler.get_hot_info()
    sys.stdout.buffer.write(hot_info)
    sys.stdout.buffer.flush()