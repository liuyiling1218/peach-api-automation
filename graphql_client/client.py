# Generated by ariadne-codegen on 2023-10-30 16:43
# Source: graphql/orange_queries.graphql

from typing import Dict, Optional, Union

from .base_client import BaseClient
from .base_model import UNSET, UnsetType
from .input_types import PeachOrderCreateInput
from .peach_order_create import PeachOrderCreate


def gql(q: str) -> str:
    return q


class Client(BaseClient):
    def peach_order_create(
        self, input: Union[Optional[PeachOrderCreateInput], UnsetType] = UNSET
    ) -> PeachOrderCreate:
        query = gql(
            """
            mutation peachOrderCreate($input: PeachOrderCreateInput) {
              peachOrderCreate(input: $input) {
                orderCancelHour
                orderCode
                orderId
                payableAmount
                paymentCode
              }
            }
            """
        )
        variables: Dict[str, object] = {"input": input}
        response = self.execute(query=query, variables=variables)
        data = self.get_data(response)
        return PeachOrderCreate.model_validate(data)
