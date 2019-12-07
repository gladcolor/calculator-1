import sqlite3
import sqlalchemy
from sqlalchemy import ARRAY

from sqlalchemy import create_engine, MetaData, Table, Integer, String, \
    Column, DateTime, ForeignKey, Numeric, CheckConstraint

from datetime import datetime
from sqlalchemy.orm import sessionmaker, Session
from sqlalchemy import create_engine
from sqlalchemy.dialects import sqlite

from sqlalchemy import Column, String, create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

print(sqlalchemy.__version__)

Base = declarative_base()


engine = create_engine("sqlite:///huan.db")
engine.connect()
Session = sessionmaker(bind=engine)
metadata = MetaData()
metadata.create_all(engine)
session = Session()
print('engine:', engine)

print('metadata: ', metadata)
from sqlalchemy import create_engine, MetaData, Table, Integer, String, \
    Column, DateTime, ForeignKey, Numeric
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime
from sqlalchemy.orm import mapper

Base = declarative_base()


conn = engine.connect()
metadata.create_all(engine)

metadata = MetaData()

#
# clear_mappers()
# mapper(Post, post)

#
# for t in metadata.sorted_tables:
#     print(t.name)  # print table name

#
# c1 = Customer(first_name='Toby',
#               last_name='Miller',
#               username='tmiller',
#               email='tmiller@example.com',
#               address='1662 Kinney Street',
#               town='Wolfden'
#               )
#
# c2 = Customer(first_name='Scott',
#               last_name='Harvey',
#               username='scottharvey',
#               email='scottharvey@example.com',
#               address='424 Patterson Street',
#               town='Beckinsdale'
#               )
# c1, c2



# conn = sqlite3.connect('huan.db')