# -*- coding: utf-8 -*-
from scrapy import cmdline
import datetime
now_time = datetime.datetime.now().strftime('%Y%m%d/%Y%m%d%H%M%S')
print(now_time)
print("===================开始采集抖音 舞蹈标签视频=====================")
cmdline.execute(('scrapy crawl douyin_wudao -o wudao_data/%s.csv'%now_time).split())

