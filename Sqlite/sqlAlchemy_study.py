import sqlite3
import sqlalchemy
from sqlalchemy import ARRAY
from sqlalchemy import MetaData, Table, String, Column, Text, DateTime, Boolean, Integer
from datetime import datetime
from sqlalchemy.orm import sessionmaker, Session
from sqlalchemy import create_engine
from sqlalchemy.dialects import sqlite

print(sqlalchemy.__version__)


# metadata.create_all(engine)




engine = create_engine("sqlite:///huan.db", echo=True)
engine.connect()
Session = sessionmaker(bind=engine)
metadata = MetaData()
metadata.create_all(engine)
session = Session()
print('engine:', engine)

print('metadata: ', metadata)
# blog = Table('blog', metadata,
#     Column('id', Integer(), primary_key=True),
#     Column('post_title', String(200), nullable=False),
#     Column('post_slug', String(200),  nullable=False),
#     Column('content', Text(),  nullable=False),
#     Column('published', Boolean(),  default=False),
#     Column('created_on', DateTime(), default=datetime.now),
#     Column('updated_on', DateTime(), default=datetime.now, onupdate=datetime.now)
# )

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