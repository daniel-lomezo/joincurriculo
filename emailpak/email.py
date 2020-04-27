import smtplib
from email import encoders
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
import os



class mail(object):

    def enviaemail(self, titulo, corpomensagem, destinatarios):
        try:
            port = 465
            


            # conexão com os servidores do google
            smtp_ssl_host = 'smtp.gmail.com'
            smtp_ssl_port = 465
            emaildeenvio = 'daniel.ubletech@gmail.com'

            username = 'daniel.lomezohdm@gmail.com'
            password = 'daniellomezo008090'



            # username ou email para logar no servidor
          
            
            
            Corpomensagem = destinatarios and corpomensagem

            message = MIMEMultipart()
            message.attach(MIMEText(Corpomensagem, 'plain'))
            message['subject'] = titulo
            message['from'] = username
            message['to'] = ', '.join(emaildeenvio)
            #config = os.path.join(os.path.dirname(os.path.abspath(__file__)), caminho)
            #attachment = open(config, "rb")

            #part = MIMEBase('application', 'octet-stream')
            #part.set_payload((attachment).read())
            #encoders.encode_base64(part)
            #part.add_header('Content-Disposition', "attachment; filename={}".format(caminho.replace('logs/', '')))
            #print(caminho)
            #message.attach(part)

            # conectaremos de forma segura usando SSL
            server = smtplib.SMTP_SSL(smtp_ssl_host, smtp_ssl_port)


            # para interagir com um servidor externo precisaremos
            # fazer login nele
            server.login(username, password)
            server.sendmail(emaildeenvio, emaildeenvio, message.as_string())
            server.quit()
        except:
            print('Erro ao enviar')