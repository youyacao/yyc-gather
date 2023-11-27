# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class LiangziSprideItem(scrapy.Item):
    # define the fields for your item here like:
    vod_id = scrapy.Field()
    vod_name = scrapy.Field()
    vod_sub = scrapy.Field()
    type_id = scrapy.Field()
    super_type_id = scrapy.Field()
    type_name = scrapy.Field()
    vod_time = scrapy.Field()
    vod_remarks = scrapy.Field()
    vod_play_from = scrapy.Field()
    vod_pic = scrapy.Field() # 封面
    vod_play_url = scrapy.Field() # 播放地址
    vod_down_url = scrapy.Field() # 下载地址
    vod_actor = scrapy.Field() # 演员
    vod_director = scrapy.Field() # 导演
    vod_blurb = scrapy.Field() # 简介
    vod_area = scrapy.Field() # 国家
    vod_pubdate = scrapy.Field() # 上映时间
    vod_score = scrapy.Field() # 豆瓣评分
    vod_lang = scrapy.Field() # 语言
    vod_year = scrapy.Field() # 年份
    pass
