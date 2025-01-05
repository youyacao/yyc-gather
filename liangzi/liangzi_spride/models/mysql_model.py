from datetime import datetime

from sqlalchemy import Column, Integer, String, Text, SmallInteger, Float, DateTime, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()


class MovieDetail(Base):
    __tablename__ = 'movie_detail'

    id = Column(Integer, primary_key=True, autoincrement=True, comment='ID')
    user_id = Column(Integer, nullable=False, default=0, comment='发送人ID')
    movie_id = Column(Integer, ForeignKey('movie.id'),nullable=False, default=0, comment='影视ID')
    title = Column(String(255), nullable=False, default=0, comment='标题')
    thumb = Column(String(255), nullable=False, default='', comment='预览图')
    url = Column(String(1000), nullable=False, default='', comment='视频地址')
    intro = Column(String(1024), nullable=False, default='', comment='本集介绍')
    sort = Column(Integer, nullable=False, default=0, comment='排序（越小越靠前）')
    relate_id = Column(Integer, nullable=False, default=0, comment='关联ID')
    status = Column(SmallInteger, nullable=False, default=0, comment='状态0删除1未读2已读')
    updated_at = Column(Integer, nullable=False, default=0, comment='更新时间')
    created_at = Column(Integer, nullable=False, default=0, comment='创建时间')
    view_num = Column(Integer, comment='播放次数')
    thumb_direction = Column(String(255), comment='封面图纵向')
    gold = Column(Integer, default=0, comment='价格')
    advert_view_duration = Column(Integer, comment='广告观看时长')
    is_free = Column(Integer, default=1, comment='是否免费 1免费 0收费')
    num_episodes = Column(String(255), default='0', comment='集数')
    duration = Column(String(55))
    movie = relationship("Movie", back_populates="details")

    def __repr__(self):
        return f"<MovieDetail(id={self.id}, movie_id={self.movie_id})>"

class Movie(Base):
    __tablename__ = 'movie'

    id = Column(Integer, primary_key=True, autoincrement=True, comment='ID')
    actor_id = Column(Integer, comment='演员ID')
    user_id = Column(Integer, nullable=False, default=0, comment='关联user_id')
    category_id = Column(Integer, nullable=False, default=0, comment='分类ID')
    type = Column(String(20), default='', comment='分类MOVIE:电影,TV:剧集,3其他')
    region = Column(String(50), default='', comment='地区国家')
    year = Column(String(20), default='', comment='年份')
    title = Column(String(255), default='', comment='标题')
    subtitle = Column(String(255), comment='副标题')
    thumb = Column(String(255), default='', comment='封面图')
    images = Column(String(5000), default='', comment='多图')
    url = Column(String(255), default='', comment='地址')
    intro = Column(Text, comment='介绍')
    duration = Column(String(50), default='', comment='时长')
    score = Column(Float(3, 1), default=0.0, comment='评分')
    release_date = Column(String(50), default='', comment='上映时间')
    release_address = Column(String(100), default='', comment='上映地点')
    tags = Column(String(255), default='', comment='题材')
    actor_list = Column(String(5000), default='', comment='演员表')
    view_num = Column(Integer, default=0, comment='查看次数')
    like_num = Column(Integer, default=0, comment='点赞次数')
    comment_num = Column(Integer, default=0, comment='评论次数')
    share_num = Column(Integer, default=0, comment='分享次数')
    collect_num = Column(Integer, default=0, comment='收藏次数')
    relate_id = Column(Integer, default=0, comment='关联ID')
    status = Column(SmallInteger, default=1, comment='状态0:删除1:待审核2:审核通过')
    updated_at = Column(DateTime, default=datetime.utcnow, comment='更新时间')
    created_at = Column(Integer, default=0, comment='创建时间')
    gold = Column(String(255), default='0', comment='金币')
    update_episodes = Column(Integer, comment='更新集数')
    is_update_all = Column(Integer, comment='是否全部更新')
    thumb_direction = Column(String(255), comment='纵向封面图')
    director = Column(String(255), comment='导演')
    language = Column(String(255), comment='语言')
    is_episodes = Column(Integer, nullable=False, default=0, comment='是否是剧集')
    sort = Column(Integer, comment='排序号')
    is_recommend = Column(Integer, comment='是否推荐，1是0否')
    is_pop = Column(Integer, comment='是否热门，1是0否')
    is_collection_lock = Column(Integer, default=0, comment='0否 1是')
    details = relationship("MovieDetail", back_populates="movie",cascade="all, delete-orphan" )

    def __repr__(self):
        return f"<Movie(id={self.id}, title='{self.title}')>"
