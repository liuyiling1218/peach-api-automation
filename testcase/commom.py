"""
@author:Liuyiling
@description:
@date:2023/10/26 16:14

"""
from graphql_client.client import Client
import requests


def login_request():
    url = 'https://auth-test.hjfruit.cn'
    headers = {'Host': 'auth-test.hjfruit.cn', 'content-type': 'application/json', 'Accept-Encoding': 'gzip',
               'User-Agent': 'okhttp/4.9.2', 'Connection': 'Keep-Alive'}
    requests.post(url=url + '/auth/sendCodeMsg?', json={"phone": "15803605089"}, headers=headers)
    res = requests.post(url=url + '/auth/loginByMsgCodeOnApp?',
                        json={"phone": "15803605089", "code": "666666", "requestId": "1"}, headers=headers)
    json_obj = res.json()
    token = json_obj['data']
    headers['authorization'] = token
    requests.post(url=url + '/auth/chooseTenant?', json={"tenantId": 1}, headers=headers)
    requests.post(url=url + '/auth/chooseOrg?', json={"orgId": 162}, headers=headers)
    return token


def common(func):
    def graphql_request():
        token = login_request()
        client = Client(url='https://peach-test.hjfruit.cn/graphql', headers={"Authorization": token})
        func(client)

    return graphql_request

# def common(func):
#     def x():
#         client = Client(url='https://peach-test.hjfruit.cn/graphql', headers={"Authorization": "kktJLMPhAtduLA0Jl5dXqull5LtuDGmM9saoDkA++meNb57xtuefKGL7MDgtnjEglF6bh+sYYEy+Wc7VeUn9+ub00oIZwQWJD3Q8XCPBbMQBemUZdNWAiylfLztn9pdh"})
#         func(client)
#     return x
#
# @common
# def greet(client):
#     print('hello world')
# client = greet()
