# -*- coding: utf-8 -*-

from sqlalchemy import Integer, Column, create_engine, String, Float, INT
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# from db.db_init import Base


Base = declarative_base()


def model_init():
    engine = create_engine('mysql+pymysql://root:123456@localhost/btb?charset=utf8', encoding='utf-8', echo=True)

    Base.metadata.create_all(engine)
    session = sessionmaker(bind=engine)
    sess = session()
    sess.close()


class K_1M(Base):
    __tablename__ = 'K_1M'
    ID = Column(Integer, autoincrement=True, primary_key=True)
    # 开盘价格
    KAI_PAN = Column(Float)
    # 最高价格
    ZUI_GAO = Column(Float)
    # 最低价格
    ZUI_DI = Column(Float)
    # 收盘价格
    SHOU_PAN = Column(Float)

    VOLUME = Column(Float)
    # 当前日期+时间
    CUR_DATE = Column(String(50))

    LAST_TIME = Column(INT)


class K_5M(Base):
    __tablename__ = 'K_5M'
    ID = Column(Integer, autoincrement=True, primary_key=True)
    # 开盘价格
    KAI_PAN = Column(Float)
    # 最高价格
    ZUI_GAO = Column(Float)
    # 最低价格
    ZUI_DI = Column(Float)
    # 收盘价格
    SHOU_PAN = Column(Float)
    # 当前日期+时间
    CUR_DATE = Column(String(50))
    # 成交量
    VOLUME = Column(Float)
    LAST_TIME = Column(INT)


class K_3M(Base):
    __tablename__ = 'K_3M'
    ID = Column(Integer, autoincrement=True, primary_key=True)
    # 开盘价格
    KAI_PAN = Column(Float)
    # 最高价格
    ZUI_GAO = Column(Float)
    # 最低价格
    ZUI_DI = Column(Float)
    # 收盘价格
    SHOU_PAN = Column(Float)
    # 当前日期+时间
    CUR_DATE = Column(String(50))
    # 成交量
    VOLUME = Column(Float)
    LAST_TIME = Column(INT)


class K_10M(Base):
    __tablename__ = 'K_10M'
    ID = Column(Integer, autoincrement=True, primary_key=True)
    # 开盘价格
    KAI_PAN = Column(Float)
    # 最高价格
    ZUI_GAO = Column(Float)
    # 最低价格
    ZUI_DI = Column(Float)
    # 收盘价格
    SHOU_PAN = Column(Float)
    # 当前日期+时间
    CUR_DATE = Column(String(50))
    # 成交量
    VOLUME = Column(Float)
    LAST_TIME = Column(INT)


class K_12H(Base):
    __tablename__ = 'K_12H'
    ID = Column(Integer, autoincrement=True, primary_key=True)
    # 开盘价格
    KAI_PAN = Column(Float)
    # 最高价格
    ZUI_GAO = Column(Float)
    # 最低价格
    ZUI_DI = Column(Float)
    # 收盘价格
    SHOU_PAN = Column(Float)
    # 当前日期+时间
    CUR_DATE = Column(String(50))
    # 成交量
    VOLUME = Column(Float)
    LAST_TIME = Column(INT)


class K_6H(Base):
    __tablename__ = 'K_6H'
    ID = Column(Integer, autoincrement=True, primary_key=True)
    # 开盘价格
    KAI_PAN = Column(Float)
    # 最高价格
    ZUI_GAO = Column(Float)
    # 最低价格
    ZUI_DI = Column(Float)
    # 收盘价格
    SHOU_PAN = Column(Float)
    # 当前日期+时间
    CUR_DATE = Column(String(50))
    # 成交量
    VOLUME = Column(Float)
    LAST_TIME = Column(INT)


class K_4H(Base):
    __tablename__ = 'K_4H'
    ID = Column(Integer, autoincrement=True, primary_key=True)
    # 开盘价格
    KAI_PAN = Column(Float)
    # 最高价格
    ZUI_GAO = Column(Float)
    # 最低价格
    ZUI_DI = Column(Float)
    # 收盘价格
    SHOU_PAN = Column(Float)
    # 当前日期+时间
    CUR_DATE = Column(String(50))
    # 成交量
    VOLUME = Column(Float)
    LAST_TIME = Column(INT)


class K_2H(Base):
    __tablename__ = 'K_2H'
    ID = Column(Integer, autoincrement=True, primary_key=True)
    # 开盘价格
    KAI_PAN = Column(Float)
    # 最高价格
    ZUI_GAO = Column(Float)
    # 最低价格
    ZUI_DI = Column(Float)
    # 收盘价格
    SHOU_PAN = Column(Float)
    # 当前日期+时间
    CUR_DATE = Column(String(50))
    # 成交量
    VOLUME = Column(Float)
    LAST_TIME = Column(INT)


