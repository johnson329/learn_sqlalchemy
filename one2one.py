from sqlalchemy import create_engine, Column, String, Integer, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship, backref

Base = declarative_base()

# 为了不使用数据库外键，手动创建对应表结构

engine = create_engine('mysql+pymysql://test:test123456@localhost:3306/test')
# 创建DBSession类型:
DBSession = sessionmaker(bind=engine)

# 创建session对象:
session = DBSession()


class Husband(Base):
    __tablename__ = 'husband'
    id = Column(Integer, primary_key=True)
    name = Column(String(20))


class Wife(Base):
    __tablename__ = 'wife'
    id = Column(Integer, primary_key=True)
    name = Column(String(20))
    husband_id = Column(Integer(), ForeignKey('husband.id'))
    husband = relationship("Husband", backref=backref("wife", uselist=False))


class License(Base):
    __tablename__ = 'li'
    id = Column(Integer, primary_key=True)
    name = Column(String(20))
    husband_id = Column(Integer(), ForeignKey('husband.id'))
    husband = relationship("Husband", backref=backref("li", uselist=False))


# w1 = Wife(name='w2')
# w1 = Wife(name='w1')
# h1 = Husband(name='h', wife=w1)
# session.add(h1)

# h1 = session.query(Husband).filter_by(name='h')
w1 = session.query(Wife).filter_by(name='w').first()
l1 = session.query(License).filter_by(name='l1').first()
h1 = w1.husband

# 可以通过mysql日志发现，sql分执行，而不是，表连接执行

# 在不使用物理外键的情况下，自行进行级联删除或者级联更新，或者不删除，不更新，减少数据库死锁的可能新

session.commit()
session.close()
