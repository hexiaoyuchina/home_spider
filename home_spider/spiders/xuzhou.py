import scrapy
from lxml import etree
from home_spider.items import LouPanItem
class XuzhouSpider(scrapy.Spider):
    name = 'xuzhou'
    allowed_domains = ['xz.fang.ke.com/loupan']
    start_urls = ['http://xz.fang.ke.com/loupan/']

    def start_requests(self):

        yield scrapy.Request("http://xz.fang.ke.com/loupan/", meta={"is_request_next": ""}, callback=self.parse)

    def parse(self, response):
        is_request_next_flag = response.meta['is_request_next']
        html = etree.HTML(response.text)
        loupans = html.xpath('//div[@class="resblock-desc-wrapper"]')
        # next_url = xz.fang.ke.com/loupan/pg2/
        for loupan in loupans:
            item = LouPanItem()
            loupan_name = loupan.xpath('./div[@class="resblock-name"]/a//text()')[0]
            loupan_satus_type = loupan.xpath('./div[@class="resblock-name"]//span//text()')
            loupan_is_sail = loupan_satus_type[0]
            loupan_type = loupan_satus_type[-1]
            loupan_location = loupan.xpath('./a[@class="resblock-location"]//text()')[1]
            total_price = loupan.xpath('./div[@class="resblock-price"]//div[@class="second"]//text()')[0]
            rom_num_area = loupan.xpath('./a[@class="resblock-room"]//span//text()')
            rom_num = rom_num_area[0] + ('/').join(rom_num_area[1:-1])
            rom_area = rom_num_area[-1]

            item['name'] = loupan_name
            item['location'] = loupan_location
            item['total_price'] = total_price
            item['room_number'] = rom_num
            item['room_area'] = rom_area
            item['is_sail'] = loupan_is_sail
            item['room_type'] = loupan_type
            yield item

        if not is_request_next_flag:
            for index in range(2, 18):
                yield scrapy.Request(
                                    "http://xz.fang.ke.com/loupan/pg{}/".format(index),
                                     meta={"is_request_next": "0"},
                                     callback=self.parse
                )


