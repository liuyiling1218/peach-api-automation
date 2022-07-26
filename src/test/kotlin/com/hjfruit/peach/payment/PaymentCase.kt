package com.hjfruit.peach.payment

import com.example.generated.CalculatorPaymentQuery
import com.hjfruit.peach.GraphqlBaseTest
import kotlinx.coroutines.runBlocking
import org.junit.Ignore
import org.junit.Test

class PaymentCase:GraphqlBaseTest() {

    @Test
    fun payment_test_ok() {
        runBlocking {
            val me = CalculatorPaymentQuery()
            val result = client.execute(me)
            print(result)

        }
    }

}