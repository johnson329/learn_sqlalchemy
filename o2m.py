from sqlalchemy import Column, Integer, ForeignKey, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker

Base = declarative_base()


class Parent(Base):
    __tablename__ = 'parent'
    id = Column(Integer, primary_key=True)
    children = relationship("Child", backref="parent")


class Child(Base):
    __tablename__ = 'child'
    id = Column(Integer, primary_key=True)
    parent_id = Column(Integer, ForeignKey('parent.id'))


# 为了不使用数据库外键，手动创建对应表结构

engine = create_engine('mysql+pymysql://username:password@localhost:3306/test')
# 创建DBSession类型:
DBSession = sessionmaker(bind=engine)

# 创建session对象:
session = DBSession()
# 创建parent
new_parent1 = Parent(id=1)
new_parent2 = Parent(id=2)
session.add(new_parent1)
session.add(new_parent2)
session.commit()

# 创建children，指定parent为p1

p1 = session.query(Parent).filter_by(id=1).first()
c1 = Child(id=1)
c1.parent = p1
session.add(c1)

# 改,指定parent为p2
p2 = session.query(Parent).filter_by(id=2).first()
c1 = session.query(Child).filter_by(id=1).first()
c1.parent = p2
session.add(c1)

session.commit()

# 断点查看数据库
# 删，删除被引用的parent，p2,但是不影响child,c1的parent_id仍然是2,只不过2这个parent不存在了，相当于 do noting

session.query(Parent).filter_by(id=2).delete()
session.commit()

session.close()
