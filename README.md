# Desafio2_ETL

 Desafio criando um ETL com Python.

# A idéia

A partir de uma planilha alimentada semanalmente pelo setor financeiro de uma empresa, listando os status dos pedidos gerados
pelos consultores, a idéia é colher esses dados, relacionar e enviar para a IA generativa para que ela crie um lembrete
personalizado informando a cada consultor os status de seus pedidos, informando quais estão em dia ou em atraso com seus pagamentos.

O código então carrega esse lembrete personalizado dentro do corpo de um e-mail e adiciona o destinatario de acordo com o email relacionado ao consultor que está dentro da propria planilha e envia.

# O Resultado
Este é um exemplo do e-mail que é gerado e enviado ao consultor:

"Olá Edson,

Aqui está um resumo dos seus pedidos:

* Pedido 98563: Bombril - Ok
* Pedido 54785: Volkswagen - Em atraso
* Pedido 85016: Panobianco - Em atraso
* Pedido 2159: Attualita - Em atraso
* Pedido 14693: Blommindales - Ok
* Pedido 55630: Microsoft - Ok
* Pedido 458896: Netflix Brasil - Em atraso

Atenciosamente,

OpenAI"
