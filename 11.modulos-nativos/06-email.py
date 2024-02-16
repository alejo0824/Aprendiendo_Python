from email.mime.multipart import MIMEMultipart  # Multiple Internet Mail Extension
from email.mime.text import MIMEText
import smtplib

mensaje = MIMEMultipart()
mensaje["from"] = "correo.prueba.dev2024@gmail.com"
mensaje["to"] = "alejo082495@gmail.com"
mensaje["subject"] = "Esta es una prueba "
cuerpo = MIMEText("Cuerpo del mensaje")
mensaje.attach(cuerpo)

with smtplib.SMTP(host="smtp.gmail.com", port=587) as smtp:
    smtp.ehlo()  # ehlo = identificarno con SMTP
    smtp.starttls()  # Encriptación del correo

    smtp.login("correo.prueba.dev2024@gmail.com", "Holamundo123")
    smtp.send_message(mensaje)
