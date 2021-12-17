import couchdb

user = "admin"
password = "admin"
server = couchdb.Server("http://%s:%s@localhost:5984/" % (user, password))

dbname = "test01"
