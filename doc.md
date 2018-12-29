
# Scrapy 教程

## 基本操作

``` bash
    1、创建项目：scrapy startproject cnblogs(项目名称)
```

``` bash
    2、目录结构：
        cnblogs: 项目目录
        spiders: 爬虫目录
        items.py: 该文件定义需要获取的字段
        pipelines: 该文件定义存储引擎
        settings: 该文件配置各种设置
```

``` bash
    3、配置IDE调试：
        Scrapy默认是不能在IDE中调试的，我们在根目录中新建一个py文件叫：begin.py；在里面写入以下内容：
```

<code> from scrapy import cmdline </code>

<code> cmdline.execute("scrapy crawl dingdian".split()) </code>


# XPath 教程

## 示例

```
/html/head/title: 选择HTML文档中 <head> 标签内的 <title> 元素
/html/head/title/text(): 选择上面提到的 <title> 元素的文字
//td: 选择所有的 <td> 元素
//div[@class="mine"]: 选择所有具有 class="mine" 属性的 div 元素
```