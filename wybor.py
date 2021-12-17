import base
from sqlalchemy.orm import sessionmaker

Session = sessionmaker(bind=base.engine)
session = Session()


for s in session.query(base.Transakcje).all():
    print(s.transakcja_id)

for s in session.query(base.Transakcje).filter(base.Transakcje.transakcja_id>5):
    print(s.transakcja_id)