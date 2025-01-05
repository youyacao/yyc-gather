# -*- coding: utf-8 -*-
import scrapy
import json
import requests
import emoji
from ..items import DouyinSprideItem
import configparser

#抖音 视频标签视频采集
class DouyinSpider(scrapy.Spider):

    file = 'config.ini'
    # 创建配置文件对象
    con = configparser.ConfigParser()

    # 读取文件
    con.read(file, encoding='utf-8')

    # 获取特定section
    items = con.items('music') 	# 返回结果为元组
    # [('baidu','http://www.baidu.com'),('port', '80')] 	# 数字也默认读取为字符串
    # 可以通过dict方法转换为字典
    items = dict(items)
    print("当前采集从第%s页开始，每页%s条数据，本次采集%s页数据"%(items['page'],items['size'],items['max_page']))
    #当前页数
    page=int(items['page'])
    #每页数据大小
    size=int(items["size"])
    #采集页数
    max_page=page+int(items["max_page"])
    #采集地址
    url='https://www.iesdouyin.com/web/api/v2/challenge/aweme/?ch_id=1550169395535874&count=%d&cursor=%d&aid=1128&screen_limit=3&download_click_limit=0&_signature=aH.ejhAWNpVhM6SbAlvK5Wh.3p'%(size,size*page)

    name = 'douyin_wudao'
    allowed_domains = ['www.iesdouyin.com']
    start_urls = [url]
    def parse(self, response):
        self.page+=1
        data = json.loads(response.text)
        if(data['status_code']==0):
            url='https://www.iesdouyin.com/web/api/v2/challenge/aweme/?ch_id=1550169395535874&count=%d&cursor=%d&aid=1128&screen_limit=3&download_click_limit=0&_signature=aH.ejhAWNpVhM6SbAlvK5Wh.3p'%(self.size,(self.size*self.page))
            for item in data['aweme_list']:
                #视频ID
                id = item['aweme_id']
                #标题
                title=item['desc']
                #采集标签
                if(item['cha_list'] and item['cha_list'][0]):
                    tag = item['cha_list'][0]['cha_name']
                else:
                    tag = ""
                #播放地址
                play_url = item['video']['play_addr']['url_list'][0].replace("/playwm/", "/play/")
                source_url = play_url
                #play_url = self.get_real_url(play_url)
                #封面图
                image = item['video']['origin_cover']['url_list'][0]
                #创建时间
                time = item['create_time']
                #创建数据结构
                items = DouyinSprideItem()
                items['id']=id
                items['source_url']=source_url
                #items['play_url']=play_url
                items['title']=emoji.emojize(title)
                items['tag']=tag
                items['image']=image
                items['time']=time
                yield items
            if(self.page>=self.max_page):
                self.con.set('wudao', 'page',str(self.page))# 给music分组的page属性设置值
                self.con.write(open(self.file,'w'))
                print("采集完成")
                pass
            else:
                print("正在采集第%d页"%self.page)
                yield scrapy.Request(url, callback=self.parse, dont_filter=True)
        else:
            self.con.set('wudao', 'page',str(self.page))# 给music分组的page属性设置值
            print("采集完成")
    def get_real_url(self,url):
        header = {
            "User-Agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Mobile Safari/537.36",
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
            "Accept-Encoding": "gzip, deflate, br",
            "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8",
            "Cache-Control": "no-cache",
            "Connection": "keep-alive",
            "Host": "aweme.snssdk.com",
            "Pragma": "no-cache",
            "Sec-Fetch-Mode": "navigate",
            "Sec-Fetch-Site": "none",
            "Sec-Fetch-User": "?1",
            "Upgrade-Insecure-Requests": "1",
        }
        res=requests.get(url,headers=header,verify=False,allow_redirects=False)
        print("跳转地址:%s"%res.headers['Location'])
        return res.headers['Location'] if res.status_code == 302 else None