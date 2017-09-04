# -*- coding: utf-8 -*-
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import threading

Base = declarative_base()
engine = create_engine('mysql+pymysql://root:123456@localhost/btb?charset=utf8', encoding='utf-8', echo=True)

Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
db_session = Session()


lock = threading.RLock()