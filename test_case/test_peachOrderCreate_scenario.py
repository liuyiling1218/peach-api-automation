"""
@author:Liuyiling
@description:
@date:2023/11/1 14:45

"""
from Action.peachOrderCreate_Action import PeachOrderCreate_Action


# 开单-收银
def test_createOrder_payment_scenario(oss_client):
    orderid = PeachOrderCreate_Action.peachOrderCreate(oss_client)
    PeachOrderCreate_Action.peachOrderPayment(oss_client, orderid)
