# Importando Pandas e OpenAi
import pandas as pd
import openai

# Adicionando a API KEY
openai.api_key = 'sk-**********************************dg'

# Criando dataframe para armazenar a tabela
df = pd.read_excel("Consultores.xlsx")

# Criando variavel 'consultant' com os nomes dos consultores
for consultant in df["Consultor"]:
    # Gerando um texto personalizado com chat completion.
    text = openai.Completion.create(
        engine="davinci",
        prompt="Olá [consultant],\n\nAqui está um resumo dos seus pedidos:\n\n",
        temperature=0.7,
        max_tokens=100,
        top_p=1.0,
        frequency_penalty=0.0,
        presence_penalty=0.0,
    )

def send_email(text, email):
    # Importar a biblioteca smtplib.
    import smtplib

    # Criar um objeto SMTP.
    smtp = smtplib.SMTP("smtp.gmail.com", 587)

    # Habilitar autenticação.
    smtp.ehlo()
    smtp.starttls()
    smtp.login("gm*******@gmail.com", "***********")

    # Enviar o e-mail.
    smtp.sendmail("gm*******@gmail.com", email, text)

    # Fechar a conexão com o servidor SMTP.
    smtp.quit()

send_email(text, df.loc[df["Consultor"] == consultant, "Email"])

# Exemplo de como ficará um e-mail:

#Olá Edson,

#Aqui está um resumo dos seus pedidos:

#* Pedido 98563: Bombril - Ok
#* Pedido 54785: Volkswagen - Em atraso
#* Pedido 85016: Panobianco - Em atraso
#* Pedido 2159: Attualita - Em atraso
#* Pedido 14693: Blommindales - Ok
#* Pedido 55630: Microsoft - Ok
#* Pedido 458896: Netflix Brasil - Em atraso

#Atenciosamente,

#OpenAI