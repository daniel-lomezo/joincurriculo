import smtplib
from email import encoders
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
import os



class mail(object):

    def enviaemail(self, titulo, corpomensagem, destinatarios):

            try:         
                # conexão com os servidores do google
                smtp_ssl_host = 'smtp.gmail.com'
                smtp_ssl_port = 465

                # username ou email para logar no servidor
                username = 'daniel.lomezohdm@gmail.com'

                password = 'daniellomezo008090'

                emaildeenvio = username
                destinatarios = destinatarios, 'daniel.ubletech@gmail.com'



                # a biblioteca email possuí vários templates
                # para diferentes formatos de mensagem
                # neste caso usaremos MIMEText para enviar
                # somente texto


                message = MIMEMultipart()
                message.attach(MIMEText(corpomensagem, 'plain'))
                message['subject'] = titulo
                message['from'] = emaildeenvio
                message['to'] = ', '.join(destinatarios)
                #config = os.path.join(os.path.dirname(os.path.abspath(__file__)))
                #attachment = open(config, "rb")

                part = MIMEBase('application', 'octet-stream')
                #part.set_payload((attachment).read())
                #encoders.encode_base64(part)
                #part.add_header('Content-Disposition', "attachment; filename={}".format(caminho.replace('logs/', '')))
                #print(caminho)
                message.attach(part)

                # conectaremos de forma segura usando SSL
                server = smtplib.SMTP_SSL(smtp_ssl_host, smtp_ssl_port)

                # para interagir com um servidor externo precisaremos
                # fazer login nele
                server.login(username, password)
                server.sendmail(emaildeenvio, destinatarios, message.as_string())
                server.quit()

            except:
                print('erro')
