import sqlite3
import sqlalchemy
from sqlalchemy import ARRAY
from sqlalchemy import MetaData, Table, String, Column, Text, DateTime, Boolean, Integer
from datetime import datetime
from sqlalchemy.orm import sessionmaker, Session
from sqlalchemy import create_engine
from sqlalchemy.dialects import sqlite

print(sqlalchemy.__version__)

engine = create_engine("sqlite:///huan.db")

engine.connect()

print(engine)

metadata = MetaData()


metadata.create_all(engine)
Session = sessionmaker(bind=engine)

session = Session()
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