from elasticsearch import Elasticsearch

from reposintory.sql.users import q1_user
from reposintory import mysql1

es = Elasticsearch(['127.0.0.1'],
                   port=9200)
user_doc = {
    "id": 0,
    'name': 'username',
    'pass': 'password'

}
permission_doc = {
    'user_id': 0,
    'permission_id': 0
}
coupone_doc = {
    'id_user': 0,
    'coupone_name': "coupone"
}
"""
user_res = es.index(index="user-index", id=3, body=coupone_doc)
print(user_res['result'])

user_res = es.get(index="user-index", id=3)
print(user_res['_source'])

permis_res = es.index(index="per-index", id=1, body=permission_doc)
print(permis_res['result'])
permis_res = es.get(index="per-index", id=1)
print(permis_res['_source'])

"""
database_object = mysql1.Database()


def index_user():
    z = {

        "id": 0,

        "name": "",
        "password": "value"
    }
    s = (database_object.execute_1(q1_user))
    for i in s:

        z['id'] = i[0]

        z['name'] = i[1]
        z['password'] = i[2]
        #`print(z)
        user_docs = es.index(index="user-index", id=1, body=z)
        user_res = es.get(index="user-index", id=1)
        print(user_res['_source'])
        #add elas





# user_docs = es.index(index="user-index", id=1, body=s)


index_user()
# user_res = es.get(index="user-index", id=1)
# print(user_res['_source'])
