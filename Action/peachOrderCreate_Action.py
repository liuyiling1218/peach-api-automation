"""
@author:Liuyiling
@description:
@date:2023/10/24 15:15
"""
from graphql_client.input_types import *
from graphql_client.enums import OrderSchema, PeachOrderType, PaymentType


# 批发开单
class PeachOrderCreate_Action:
    @staticmethod
    def peachOrderCreate(client):
        peachOrderCommodityCreateInput = PeachOrderCommodityCreateInput.model_construct()
        peachOrderCommodityCreateInput.quantity = 0.01
        peachOrderCommodityCreateInput.stock_id = '1007564658771894272'
        peachOrderCommodityCreateInput.quantity_unit_type = 1
        peachOrderCommodityCreateInput.subtotal = 1
        peachOrderCommodityCreateInput.unit_price = 100
        foo = [peachOrderCommodityCreateInput]
        input = PeachOrderCreateInput.model_construct()
        input.commodity_list = foo
        input.contact_id = 450
        input.customer_id = 2654
        input.order_schema = OrderSchema.SCHEMA_SKU
        input.order_type = PeachOrderType.WHOLESALE
        input.payable_amount = 1
        input.pre_payment_type = [PaymentType.CASH]
        input.total_amount = 1
        input.remark = '自动化测试脚本数据'
        res = client.peach_order_create(input)
        return res.peach_order_create.order_id
#订单收银
    @staticmethod
    def peachOrderPayment(client,orderid):
        paymentDetail_input = OrderPaymentDetailListInput.model_construct()
        paymentDetail_input.payment_type = PaymentType.CASH
        paymentDetail_input.paid_amount = 1
        foo = [paymentDetail_input]
        input = PeachOrderPaymentInput.model_construct()
        input.order_id =orderid
        input.cash_remark = '自动化测试脚本数据'
        input.order_payments_details = foo
        client.peach_order_payment(input)

