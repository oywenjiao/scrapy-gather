# -*- coding: utf-8 -*-
import scrapy
from huatu.items import YhbItem

class YhbSpider(scrapy.Spider):
    name = 'yhb'
    allowed_domains = ['ekeguan.com']
    start_urls = ['http://mokao.ekeguan.com/exam/resolve/id/89131.html']

    def start_requests(self):
        start_url = [
            'http://mokao.ekeguan.com/exam/resolve/id/89131.html'
        ]
        cookie = {'PHPSESSID': '6fd5c79e84dc54746039fc9547e7dab9', 'Hm_lvt_69adc0418f3be10cef5b362f1fca856f': '1569564415', '_ga': 'GA1.2.1877060561.1569564415', '_gid': 'GA1.2.1175788722.1569564415', 'EKG_ID': '497E9DF9DD9138705FC942C059EA37BF', 'Hm_lpvt_69adc0418f3be10cef5b362f1fca856f': '1569564472'}
        headers = {
            'Connection': 'keep - alive',
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.82 Safari/537.36'
        }
        for item in start_url:
            yield scrapy.Request(url=item, headers=headers, cookies=cookie)

    def parse(self, response):
        for each in response.xpath("//div[contains(@class,'select_item')]"):
            # 初始化模型对象
            item = YhbItem()
            item['title'] = each.xpath("normalize-space(./p[contains(@class, 'com-jx-weight')]/text())").extract_first()
            item['question_option'] = each.xpath("./ul[contains(@class, 'item_list')]/li/label/text()").extract()
            item['answer'] = each.xpath("normalize-space(./div[contains(@class, 'key_two')]/p/span/text())").extract()
            try:
                item['analysis'] = each.xpath("./div/div[1]/div[@class='tag_two']/p").extract()
            except Exception as e:
                item['analysis'] = ''

            yield item
