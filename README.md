# Desafio2_ETL

 Desafio criando um ETL com Python.

# A idéia

A partir de uma planilha alimentada semanalmente pelo setor financeiro de uma empresa, listando os status dos pedidos gerados
pelos consultores, a idéia é colher esses dados, relacionar e enviar para a IA generativa para que ela crie um lembrete
personalizado informando a cada consultor os status de seus pedidos, informando quais estão em dia ou em atraso com seus pagamentos.

O código então carrega esse lembrete personalizado dentro do corpo de um e-mail e adiciona o destinatario de acordo com o email relacionado ao consultor que está dentro da propria planilha e envia.
