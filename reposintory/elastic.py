from elasticsearch import Elasticsearch

from reposintory.sql import users, permission, coupone
from reposintory import mysql1

es = Elasticsearch(['127.0.0.1'],
                   port=9200)
user_doc = {
    "id": 0,
    'name': 'username',
    'pass': 'password'

}
permission_doc = {
    "id ": 0,
    'user_id': 0,
    'permission_id': 0
}
user_coupone_doc = {
    "id": 0,
    'id_user': 0,
    'coupone_name': "coupone"
}
coupone_doc = {
    "id": 0,
    "coupon_name": "value"

}

database_object = mysql1.Database()
es.index(index="user_coupone-index", id=1, body=user_coupone_doc)


def index_user():
    user = {

        "id": 0,

        "name": "",
        "password": "value"
    }
    s = (database_object.execute_1(users.q1_user))
    for i in s:
        user['id'] = i[0]
        user['name'] = i[1]
        user['password'] = i[2]
        es.index(index="user-index", id=1, body=user)
        es.get(index="user-index", id=1)
        # print(user_res['_source'])


def index_permission():
    permissions = {
        "id": 0,
        "user_id": 0,
        "permission_id": 0
    }
    s = (database_object.execute_1(permission.q1_user_permission))
    for i in s:
        permissions['id'] = i[0]
        permissions['user_id'] = i[1]
        permissions['permission_id'] = i[2]
        es.index(index="permission-index", id=1, body=permissions)

        es.get(index='permission-index', id=1)


def index_coupon():
    coupon = {
        "id": 0,
        "coupon_name": "value"
    }
    s = (database_object.execute_1(coupone.q4_coupone))
    for i in s:
        coupon['id'] = i[0]
        coupon['coupon_name'] = i[1]

        es.index(index="coupone-index", id=1, body=coupon)

        es.get(index='coupone-index', id=1)


def index_user_coupon():
    user_coupon = {
        "id": 0,
        'id_user': 0,
        'coupone_name': "coupone"
    }
    s = (database_object.execute_1(coupone.q3_user_coupone))

    for i in s:
        user_coupon['id'] = i[0]
        user_coupon['id_user'] = i[1]
        user_coupon['coupon_name'] = i[2]

        es.index(index="user_coupone-index", id=1, body=user_coupon)

        es.get(index='user_coupone-index', id=1)
index_user_coupon()