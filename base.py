from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base


engine = create_engine('sqlite:///F:\\pythonProject\\sqlalchemy.sqlite', echo=True)

base = declarative_base()


class Transakcje(base):
    __tablename__ = 'transakcje'

    transakcja_id = Column(Integer, primary_key=True)
    data = Column(String)
    przedmiot_id = Column(Integer)
    cena = Column(Integer)

    def __init__(self, transakcja_id, data, przedmiot_id, cena):
        self.transakcja_id = transakcja_id
        self.data = data
        self.przedmiot_id = przedmiot_id
        self.cena = cena

base.metadata.create_all(engine)