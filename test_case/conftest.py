"""
@author:Liuyiling
@description:
@date:2023/10/31 9:33

"""
import requests
import pytest
from test_case.Autheration import autheration
@pytest.fixture(scope='module',autouse=True)
def test_login_request():
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
    autheration.token=token