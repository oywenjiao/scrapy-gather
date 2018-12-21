# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

from twisted.enterprise import adbapi
import MySQLdb
import MySQLdb.cursors

# 导入时间处理库
import datetime
import time

class XiaohuaPipeline(object):

    def __init__(self):
        # 存入mysql
        dbargs = dict(
            host='127.0.0.1',
            db='test',
            user='root',
            passwd='root',
            charset='utf8',
            cursorclass=MySQLdb.cursors.DictCursor,
            use_unicode=True,
        )
        self.dbpool = adbapi.ConnectionPool('MySQLdb', **dbargs)

    def process_item(self, item, spider):
        self.dbpool.runInteraction(self.insert_into_table, item)
        return item

    def insert_into_table(self, conn, item):
        publish = int(time.time())
        created = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        conn.execute(
            'insert into joke(content,publish,created_at,updated_at) values(%s, %s, %s, %s)',
            (item['content'], publish, created, created))

