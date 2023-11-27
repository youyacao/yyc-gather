#### 介绍

```
爬取量子资源网数据

dbconf.py是数据库配置

myclass_back.json是分类原始数据 在这里查看需要采集的分类，复制分类到  myclass.py中进行采集

安装好requirements.txt中的第三方包后就可以开始用命令开始采集

采集命令：scrapy  crawl liangzi
```

myclass.py是需要爬取的分类树，这里可以控制爬取的分类

