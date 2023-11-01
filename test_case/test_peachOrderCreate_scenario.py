"""
@author:Liuyiling
@description:
@date:2023/11/1 14:45

"""
from Action.peachOrderCreate_Action import test_peachOrderCreate, test_peachOrderPayment

# 开单-收银
def test_createOrder_payment_scenario():
    order_id=test_peachOrderCreate()
    test_peachOrderPayment(order_id)



