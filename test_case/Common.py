"""
@author:Liuyiling
@description:
@date:2023/10/31 14:05

"""
from graphql_client.client import Client
from test_case.Autheration import autheration
def common(func):
    def graphql_request():
        client = Client(url='https://peach-test.hjfruit.cn/graphql', headers={"Authorization": autheration.token})
        func(client)
    return graphql_request