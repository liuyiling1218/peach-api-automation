package com.hjfruit.peach

import com.expediagroup.graphql.client.spring.GraphQLWebClient
import io.netty.channel.ChannelOption
import org.springframework.http.client.reactive.ClientHttpConnector
import org.springframework.http.client.reactive.ReactorClientHttpConnector
import org.springframework.web.reactive.function.client.WebClient
import reactor.netty.http.client.HttpClient
import java.time.Duration

open class GraphqlBaseTest {
     val httpClient: HttpClient = HttpClient.create()
        .option(ChannelOption.CONNECT_TIMEOUT_MILLIS, 10_000)
        .responseTimeout(Duration.ofMillis(10_000))
    val connector: ClientHttpConnector = ReactorClientHttpConnector(httpClient.wiretap(true))
    val webClientBuilder = WebClient.builder()
        .clientConnector(connector)
        .defaultHeader(
            "Authorization",
            "kktJLMPhAtduLA0Jl5dXqoT74nxpPLJDoYw89mMaz6ktV70WVGv236G2J5nHhvboPKUPRyjNFOnbc6QSsUt7mw=="
        )

    open val client = GraphQLWebClient(
        url = "http://192.168.10.233:10002/graphql",
        builder = webClientBuilder
    )

}