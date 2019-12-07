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

from sqlalchemy import create_engine, MetaData, Table, Integer, String, \
    Column, DateTime, ForeignKey, Numeric, SmallInteger

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

from datetime import datetime


Base = declarative_base()


class Customer(Base):
    __tablename__ = 'customers'
    id = Column(Integer(), primary_key=True)
    first_name = Column(String(100), nullable=False)
    last_name = Column(String(100), nullable=False)
    username = Column(String(50), nullable=False)
    email = Column(String(200), nullable=False)
    created_on = Column(DateTime(), default=datetime.now)
    updated_on = Column(DateTime(), default=datetime.now, onupdate=datetime.now)
    orders = relationship("Order", backref='customer')


class Item(Base):
    __tablename__ = 'items'
    id = Column(Integer(), primary_key=True)
    name = Column(String(200), nullable=False)
    cost_price = Column(Numeric(10, 2), nullable=False)
    selling_price = Column(Numeric(10, 2), nullable=False)


#     orders = relationship("Order", backref='customer')


class Order(Base):
    __tablename__ = 'orders'
    id = Column(Integer(), primary_key=True)
    customer_id = Column(Integer(), ForeignKey('customers.id'))
    date_placed = Column(DateTime(), default=datetime.now)
    line_items = relationship("OrderLine", secondary="order_lines", backref='order')


class OrderLine(Base):
    __tablename__ = 'order_lines'
    id = Column(Integer(), primary_key=True)
    order_id = Column(Integer(), ForeignKey('orders.id'))
    item_id = Column(Integer(), ForeignKey('items.id'))
    quantity = Column(SmallInteger())
    item = relationship("Item")


Base.metadata.create_all(engine)
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