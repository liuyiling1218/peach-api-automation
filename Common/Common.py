"""
@author:Liuyiling
@description:
@date:2023/10/31 14:05

"""
from graphql_client.client import Client
from Common.Autheration import autheration
def common(func):
    def graphql_request(parameter=''):
        client = Client(url='https://peach-test.hjfruit.cn/graphql', headers={"Authorization": autheration.token})
        res=func(client,parameter)
        return res
    return graphql_request