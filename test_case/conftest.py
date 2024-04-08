"""
@author:Liuyiling
@description:
@date:2023/10/31 9:33

"""
import requests
import pytest
from Common.Autheration import autheration
from Common.ClientProxy import ClientProxy
from graphql_client.client import Client


@pytest.fixture(scope='session', autouse=True)
def get_login_token():
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
    autheration.token = token


@pytest.fixture()
def oss_client():
    original_client = Client(url='https://peach-test.hjfruit.cn/graphql', headers={
        "Authorization": autheration.token})

    return ClientProxy(original_client)
