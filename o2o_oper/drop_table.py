from o2o_oper.declarative_model import Base, engine

if __name__ == '__main__':
    Base.metadata.drop_all(engine)
