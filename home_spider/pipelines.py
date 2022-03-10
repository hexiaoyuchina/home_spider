# -*- coding: utf-8 -*-
# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

import uuid
import logging
# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from home_spider.db.clickhouse_db import ConnectClickhouse
logger = logging.getLogger(__name__)

class HomeSpiderPipeline:
    def __init__(self):
        self.item_list = []
        self.client=None

    def open_spider(self, spider):
        self.client = ConnectClickhouse(
            host="114.112.79.242",
            database="home_data",
            user="default",
            password="123456",
            port=9000
        )

    def close_spider(self, spider):
        # 关闭爬虫前，插入剩余数据
        sql = "insert into home_data(id,name,location,price,total_price,room_number,room_area,is_sail,room_type) values "
        logger.info(sql, )
        self.client.execute(sql, self.item_list)

        self.client.close()

    def process_item(self, item, spider):

        page_data = [str(uuid.uuid1()),
                     item['name'],
                     item['location'],
                     item['price'],
                     item['total_price'],
                     item['room_number'],
                     item['room_area'],
                     item['is_sail'],
                     item['room_type']]
        self.item_list.append(page_data)
        if len(self.item_list) == 1000:
            sql = "insert into home_data(id,name,location,price,total_price,room_number,room_area,is_sail,room_type) values "
            self.client.execute(sql, self.item_list)
        return item
