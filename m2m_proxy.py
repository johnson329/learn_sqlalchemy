from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy import create_engine
from sqlalchemy.ext.associationproxy import association_proxy
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, backref

engine = create_engine('mysql+pymysql://test:test123456@localhost:3306/test')
from sqlalchemy.orm import sessionmaker

Session = sessionmaker(bind=engine)
ss = Session()
Base = declarative_base()


class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    name = Column(String(64))

    # association proxy of "user_keywords" collection
    # to "keyword" attribute
    keywords = association_proxy('user_keywords', 'keyword')  # 中间表和Many2Many表的名字


class Keyword(Base):
    __tablename__ = 'keyword'
    id = Column(Integer, primary_key=True)
    keyword = Column('keyword', String(64))  # 要加跟表名一样的标签

    def __repr__(self):
        return 'Keyword(%s)' % repr(self.keyword)


class UserKeyword(Base):
    __tablename__ = 'user_keyword'
    user_id = Column(Integer, ForeignKey('user.id'), primary_key=True)
    keyword_id = Column(Integer, ForeignKey('keyword.id'), primary_key=True)
    special_key = Column(String(50))

    # bidirectional attribute/collection of "user"/"user_keywords"
    user = relationship(User,
                        backref=backref("user_keywords",
                                        cascade="all, delete-orphan")
                        )

    # reference to the "Keyword" object
    keyword = relationship("Keyword")

    def __repr__(self):
        return f'User({self.user_id})-Keyword({self.keyword_id})_self.special_key '


u1 = User(id=1, name='johnson')
k1 = Keyword(id=1, keyword='shuai')
u1.keywords=k1
ss.add(u1)
ss.commit()
ss.close()
