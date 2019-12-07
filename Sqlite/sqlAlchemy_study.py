import sqlite3
import sqlalchemy
from sqlalchemy import ARRAY
from sqlalchemy import *
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
    address = Column(String(200), nullable=False)
    town = Column(String(200), nullable=False)
    created_on = Column(DateTime(), default=datetime.now)
    updated_on = Column(DateTime(), default=datetime.now, onupdate=datetime.now)
    orders = relationship("Order", backref='customers')

class Item(Base):
    __tablename__ = 'items'
    id = Column(Integer(), primary_key=True)
    name = Column(String(200), nullable=False)
    cost_price =  Column(Numeric(10, 2), nullable=False)
    selling_price = Column(Numeric(10, 2),  nullable=False)
#     orders = relationship("Order", backref='customer')

    quantity = Column(String(200), nullable=False)

#
class Order(Base):
    __tablename__ = 'orders'
    id = Column(Integer(), primary_key=True)
    customer_id = Column(Integer(), ForeignKey('customers.id'))
    date_placed = Column(DateTime(), default=datetime.now)
    line_items = relationship("OrderLine")#, secondary="order_lines")#, backref='orders')
    customer  = relationship("Customer")
    order_lines = relationship("OrderLine")
    date_shipped = Column(DateTime())
#
class OrderLine(Base):
    __tablename__ = 'order_lines'
    id = Column(Integer(), primary_key=True)
    order_id = Column(Integer(), ForeignKey('orders.id'))
    item_id = Column(Integer(), ForeignKey('items.id'))
    quantity = Column(SmallInteger())
    item = relationship("Item")
    order = relationship("Order")

'''
c1 = Customer(first_name='Toby',
              last_name='Miller',
              username='tmiller',
              email='tmiller@example.com',
              address='1662 Kinney Street',
              town='Wolfden'
              )

c2 = Customer(first_name='Scott',
              last_name='Harvey',
              username='scottharvey',
              email='scottharvey@example.com',
              address='424 Patterson Street',
              town='Beckinsdale'
              )

print('c1.c1.first_name: ', str(c1.first_name))

session.add(c1)
session.add(c2)
session.commit()

c3 = Customer(
    first_name="John",
    last_name="Lara",
    username="johnlara",
    email="johnlara@mail.com",
    address="3073 Derek Drive",
    town="Norfolk"
)

c4 = Customer(
    first_name="Sarah",
    last_name="Tomlin",
    username="sarahtomlin",
    email="sarahtomlin@mail.com",
    address="3572 Poplar Avenue",
    town="Norfolk"
)

c5 = Customer(first_name='Toby',
              last_name='Miller',
              username='tmiller',
              email='tmiller@example.com',
              address='1662 Kinney Street',
              town='Wolfden'
              )

c6 = Customer(first_name='Scott',
              last_name='Harvey',
              username='scottharvey',
              email='scottharvey@example.com',
              address='424 Patterson Street',
              town='Beckinsdale'
              )

session.add_all([c3, c4, c5, c6])
session.commit()
# conn = sqlite3.connect('huan.db')

i1 = Item(name='Chair', cost_price=9.21, selling_price=10.81, quantity=5)
i2 = Item(name='Pen', cost_price=3.45, selling_price=4.51, quantity=3)
i3 = Item(name='Headphone', cost_price=15.52, selling_price=16.81, quantity=50)
i4 = Item(name='Travel Bag', cost_price=20.1, selling_price=24.21, quantity=50)
i5 = Item(name='Keyboard', cost_price=20.1, selling_price=22.11, quantity=50)
i6 = Item(name='Monitor', cost_price=200.14, selling_price=212.89, quantity=50)
i7 = Item(name='Watch', cost_price=100.58, selling_price=104.41, quantity=50)
i8 = Item(name='Water Bottle', cost_price=20.89, selling_price=25, quantity=50)

session.add_all([i1, i2, i3, i4, i5, i6, i7, i8])
session.commit()

o1 = Order(customer=c1)
o2 = Order(customer=c1)

line_item1 = OrderLine(order=o1, item=i1, quantity=3)
line_item2 = OrderLine(order=o1, item=i2, quantity=2)
line_item3 = OrderLine(order=o2, item=i1, quantity=1)
line_item3 = OrderLine(order=o2, item=i2, quantity=4)

session.add_all([o1, o2])

session.new
session.commit()

o3 = Order(customer=c1)
orderline1 = OrderLine(item=i1, quantity=5)
orderline2 = OrderLine(item=i2, quantity=10)

o3.order_lines.append(orderline1)
o3.order_lines.append(orderline2)

session.add_all([o3])

session.commit()

print(c1.orders, o1.customer, c1.orders[0].order_lines, c1.orders[1].order_lines)
for ol in c1.orders[0].order_lines:
    print(ol.id, ol.item, ol.quantity)

print('-------')

for ol in c1.orders[1].order_lines:
    print(ol.id, ol.item, ol.quantity)
    
'''


