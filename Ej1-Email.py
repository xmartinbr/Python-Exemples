import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

msg = MIMEMultipart()

message = "Thank you"

msg['Subject'] = 'Email Test'
msg['From'] = 'desdemicorreo@gmail.com'
msg['To'] = 'haciaotrocorreo@gmail.com'
passw = 'xxxxxxxx'

msg.attach(MIMEText(message, 'plain'))

#Dirección del servidor de correo desde donde queremos enviar el correo
mailServer = smtplib.SMTP('smtp.gmail.com',587)
mailServer.ehlo()
mailServer.starttls()
mailServer.ehlo()
#Nos conectados al servidor de correo desde donde queremos
#enviar el correo con nuestro usuario y password
mailServer.login(msg['From'],passw)
#Enviamos el correo
mailServer.sendmail(msg['From'],msg['To'],msg.as_string())
mailServer.close()

#Si todo se ha configurado correctamente el correo será enviado al usuario
#destino, pero es muy probable que cuando intentamos establecer conexión
#con nuestro servidor SMTP de Google este no nos permita conectarnos
#y nos deniegue el acceso
#Que hacemos para poder enviar el correo desde nuestro servidor de Google?
#Debemos ir a la página de configuración de Google
# "https://www.google.com/settings/security/lesssecureapps"
#y una vez dentro activaremos la opción "Allow less secure apps" o en
#castellano "Permitir el acceso de aplicaciones poco seguras"
#Una vez activada la opción ya podremos vovler a ejecutar el código y esta
#vez ya se podrá enviar el correro
#Una vez finalicen las pruebas es recomendable volver a desactivar la opción
#ya que sino si alguien nos hacleara nuestra cuenta podría utilizar
#nuestra dirección de correo para enviar infinidad de emails.
#Link interesante
# https://code.tutsplus.com/es/tutorials/sending-emails-in-python-with-smtp--cms-29975

    
