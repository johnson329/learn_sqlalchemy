from sqlalchemy import Column, Integer, ForeignKey, Table, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker

Base = declarative_base()
engine = create_engine('mysql+pymysql://test:test123456@localhost:3306/test')
Session = sessionmaker(bind=engine)
ss = Session()
Base = declarative_base()

association_table = Table('association', Base.metadata,
                          Column('left_id', Integer, ForeignKey('left.id',ondelete="CASCADE")),
                          Column('right_id', Integer, ForeignKey('right.id',ondelete="CASCADE"))
                          )


class Left(Base):
    __tablename__ = 'left'
    id = Column(Integer, primary_key=True)
    right = relationship("Right",
                         secondary=association_table, backref="left",cascade="all, delete",passive_deletes=True)


class Right(Base):
    __tablename__ = 'right'
    id = Column(Integer, primary_key=True)

l1_q = ss.query(Left).filter_by(id=1)
# 增
l1 = Left(id=1)
r1 = Right(id=1)
r2 = Right(id=2)
r3 = Right(id=3)

l1.right = [r1, r2]
# l1.right.append(r1)
# l1.right.append(r2)

# ss.add_all([l1, r1,r2])
# 等同于下面这句
ss.add(r1)
ss.commit()

# 查
l1_q = ss.query(Left).filter_by(id=1)
# r1 = ss.query(Right).filter_by(id=1)

# 改
l1 = l1_q.first()
l1.right = [r1, r3]
ss.add(l1)
ss.commit()
# 删除

l1_q.first().right = []
l1_q.delete()

ss.commit()

# l1 = Left(id=1)
#
# ss.add(l1)
# ss.commit()
#
# a = ss.query(Left).filter_by(id=1).first()

ss.close()
