# -*- coding: utf-8 -*-
import scrapy

from scrapyGather.items import XiaohuaItem


class XiaohuaSpider(scrapy.Spider):
    # 爬虫名（运行命令时使用的参数)
    name = 'xiaohua'
    # 爬虫作用范围(在指定的域名下通用)
    allowed_domains = ['pengfu.com']
    # 实际操作链接地址
    start_urls = ['https://www.pengfu.com/xiaohua_1.html']

    # 业务处理函数
    def parse(self, response):
        articleList = response.css('.list-item')

        for item in articleList:
            article = XiaohuaItem()
            article['content'] = item.css('.content-img::text').extract_first().strip()
            # strip() 去除空格
            yield article

        # 获取下一页标签
        text = response.css('div.page > div > a:last-child::text').extract_first().strip()
        # unicode转化为str，采用encode 编码
        a = text.encode("utf-8")
        if a == '下一页':
            next = response.css('div.page > div > a:last-child::attr(href)').extract_first()
            url = response.urljoin(next)
            yield scrapy.Request(url=url, callback=self.parse)


