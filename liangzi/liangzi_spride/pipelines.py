# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import re

import openpyxl
# useful for handling different item types with a single interface
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from liangzi_spride.models.mysql_model import Base, Movie, MovieDetail

from liangzi_spride.dbconf import dbconf

class LiangziSpridePipeline:
    def __init__(self):
        self.wb = openpyxl.Workbook()
        self.ws = self.wb.active
        self.ws.title = 'Video'
        self.ws.append(('已更新集数（数字）', '是否已完结（1:0)', '分类ID（字典管理可查）', '题材ID（字典管理可查）',
                        '地区/国家ID', '年份ID（字典管理可查）', '标题', '副标题', '介绍', '时长',
                        '评分（数字）', '上映时间', '演员表', '查看次数（数字）', '点赞次数（数字）', '分享次数（数字）',
                        '收藏次数（数字）', '关联ID', '导演', '语言', '状态（0:删除1:待审核2:审核通过）',
                        '采集锁定（0:否1:是）'))

    def close_spider(self, spider):
        self.wb.save('体育视频.xlsx')

    def process_item(self, item, spider):
        vod_id = item.get('vod_id', '')
        vod_name = item.get('vod_name', '')
        type_id = item.get('type_id', '')
        super_type_id = item.get('super_type_id', '')
        type_name = item.get('type_name', '')
        vod_sub = item.get('vod_sub', '')
        vod_time = item.get('vod_time', '')
        vod_remarks = item.get('vod_remarks', '')
        vod_play_from = item.get('vod_play_from', '')
        vod_pic = item.get('vod_pic', '')  # 封面
        vod_play_url = item.get('vod_play_url', '')  # 播放地址
        vod_down_url = item.get('vod_down_url', '')  # 下载地址
        vod_actor = item.get('vod_actor', '')  # 演员
        vod_director = item.get('vod_director', '')  # 导演
        vod_blurb = item.get('vod_blurb', '')  # 简介
        vod_area = item.get('vod_area', '')  # 国家
        vod_score = item.get('vod_score', '')  # 评分
        vod_pubdate = item.get('vod_pubdate', '')  # 上映时间
        vod_lang = item.get('vod_lang', '')  # 语言
        vod_year = item.get('vod_year', '')  # 年份
        if type_id == 40:
            self.ws.append(
                (vod_remarks, '是否已完结', type_id, '题材ID', vod_area, vod_year, vod_name, vod_sub, vod_blurb,
                 '时长', vod_score, vod_pubdate, vod_actor, '查看次数', '点赞次数', '分享次数', '收藏次数',
                 super_type_id, vod_director, vod_lang, 1, 1))
        return item


class hanjuSpridePipeline:
    def __init__(self):
        self.wb = openpyxl.Workbook()
        self.ws = self.wb.active
        self.ws.title = 'Video'
        self.ws.append(('已更新集数（数字）', '是否已完结（1:0)', '分类ID（字典管理可查）', '题材ID（字典管理可查）',
                        '地区/国家ID', '年份ID（字典管理可查）', '标题', '副标题', '介绍', '时长',
                        '评分（数字）', '上映时间', '演员表', '查看次数（数字）', '点赞次数（数字）', '分享次数（数字）',
                        '收藏次数（数字）', '关联ID', '导演', '语言', '状态（0:删除1:待审核2:审核通过）',
                        '采集锁定（0:否1:是）'))

    def close_spider(self, spider):
        self.wb.save('韩剧视频.xlsx')

    def process_item(self, item, spider):
        # vod_id = item.get('vod_id', '')
        vod_name = item.get('vod_name', '')
        type_id = item.get('type_id', '')
        super_type_id = item.get('super_type_id', '')
        type_name = item.get('type_name', '')
        vod_sub = item.get('vod_sub', '')
        vod_time = item.get('vod_time', '')
        vod_remarks = item.get('vod_remarks', '')
        vod_play_from = item.get('vod_play_from', '')
        vod_pic = item.get('vod_pic', '')  # 封面
        vod_play_url = item.get('vod_play_url', '')  # 播放地址
        vod_down_url = item.get('vod_down_url', '')  # 下载地址
        vod_actor = item.get('vod_actor', '')  # 演员
        vod_director = item.get('vod_director', '')  # 导演
        vod_blurb = item.get('vod_blurb', '')  # 简介
        vod_area = item.get('vod_area', '')  # 国家
        vod_score = item.get('vod_score', '')  # 评分
        vod_pubdate = item.get('vod_pubdate', '')  # 上映时间
        vod_lang = item.get('vod_lang', '')  # 语言
        vod_year = item.get('vod_year', '')  # 年份
        if type_id == 15:
            self.ws.append(
                (vod_remarks, '是否已完结', type_id, '题材ID', vod_area, vod_year, vod_name, vod_sub, vod_blurb,
                 '时长', vod_score, vod_pubdate, vod_actor, '查看次数', '点赞次数', '分享次数', '收藏次数',
                 super_type_id, vod_director, vod_lang, 1, 1))
        return item


