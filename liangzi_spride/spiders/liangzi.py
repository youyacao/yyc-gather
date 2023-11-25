import json
from typing import Iterable

import scrapy
from scrapy import Request

from liangzi_spride.items import LiangziSprideItem


class LiangziSpider(scrapy.Spider):
    name = "liangzi"

    def __init__(self):
        super(LiangziSpider, self).__init__()

        self.file2 = 'liangzi_spride/myclass.json'
        # 创建配置文件对象
        with open(self.file2, 'r', encoding='utf-8') as f:
            file_content = f.read()
            self.type_class = json.loads(file_content)

    def start_requests(self) -> Iterable[Request]:
        for my_type_class in self.type_class:
            type_id = my_type_class['type_id']
            url = 'https://cj.lzcaiji.com/api.php/provide/vod/?ac=list&t=%d&pg=1' % type_id
            yield scrapy.Request(url=url, callback=self.parse, dont_filter=True)

    def parse(self, response):
        data = json.loads(response.text)
        if data['code'] == 1:
            mytype = {'page': data['page'], 'count': data['pagecount'], 'total': data['total']}
            if mytype.get('count') > 1:
                for item in data['list']:
                    items = LiangziSprideItem()
                    items['vod_id'] = item.get('vod_id', 0)
                    items['vod_name'] = item.get('vod_name', 0)
                    items['type_id'] = item.get('type_id', 0)
                    items['type_name'] = item.get('type_name', '采集失败')
                    items['vod_time'] = item.get('vod_time', 0)
                    items['vod_remarks'] = item.get('vod_remarks', '采集失败')
                    items['vod_play_from'] = item.get('vod_play_from', '采集失败')
                    detail_url = 'https://cj.lziapi.com/api.php/provide/vod/?ac=detail&ids=%d' % item.get('vod_id', 0)
                    yield Request(
                        url=detail_url, callback=self.detail_parse, cb_kwargs=dict(item=item), dont_filter=True
                    )

                if int(mytype.get('page')) < int(mytype.get('count')):
                    sub_url = response.url.rfind('=')
                    result = response.url[:sub_url + 1] + str(int(mytype.get('page')) + 1)
                    print(f"正在采集第{int(mytype.get('page'))}页--地址：{result}")
                    yield scrapy.Request(url=result, callback=self.parse, dont_filter=True)

    def detail_parse(self, response, item):
        data = json.loads(response.text)
        if data['code'] == 1:
            item['vod_pic'] = data['list'][0]['vod_pic']
            item['vod_actor'] = data['list'][0]['vod_actor']
            item['super_type_id'] = data['list'][0]['type_id_1']
            item['vod_director'] = data['list'][0]['vod_director']
            item['vod_blurb'] = data['list'][0]['vod_blurb']
            item['vod_area'] = data['list'][0]['vod_area']
            item['vod_lang'] = data['list'][0]['vod_lang']
            item['vod_year'] = data['list'][0]['vod_year']
            item['vod_play_url'] = (data['list'][0]['vod_play_url']).split('#')
            item['vod_down_url'] = data['list'][0]['vod_down_url'].split('#')
        yield item
