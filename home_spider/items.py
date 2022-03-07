# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class HomeSpiderItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass


class LouPanItem(scrapy.Item):
    name = scrapy.Field()
    location = scrapy.Field()
    total_price = scrapy.Field()
    room_number = scrapy.Field()
    price = scrapy.Field()
    room_area = scrapy.Field()
    is_sail = scrapy.Field()
    room_type = scrapy.Field()