# Query
'''
re = session.query(Customer).all()
for i in re:
    print(i.last_name)
'''

# Count()
'''
re = session.query(Customer).count()  
print(re)
re = session.query(Item).count()  
print(re)
re = session.query(Order).count()  
print(re)
'''

# get()
'''
re = session.query(Customer).get(1) 
print(re)
re = session.query(Item).get(1)   
print(re)
re = session.query(Order).get(100)   
print(re)
'''

# filter()
'''
re = session.query(Customer).filter(Customer.first_name == 'John').all()
for i in re:
    print(i.first_name, i.last_name)
'''
'''
re = session.query(Customer).filter(Customer.id <= 500, Customer.town == "Norfolk").all()
for i in re:
    print(i.first_name, i.last_name)
'''
'''
re = session.query(Customer).filter(or_(
    Customer.town == 'Peterbrugh',
    Customer.town == 'Norfolk'
)).all()
for i in re:
    print(i.first_name, i.last_name)
'''
'''
re = session.query(Customer).filter(and_(
    Customer.first_name == 'John',
    Customer.town == 'Norfolk'
)).all()
for i in re:
    print(i.first_name, i.last_name)
'''
'''
re = session.query(Customer).filter(and_(
    Customer.first_name == 'John',
    not_(
        Customer.town == 'Peterbrugh',
    )
)).all()
for i in re:
    print(i.first_name, i.last_name)
'''
'''
re = session.query(Customer).filter(Order.date_shipped == None).all()
for i in re:
    print(i.first_name, i.last_name)

re = session.query(Customer).filter(Order.date_shipped != None).all()
for i in re:
    print(i.first_name, i.last_name)
'''
'''
re = session.query(Customer).filter(Customer.first_name.in_(['Toby', 'Sarah'])).all()
for i in re:
    print(i.first_name, i.last_name)


re = session.query(Customer).filter(Customer.first_name.notin_(['Toby', 'Sarah'])).all()
for i in re:
    print(i.first_name, i.last_name)
'''

