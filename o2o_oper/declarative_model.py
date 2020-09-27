from sqlalchemy import create_engine, ForeignKey

# echo=True会用python的logging库打印出日志 执行的sql
# 返回Engine对象
from sqlalchemy.orm import relationship

engine = create_engine('sqlite:///o2o.db', echo=True)
from sqlalchemy.ext.declarative import declarative_base  # noqa

# 定义映射
Base = declarative_base()
from sqlalchemy import Column, Integer, String  # noqa


# 一夫一妻制
class Husband(Base):
    __tablename__ = "husband"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    # 1.ForeignKey的参数是__tablename__.id
    # 2.外键的作用就是当引用对象，这里是wife，被删除时或者被修改时，本对象如何变化
    # 不使用数据库外键（注意数据库外键和orm的ForeignKey不是必然一致，我可以model定义好外键，
    # 但是数据库手动创建，我就是不用数据库外键）
    # 3.如果用数据库外键，ondelete,onupdate定义了当被引用对象被删除或者被修改时，本对象如何变化
    # RESTRICT表示不准删除被引用对象，NO ACTION：在MySQL中，同RESTRICT，sqlite中是什么也不做
    # CASCADE表示被引用对象删除了，本对象也删除，也就是wife没了，husband也没了
    # SET NULL 表示被引用对象没了，外键，此处也就是wife_id被设置为null
    # sqlalchemy 默认就是no action
    # sqlite 中如果ForeignKey("wife.id"，ondelete="RESTRICT")在创建表的时候会有
    # 但是，数据库不会自动帮你删除，不起作用
    wife_id = Column(Integer, ForeignKey("wife.id"), )
    # 参数是类名,一对一的关系，两边都写relationship，可以获得ide的提示
    wife = relationship("Wife", back_populates="husband", uselist=False)


class Wife(Base):
    __tablename__ = "wife"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    # 由于wife_id也就是外键在Husband类，所以为了和一对多关系区分，也就是从wife获取husband
    # 不能是一个集合类型也就是collection，那么 uselist=False
    husband = relationship("Husband", back_populates="wife", uselist=False, cascade="all, delete")


from sqlalchemy.orm import sessionmaker

Session = sessionmaker(bind=engine)
session = Session()
if __name__ == '__main__':
    # 创建表
    Base.metadata.create_all(engine)
