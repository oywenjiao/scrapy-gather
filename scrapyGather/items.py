# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class XiaohuaItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()

    content = scrapy.Field()
    publish = scrapy.Field()


class HuatuItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()

    # 所属题库
    bank = scrapy.Field()
    # 标题
    title = scrapy.Field()
    # 选项
    option = scrapy.Field()
    # 正确答案
    answer = scrapy.Field()
    # 解析
    analysis = scrapy.Field()
    # 拓展
    expand = scrapy.Field()
    # 考点
    examination = scrapy.Field()
    # 来源
    source = scrapy.Field()


class YhbItem(scrapy.Item):
    # 题目标题
    title = scrapy.Field()
    # 题目选项
    question_option = scrapy.Field()
    # 题目正确答案
    answer = scrapy.Field()
    # 题目解析
    analysis = scrapy.Field()


class BooksItem(scrapy.Item):
    book_name = scrapy.Field()
    book_star = scrapy.Field()
    book_pl = scrapy.Field()
    book_author = scrapy.Field()
    book_publish = scrapy.Field()
    book_date = scrapy.Field()
    book_price = scrapy.Field()
    pass

