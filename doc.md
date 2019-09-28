
# Scrapy 教程

## 基本操作

``` bash
    1、创建项目：scrapy startproject scrapy-gather(项目名称)
```

``` bash
    2、目录结构：
        scrapyGather: 项目目录
        spiders: 爬虫文件存储目录
        items.py: 该文件定义需要获取的字段
        pipelines: 该文件定义存储引擎
        settings: 该文件配置各种设置
```

``` bash
    3、配置IDE调试：
        Scrapy默认是不能在IDE中调试的，我们在根目录中新建一个py文件叫：begin.py；在里面写入以下内容：
```

<code> from scrapy import cmdline </code>

<code> cmdline.execute("scrapy crawl xiaohua".split()) </code>

## <code> items.py </code> 文件说明

``` 
    用来定义爬取内容的每一个字段名称，每一个爬虫定义一个类！
    class XiaohuaItem(scrapy.Item):
    # 在此处定义项目的字段，如下所示:
    # name = scrapy.Field()

    content = scrapy.Field()
    publish = scrapy.Field()
```

## <code> settings.py  </code> 文件说明

```
    用来配置爬虫相关属性
```


## <code> pipelines.py </code> 文件说明

```
    用来配置爬取数据存储方式

    class HuatuPipeline(object):

    def __init__(self):
        self.filename = open('huatu.json', 'w', encoding='utf-8')

    def process_item(self, item, spider):
        text = json.dumps(dict(item), ensure_ascii=False) + ",\n"
        self.filename.write(text)
        return item

    def close_spider(self, spider):
        self.filename.close()
```


# XPath 教程

## 示例

```
/html/head/title: 选择HTML文档中 <head> 标签内的 <title> 元素
/html/head/title/text(): 选择上面提到的 <title> 元素的文字
//td: 选择所有的 <td> 元素
//div[@class="mine"]: 选择所有具有 class="mine" 属性的 div 元素
//div[contains(@class,'main')]：选择所有包含 class 名为 main 的 div 元素

normalize-space() 过滤标签
```