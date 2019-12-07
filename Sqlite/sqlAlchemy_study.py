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


class Post(Base):
    __tablename__ = 'posts'
    id = Column(Integer, primary_key=True)
    title = Column(String(100), nullable=False)
    slug = Column(String(100), nullable=False)
    content = Column(String(50), nullable=False)
    published = Column(String(200), nullable=False, unique=True)
    created_on = Column(DateTime(), default=datetime.now)
    updated_on = Column(DateTime(), default=datetime.now, onupdate=datetime.now)


from sqlalchemy import MetaData, Table, String, Column, Text, DateTime, Boolean
from sqlalchemy.orm import mapper
from datetime import datetime

metadata = MetaData()
metadata.drop_all(engine)
post = Table('post', metadata,
             Column('id', Integer(), primary_key=True),
             Column('title', String(200), nullable=False),
             Column('slug', String(200), nullable=False),
             Column('content', Text(), nullable=False),
             Column('published', Boolean(), default=False),
             Column('created_on', DateTime(), default=datetime.now),
             Column('updated_on', DateTime(), default=datetime.now, onupdate=datetime.now)
)



mapper(Post, post)
conn = engine.connect()
metadata.create_all(engine)


# metadata.drop_all(engine)
for t in metadata.tables:
    print(metadata.tables[t])

print('-------------')

for t in metadata.sorted_tables:
    print(t.name)  # print table name

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