class K_3D(Base):
    __tablename__ = 'K_3D'
    ID = Column(Integer, autoincrement=True, primary_key=True)
    # 开盘价格
    KAI_PAN = Column(Float)
    # 最高价格
    ZUI_GAO = Column(Float)
    # 最低价格
    ZUI_DI = Column(Float)
    # 收盘价格
    SHOU_PAN = Column(Float)
    # 当前日期+时间
    CUR_DATE = Column(String(50))
    # 成交量
    VOLUME = Column(Float)
    LAST_TIME = Column(INT)


class K_1H(Base):
    __tablename__ = 'K_1H'
    ID = Column(Integer, autoincrement=True, primary_key=True)
    # 开盘价格
    KAI_PAN = Column(Float)
    # 最高价格
    ZUI_GAO = Column(Float)
    # 最低价格
    ZUI_DI = Column(Float)
    # 收盘价格
    SHOU_PAN = Column(Float)
    # 当前日期+时间
    CUR_DATE = Column(String(50))
    # 成交量
    VOLUME = Column(Float)
    LAST_TIME = Column(INT)


class K_WEEK(Base):
    __tablename__ = 'K_WEEK'
    ID = Column(Integer, autoincrement=True, primary_key=True)
    # 开盘价格
    KAI_PAN = Column(Float)
    # 最高价格
    ZUI_GAO = Column(Float)
    # 最低价格
    ZUI_DI = Column(Float)
    # 收盘价格
    SHOU_PAN = Column(Float)
    # 当前日期+时间
    CUR_DATE = Column(String(50))
    # 成交量
    VOLUME = Column(Float)
    LAST_TIME = Column(INT)


class K_MONTH(Base):
    __tablename__ = 'K_MONTH'
    ID = Column(Integer, autoincrement=True, primary_key=True)
    # 开盘价格
    KAI_PAN = Column(Float)
    # 最高价格
    ZUI_GAO = Column(Float)
    # 最低价格
    ZUI_DI = Column(Float)
    # 收盘价格
    SHOU_PAN = Column(Float)
    # 当前日期+时间
    CUR_DATE = Column(String(50))
    # 成交量
    VOLUME = Column(Float)
    LAST_TIME = Column(INT)


class K_15M(Base):
    __tablename__ = 'K_15M'
    ID = Column(Integer, autoincrement=True, primary_key=True)
    # 开盘价格
    KAI_PAN = Column(Float)
    # 最高价格
    ZUI_GAO = Column(Float)
    # 最低价格
    ZUI_DI = Column(Float)
    # 收盘价格
    SHOU_PAN = Column(Float)
    # 当前日期+时间
    CUR_DATE = Column(String(50))
    VOLUME = Column(Float)
    LAST_TIME = Column(INT)


class K_30M(Base):
    __tablename__ = 'K_30M'
    ID = Column(Integer, autoincrement=True, primary_key=True)
    # 开盘价格
    KAI_PAN = Column(Float)
    # 最高价格
    ZUI_GAO = Column(Float)
    # 最低价格
    ZUI_DI = Column(Float)
    # 收盘价格
    SHOU_PAN = Column(Float)
    # 当前日期+时间
    CUR_DATE = Column(String(50))
    VOLUME = Column(Float)
    LAST_TIME = Column(INT)


class K_1D(Base):
    __tablename__ = 'K_1D'
    ID = Column(Integer, autoincrement=True, primary_key=True)
    # 开盘价格
    KAI_PAN = Column(Float)
    # 最高价格
    ZUI_GAO = Column(Float)
    # 最低价格
    ZUI_DI = Column(Float)
    # 收盘价格
    SHOU_PAN = Column(Float)
    # 当前日期+时间
    CUR_DATE = Column(String(50))
    VOLUME = Column(Float)
    LAST_TIME = Column(INT)


class Deal_Rec(Base):
    __tablename__ = 'DEAL_RECORD'
    ID = Column(Integer, autoincrement=True, primary_key=True)
    # 成交类型
    DEAL_KIND = Column(String(20))
    # 成交量
    VOLUME = Column(Float)
    # 成交价格
    PRICE = Column(Float)
    # 总金额
    TOTAL = Column(Float)
    # 成交时间
    CUR_DATE = Column(String(50))
    LAST_TIME = Column(INT)


if __name__ == '__main__':
    model_init()
