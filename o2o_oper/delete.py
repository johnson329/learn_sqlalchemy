from o2o_oper.declarative_model import Wife, Husband
from o2o_oper.declarative_model import session


def delete():
    # session.query(Husband).filter(Husband.name == "周杰伦").delete()
    session.query(Wife).filter(Wife.name == "昆凌").delete()
    session.commit()
    session.close()


if __name__ == '__main__':
    delete()
