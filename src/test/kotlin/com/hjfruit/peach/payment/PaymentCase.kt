package com.hjfruit.peach.payment

import com.hjfruit.peach.GraphqlBaseTest
import com.hjfruit.peach.generated.CalculatorPayment
import com.hjfruit.peach.generated.inputs.CalculatorPaymentInput
import com.hjfruit.peach.generated.inputs.Page
import com.ibm.icu.util.IslamicCalendar.CalculationType
import kotlinx.coroutines.runBlocking
import org.junit.Ignore
import org.junit.Test

class PaymentCase:GraphqlBaseTest() {

    @Test
    fun payment_test_ok() {
        runBlocking {
            val calculatorPayment = CalculatorPayment(CalculatorPayment.Variables(CalculatorPaymentInput()))
            print(client.execute(calculatorPayment))



        }
    }

}