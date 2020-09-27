from o2o_oper.declarative_model import Wife, Husband
from o2o_oper.declarative_model import session


def q():
    wife_obj = session.query(Wife).filter_by(name="昆凌").first()

    # 这地方有人可能要转换一下思想
    # wife表中没有husband的信息，我怎么能wife_obj.husband呢？我应该拿着wife_id去husband表查询啊
    # 实际上执行wife_obj.husband 就是去husband表查询
    # orm就是把表之间的关系转换成对象之间的关系，所以我们不必像写sql那样去思考
    if wife_obj:
        husband_obj = wife_obj.husband
        print(husband_obj.name)


if __name__ == '__main__':
    # 执行中可以在console中看到sql语句
    q()
