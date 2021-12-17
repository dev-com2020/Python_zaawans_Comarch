from sqlalchemy import *

db = create_engine('sqlite:///przyklad.db')

db.echo = False

metadata = MetaData(db)

users = Table('users', metadata,
              Column('user_id', Integer, primary_key=True),
              Column('name', String(255)),
              Column('job', Integer),
              Column('pas', String(255)),
              )
# users.create()

# insert = users.insert()
#
# insert.execute(name='Michal', job='Bezrobotny', pas='sekretne')
#
# insert.execute({'name': 'Jan', 'job': 'Handlowiec', 'pass': 'tajne'},
#                {'name': 'Kuba', 'job': 'Wozny'},
#                {'name': 'Ola', 'job': 'Handlowiec'})  # Wkładamy dane

select = users.select()
result = select.execute()
wszystko = result.fetchall()




#print('Praca:', row['user_id'])
# print('Haslo:', row['pas'])
#
# for row in wszystko:
#     print(row.name, 'pracuje jako', row.job)
