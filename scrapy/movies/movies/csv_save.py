from scrapy import cmdline
cmdline.execute("scrapy crawl tencent -o tencent.csv -t csv".split())