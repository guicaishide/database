import scrapy
from ..items import MoviesItem

class TencentSpider(scrapy.Spider):
    name='tencent'
    start_urls = []
    for i in range(0,332):
        url='https://hr.tencent.com/position.php?keywords=&tid=0&start='+str(i*10)+'#a'
        start_urls.append(url)


    def parse(self, response):
        even_list=response.xpath('//tr[@class="even"]')
        for even in even_list:
            item = MoviesItem()
            item['title'] = even.xpath('./td[@class="l square"]/a/text()').extract()
            item['job'] = even.xpath('./td[2]/text()').extract()
            item['number'] = even.xpath('./td[3]/text()').extract()
            item['place'] = even.xpath('./td[4]/text()').extract()
            item['pub_time'] = even.xpath('./td[5]/text()').extract()
            yield item

        odd_list = response.xpath('//tr[@class="odd"]')
        for odd in odd_list:
            item = MoviesItem()
            item['title'] = odd.xpath('./td[@class="l square"]/a/text()').extract()
            item['job'] = odd.xpath('./td[2]/text()').extract()
            item['number'] = odd.xpath('./td[3]/text()').extract()
            item['place'] = odd.xpath('./td[4]/text()').extract()
            item['pub_time'] = odd.xpath('./td[5]/text()').extract()
            yield item






