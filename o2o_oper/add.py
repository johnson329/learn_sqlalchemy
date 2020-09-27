from o2o_oper.declarative_model import Wife, Husband
from o2o_oper.declarative_model import session


def add():
    wife_obj = Wife(name="昆凌")
    husband_obj = Husband(name="周杰伦")
    wife_obj.husband = husband_obj
    session.add(wife_obj)
    session.commit()


if __name__ == '__main__':
    # 执行中可以在console中看到sql语句
    add()
