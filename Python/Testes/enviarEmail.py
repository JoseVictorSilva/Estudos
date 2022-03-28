from email import message
import smtplib, ssl
from email.message import EmailMessage

titulo = "Email Enviado Pelo Python"
txt = input("Entre com o Texto a ser enviado")
remetente = input("Entre com seu Email: ")
destinatario = input("Quem será o destinatário? ")
senha = input("Entre com sua senha: ")

message = EmailMessage()
message["From"] = remetente
message["To"] = destinatario
message["Subject"] = titulo

message.set_content(txt)

context = ssl.create_default_context()
print("Enviando email")
with smtplib.SMTP_SSL("smtp.gmail.com",465,context = context) as server:
    server.login(remetente,senha)
    server.sendmail(remetente,destinatario,message.as_string())
print("Sucesso")