'''
re = session.query(Item).filter(Item.cost_price.between(10, 50)).all()
for i in re:
    print(i.name)

re = session.query(Item).filter(not_(Item.cost_price.between(10, 50))).all()
for i in re:
    print(i.name)
'''
'''
re = session.query(Item).filter(Item.name.like("%r")).all()
for i in re:
    print(i.name)
'''
'''
re = session.query(Item).filter(Item.name.ilike("%r")).all()
for i in re:
    print(i.name)
'''
'''
re = session.query(Item).filter(not_(Item.name.ilike("%r"))).all()
for i in re:
    print(i.name)
'''
'''
re = session.query(Customer).limit(2).all()
for i in re:
    print(i.first_name, i.last_name)

re = session.query(Customer).filter(Customer.address.ilike("%avenue")).limit(2).all()
for i in re:
    print(i.first_name, i.last_name)
'''
'''
re = session.query(Customer).limit(2).all()
for i in re:
    print(i.first_name, i.last_name)
print('----------    ')
re = session.query(Customer).limit(2).offset(17).all()
for i in re:
    print(i.first_name, i.last_name)
'''
'''
re = session.query(Item).filter(Item.name.ilike("wa%")).all()
for i in re:
    print(i.name)
print('----------    ')
re = session.query(Item).filter(Item.name.ilike("wa%")).order_by(Item.cost_price).all()
for i in re:
    print(i.name)
'''
'''
re = session.query(Customer).join(Order).all()
for i in re:
    print(i.first_name, i.last_name )
'''
'''
re = session.query(
    Customer.first_name,
    Order.id,
).outerjoin(Order).all()
for i in re:
    print(i.first_name, i.id )
'''
'''
re = session.query(
    Customer.first_name,
    Order.id,
).outerjoin(Order, full=True).all()
for i in re:
    print(i.first_name, i.id)
# Error:   sqlalchemy.exc.OperationalError: (sqlite3.OperationalError) RIGHT and FULL OUTER JOINs are not currently supported
# [SQL: SELECT customers.first_name AS customers_first_name, orders.id AS orders_id 
# FROM customers FULL OUTER JOIN orders ON customers.id = orders.customer_id]
# (Background on this error at: http://sqlalche.me/e/e3q8)  
'''
'''
re = session.query(func.count(Customer.id)).join(Order).filter(
    Customer.first_name == 'Toby'
).group_by(Customer.id).scalar()

print(re)
'''

'''
re = session.query(
    func.count("*").label('town_count'),
    Customer.town
).group_by(Customer.town).having(func.count("*") > 2).all()

for i in re:
    print(i.town, i.town_count)
'''

# Dealing with Duplicates
'''
re = session.query(Customer.town).filter(Customer.id < 10).all()
for i in re:
    print(i.town)
print('----------------')
re = session.query(Customer.town).filter(Customer.id < 10).distinct().all()
for i in re:
    print(i.town)
print('----------------')
re = session.query(
    func.count(distinct(Customer.town)),
    func.count(Customer.town)
).all()
for i in re:
    print(i)
print('----------------')
'''

# Casting
'''
re = session.query(
    cast(func.pi(), Integer),
    cast(func.pi(), Numeric(10, 2)),
    cast(datetime.strptime("2010-12-01", '%Y-%m-%d'), DateTime),
    # cast("2010-12-01", Date),
).all()

print(re)

# Error:
# sqlalchemy.exc.OperationalError: (sqlite3.OperationalError) no such function: pi
# [SQL: SELECT CAST(pi() AS INTEGER) AS anon_1, CAST(pi() AS NUMERIC(10, 2)) AS anon_2, CAST(? AS DATETIME) AS anon_3]
# [parameters: ('2010-12-01 00:00:00.000000',)]
'''

# Unions
'''
s1 = session.query(Item.id, Item.name).filter(Item.name.like("Wa%"))

for i in s1:
    print(i)
print('-------------')
s2 = session.query(Item.id, Item.name).filter(Item.name.like("%e%"))
for i in s2:
    print(i)
print('-------------')

s3 = s1.union(s2).all()
for i in s3:
    print(i)
'''

# deleting
'''
re = session.query(Item).filter(Item.name == 'Monitor')
for i in re:
    print(i.id, i.name)
    session.delete(i)
session.commit()
'''

# Updating Data
'''
i = session.query(Item).get(8)
i.selling_price = 25.91
session.add(i)
session.commit()
'''

# Raw Queries

re = session.query(Customer).filter(text("first_name = 'John'")).all()
for i in re:
    print(i.id, i.last_name)
re = session.query(Customer).filter(text("town like 'Nor%'")).all()
for i in re:
    print(i.id, i.last_name)
re = session.query(Customer).filter(text("town like 'Nor%'")).order_by(text("first_name, id desc")).all()
for i in re:
    print(i.id, i.last_name)