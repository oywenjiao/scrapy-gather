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

# 导入json/csv模块
import json
import csv

# 导入pymysql模块
import pymysql

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


class HuatuPipeline(object):

    def __init__(self):
        self.filename = open('huatu.json', 'w', encoding='utf-8')

    def process_item(self, item, spider):
        text = json.dumps(dict(item), ensure_ascii=False) + ",\n"
        self.filename.write(text)
        return item

    def close_spider(self, spider):
        self.filename.close()


class YhbCSVPipeline(object):

    def __init__(self):
        # 打开文件，指定方式为写，利用第3个参数把csv写数据时产生的空行消除
        self.f = open("myproject.csv", "a", encoding='utf-8')
        # 设置文件第一行的字段名，注意要跟spider传过来的字典key名称相同
        self.fieldnames = ["title", "option", "answer", "analysis"]
        # 指定文件的写入方式为csv字典写入，参数1为指定具体文件，参数2为指定字段名
        self.writer = csv.DictWriter(self.f, fieldnames=self.fieldnames)
        # 写入第一行字段名，因为只要写入一次，所以文件放在__init__里面
        self.writer.writeheader()

    def process_item(self, item, spider):
        # 写入spider传过来的具体数值
        self.writer.writerow(item)
        # 写入完返回
        return item

    def close(self, spider):
        self.f.close()


class YhbPipeline(object):

    def __init__(self):
        dbparams = {
            'host': '127.0.0.1',
            'port': 3306,
            'user': 'root',
            'password': 'root',
            'database': 'pythonDB',
            'charset': 'utf8'
        }
        self.conn = pymysql.connect(**dbparams)
        self.cursor = self.conn.cursor()
        self._sql = None

    def process_item(self, item, spider):
        # 获取当前时间的日期格式
        times = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        self.cursor.execute(self.sql, (
        item['title'], item['answer'], json.dumps(item['analysis']), str(item['question_option']), times))
        self.conn.commit()
        return item

    @property
    def sql(self):
        if not self._sql:
            self._sql = """
                            insert into yhb_questions(id,title,answer,analysis,question_option,create_time) values(null,%s,%s,%s,%s,%s)
                            """
            return self._sql
        return self._sql