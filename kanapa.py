import os

import couchdb

user = 'admin'
password = 'admin'
couchserver = couchdb.Server("http://%s:%s@localhost:5984/" % (user, password))

# for dbname in couchserver:
#      print(dbname)

dbname = "test01"
if dbname in couchserver:
    db = couchserver[dbname]
else:
    db = couchserver.create(dbname)

# db['jankowalski'] = dict(type='Person', name='Jan Kowalski')
# db['jankowalski2'] = dict(type='Person', name='Zbigniew Kowalski')
# db['jankowalski3'] = dict(type='Person', name='Tomasz Kowalski')
map_fun = ''' function(doc){
emit([doc.type, doc.name],doc.name);
}
'''
results = db.query(map_fun)
ludzie = results[['Person']:['Person', "zzzz"]]
for person in ludzie:
    print(person.value)

# del couchserver[dbname]

# doc_id, doc_rev = db.save({'key': 'value'})
#
# docs = [{'key1': 'value1'}, {'key2': 'value2'}]
# for (success, doc_id, revision_or_exception) in db.update(docs):
#     print(success, doc_id, revision_or_exception)


# doc = db[doc_id]
# nameFile = doc['_attachments'].keys()[0]
# attachment = db.get._attachment(doc,nameFile).read()
# current_folder = os.getcwd()
# tempfile = os.path.join(current_folder,nameFile)
# f = open(tempfile,'w')
# f.write(attachment)
# f.close()

# db.get(doc_id)

# for row in db.view('_all_docs',starkey=["key2"]):
#    print(row)
#
