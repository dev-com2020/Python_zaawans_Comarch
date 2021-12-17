import base
from sqlalchemy.orm import sessionmaker

Session = sessionmaker(bind=base.engine)
s = Session()

for t in range(10):
    tr = base.Transakcje(t, '2021/12/15', 12, 130)
    s.add(tr)

s.commit()
