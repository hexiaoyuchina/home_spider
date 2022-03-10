# -*- coding: utf-8 -*-
import json
import re
import scrapy
from lxml import etree
from home_spider.items import LouPanItem
import logging

logger = logging.getLogger(__name__)
class XuzhouSpider(scrapy.Spider):
    name = 'xuzhou'
    allowed_domains = ['xz.fang.ke.com/loupan']
    start_urls = ['http://xz.fang.ke.com/loupan/']
    start_urls = ['https://xz.fang.ke.com/loupan/pg' + str(x) for x in range(1, 18)]

    def parse(self, response):
        html = etree.HTML(response.text)
        loupans = html.xpath('//div[@class="resblock-desc-wrapper"]')
        for loupan in loupans:

            item = LouPanItem()
            loupan_name = loupan.xpath('./div[@class="resblock-name"]/a//text()')[0]
            loupan_satus_type = loupan.xpath('./div[@class="resblock-name"]//span//text()')
            loupan_is_sail = loupan_satus_type[0]
            loupan_type = loupan_satus_type[-1]
            loupan_location = loupan.xpath('./a[@class="resblock-location"]//text()')[1]
            price_list = loupan.xpath('./div[@class="resblock-price"]//div[@class="main-price"]/span[@class="number"]//text()')
            if price_list:
                price = price_list[0]
            else:
                price = '0'

            total_price_list = loupan.xpath('./div[@class="resblock-price"]//div[@class="second"]//text()')
            if total_price_list:
                total_price = total_price_list[0]
            else:
                total_price = '0'

            rom_num_area = loupan.xpath('./a[@class="resblock-room"]//span//text()')
            if not rom_num_area:
                rom_num = '0'
                rom_area = '0'
            else:
                rom_num = rom_num_area[0] + ('/').join(rom_num_area[1:-1])
                rom_area = rom_num_area[-1]

            item['name'] = loupan_name
            item['location'] = loupan_location.replace('\n\t\t', '')
            item['price'] = price
            item['total_price'] = total_price
            item['room_number'] = rom_num
            item['room_area'] = rom_area
            item['is_sail'] = loupan_is_sail
            item['room_type'] = loupan_type

            yield item

