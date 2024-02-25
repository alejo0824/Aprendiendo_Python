import os
from sendgrid.helpers.mail import Mail
# API de cliente para enviar correos electrónicos utilizando SendGrid.
from sendgrid import SendGridAPIClient

email = os.environ.get("SEDNGRID_EMAIL")

mensaje = Mail(
    from_email=email,
    to_emails='alejo082495@gmail.com',
    subject="Correo de prueba",
    html_content="Curso de <b>Python</p>"
)
try:
    apikey = os.environ.get("SENDGRID_API_KEY")
    sg = SendGridAPIClient(apikey)
    respuesta = sg.send(mensaje)
    print(
        respuesta.status_code,
        respuesta.body,
        respuesta.headers
    )

except Exception as e:
    print(e)