class MySqlSpridePipeline:
    def __init__(self):
        self.mysqlsession = None
        self.video_type_dy = [6, 7, 8, 9, 10, 11, 12, 20, 34, 45]
        self.video_type_esps = [13, 14, 15, 16, 21, 22, 23, 24, 46]

    def open_spider(self, spider):
        engine = create_engine('mysql+pymysql://'+dbconf.get('user')+':'+dbconf.get('password')+'@'+dbconf.get('host')+ '/'+dbconf.get('database')+'')
        Base.metadata.create_all(engine)
        # 创建 SQLAlchemy 会话对象
        Session = sessionmaker(bind=engine)
        self.mysqlsession = Session()

    def close_spider(self, spider):
        self.mysqlsession.close()

    def process_item(self, item, spider):
        # vod_id = item.get('vod_id', '')
        vod_name = item.get('vod_name', '')
        type_id = item.get('type_id', '')
        super_type_id = item.get('super_type_id', '')
        type_name = item.get('type_name', '')
        vod_sub = item.get('vod_sub', '')
        vod_time = item.get('vod_time', '')
        vod_remarks = item.get('vod_remarks', '')
        vod_play_from = item.get('vod_play_from', '')
        vod_pic = item.get('vod_pic', '')  # 封面
        vod_play_url = item.get('vod_play_url', '')  # 播放地址
        vod_down_url = item.get('vod_down_url', '')  # 下载地址
        vod_actor = item.get('vod_actor', '')  # 演员
        vod_director = item.get('vod_director', '')  # 导演
        vod_blurb = item.get('vod_blurb', '')  # 简介
        vod_area = item.get('vod_area', '')  # 国家
        vod_score = item.get('vod_score', '')  # 评分
        vod_pubdate = item.get('vod_pubdate', '')  # 上映时间
        vod_lang = item.get('vod_lang', '')  # 语言
        vod_year = item.get('vod_year', '')  # 年份
        movie_data = self.mysqlsession.query(Movie).filter(Movie.title.like("%" + vod_name + "%")).first()
        if movie_data is not None:  # Movie数据查到了
            if not movie_data.details:
                parts = vod_play_url.split('$$$')
                urls_list = []
                exp_list = []
                for part in parts:
                    exp = [x.split('$')[0] for x in part.split('#')]
                    urls = [(x.split('$')[1]).replace("\\", "") for x in part.split('#')]
                    exp_list.append(exp)  # 集数
                    urls_list.append({exp[i]: urls[i] for i in range(len(exp))})  # url地址

                parts = vod_play_url.split('$$$')
                urls_list = []
                for part in parts:
                    urls = [x.split('$')[1].replace("\\", "") for x in part.split('#')]
                    exp = [x.split('$')[0] for x in part.split('#')]
                    urls_list.append({exp[i]: urls[i] for i in range(len(exp))})
                for tt in urls_list[0]:
                    number_part = re.search(r'\d+', tt).group()
                    number = int(number_part)  # 纯数字集数   带文字的  直接用tt
                    details_filter = {
                        'movie_id': movie_data.id,
                        'title': vod_name + tt,
                        'url': urls_list[0][tt],
                        'sort': number,
                        'is_free': 1,
                    }
                    new_data1 = MovieDetail(**details_filter)
                    self.mysqlsession.add(new_data1)
        else:  # Movie数据没有查到
            query_filter = {'category_id': type_id, 'region': vod_area, 'year': vod_year, 'title': vod_name,
                            'subtitle': vod_sub,
                            'intro': vod_blurb, 'score': vod_score, 'release_date': vod_pubdate, 'thumb': vod_pic,
                            'actor_list': vod_actor, 'relate_id': super_type_id, 'status': 1,
                            'director': vod_director, 'language': vod_lang, 'type': 3}
            if type_id in self.video_type_dy:
                query_filter['type'] = 1
            if type_id in self.video_type_esps:
                query_filter['type'] = 2
            parts = vod_play_url.split('$$$')
            urls_list = []
            exp_list = []
            for part in parts:
                exp = [x.split('$')[0] for x in part.split('#')]
                urls = [(x.split('$')[1]).replace("\\", "") for x in part.split('#')]
                exp_list.append(exp)  # 集数
                urls_list.append({exp[i]: urls[i] for i in range(len(exp))})  # url地址

            parts = vod_play_url.split('$$$')
            urls_list = []
            for part in parts:
                urls = [x.split('$')[1].replace("\\", "") for x in part.split('#')]
                exp = [x.split('$')[0] for x in part.split('#')]
                urls_list.append({exp[i]: urls[i] for i in range(len(exp))})
            details = []
            for tt in urls_list[0]:
                number_part = re.search(r'\d+', tt).group()
                number = int(number_part)  # 纯数字集数   带文字的  直接用tt
                details_filter = {
                    'title': vod_name + tt,
                    'url': urls_list[0][tt],
                    'sort': number,
                    'is_free': 1,
                }
                details.append(MovieDetail(**details_filter))
            query_filter['details'] = details
            new_data = Movie(**query_filter)
            self.mysqlsession.add(new_data)

        self.mysqlsession.commit()

        return item
