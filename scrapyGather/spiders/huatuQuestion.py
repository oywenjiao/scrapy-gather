# -*- coding: utf-8 -*-
import scrapy
from huatu.items import HuatuItem

class HuatuquestionSpider(scrapy.Spider):
    name = 'huatuQuestion'
    allowed_domains = ['huatu.com']
    start_urls = ['http://v.huatu.com/tiku/analysis/2379454042589195263', 'http://v.huatu.com/tiku/analysis/2521056048142580462']

    def start_requests(self):
        start_url = [
            'http://v.huatu.com/tiku/analysis/2379454042589195263',
            'http://v.huatu.com/tiku/analysis/2521056048142580462'
        ]
        cookie = {'UM_distinctid': '16cff897a24434-0cf5edb501a411-5373e62-1fa400-16cff897a259f', 'uid_cv_k_u_s': 'BgQSUCHuopBrSs495677||||', 'NTKF_T2D_CLIENTID': 'guest63288B4E-AA1C-DF14-5C9B-FF897B185C32', 'PHPSESSID': 'hg4j3466et4de9ntcukth2f950', 'CNZZDATA580664': 'cnzz_eid%3D117736191-1567651058-%26ntime%3D1569309608', 'Hm_lvt_f735d6529dbfd84e0e9d68fea4bb90a4': '1567655296,1569311093', 'CNZZDATA443728': 'cnzz_eid%3D1151025438-1567649983-%26ntime%3D1569307857', 'nTalk_CACHE_DATA': '{uid:kf_9846_ISME9754_guest63288B4E-AA1C-DF,tid:1569311093217546}', 'ca_sessionid': 'oCdcL3VgkF7ugXc93232', 'HT_sc_f41114f3ecfa342590164bded47c5b07f528ac74': 'faf636b2c4339527.1567655296.1569311270.1569311270', 'UserID': '11616977', 'UserName': 'app_ztk799828835', 'UserReName': '133%2A%2A%2A%2A9917', 'Password': '5da8d85adab5d0ec', 'TruePassWord': '717c6b12c51b98e18f51a4789ea82685', 'UserLevel': '1', 'UserFace': 'http%3A%2F%2Ftiku.huatu.com%2Fcdn%2Fimages%2Fvhuatu%2Favatars%2Fdefault2.png', 'synlogin': '0', 'ht_token': '5cf374611fea45d0885c44b29e3efb99', 'ht_id': '236973252', 'ht_uname': 'app_ztk799828835', 'ht_qcount': '10', 'ucId': '13391169917', 'jtoken': 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpYXQiOm51bGwsImp0aSI6Ik1UVTJPVE14TWpBek1RPT0iLCJleHAiOiIxNTcxOTA0MDMxIiwidW5hbWUiOiJhcHBfenRrNzk5ODI4ODM1IiwibmljayI6IjEzMyoqKio5OTE3In0.dOCedDFAwrlBnpDwGu1ZXkm_WnhM1KUEAQzYhMClafc', 'sensorsdata2015jssdkcross': '%7B%22distinct_id%22%3A%2213391169917%22%2C%22%24device_id%22%3A%2216cff897a348c-0835d5c53fa621-5373e62-2073600-16cff897a357a0%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_referrer%22%3A%22%22%2C%22%24latest_referrer_host%22%3A%22%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%7D%2C%22first_id%22%3A%2216cff897a348c-0835d5c53fa621-5373e62-2073600-16cff897a357a0%22%7D', 'Hm_lpvt_f735d6529dbfd84e0e9d68fea4bb90a4': '1569312032'}
        headers = {
            'Connection': 'keep - alive',
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.82 Safari/537.36'
        }
        # 设置文件头信息及cookie
        for item in start_url:
            yield scrapy.Request(url=item, headers=headers, cookies=cookie)

    def parse(self, response):
        for each in response.xpath("//div[contains(@class,'exercise-main-topic')]"):
            # 初始化模型对象
            item = HuatuItem()
            item['bank'] = each.xpath("normalize-space(//div[@class='exercise-main-title']/text())").extract_first()
            item['title'] = each.xpath("./div[@class='main-topic-stem']").extract()
            item['option'] = each.xpath("./div[@class='main-topic-choices']/div").extract()
            item['answer'] = each.xpath(".//span[@class='g-right-answer-color']/text()").extract()
            item['source'] = each.xpath("./div[@class='main-topic-jiexi']/div[@class='jiexi-items']/div[contains(@class,'jiexi-item')][last()]/div[@class='jiexi-item-content']/text()").extract_first()
            item['examination'] = each.xpath("./div[@class='main-topic-jiexi']/div[@class='jiexi-items']/div[contains(@class,'jiexi-item')][last()-1]/div[@class='jiexi-item-content']/text()").extract()
            item['analysis'] = each.xpath("./div[@class='main-topic-jiexi']/div[@class='jiexi-items']/div[contains(@class,'jiexi-item')][2]/div[@class='jiexi-item-content']/text()").extract()
            item['expand'] = each.xpath("./div[@class='main-topic-jiexi']/div[@class='jiexi-items']/div[contains(@class,'jiexi-item')][last()-2 and position()=3]/div[@class='jiexi-item-content']").extract()

            yield item

