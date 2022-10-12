import requests
import datetime


class Telegram(object):

	def bot_sendtextinfo(self, nome=None, titulo=None, email_phone_number=None, id_user=None, mensagem=None, tipo_message=None):
  
		if not tipo_message:

			bot_message = """Olá, eu me chamo, {}\n Quero falar sobre:{}\n 
	
							Meu Id ou número para contato é:{}\n 
							Meu email{}\n 
							E a minha mensagem é:{}\n """.format(nome, titulo, id_user, email_phone_number, mensagem)

			bot_token = '1180610851:AAG3VsePZsCE5ZXNSJltmMaPPr9YwDgQrZU'
			bot_chatID = '-486594727'
			send = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + bot_chatID + '&parse_mode=html&text=' + str(bot_message)
			#response = requests.get(send_text)
			r = requests.get(send)

			print(r)
		if tipo_message == "casamento":
			bot_message = f"Mensagem sobre o casamento: \n\n" \
						  f"Nome Completo: {nome} \n" \
						  f"Telefone para contato: {email_phone_number} \n"\
						  f"Mensagem enviada: {mensagem} \n"


			bot_token = '1180610851:AAG3VsePZsCE5ZXNSJltmMaPPr9YwDgQrZU'
			bot_chatID = '-486594727'
			send = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + bot_chatID + '&parse_mode=html&text=' + str(
				bot_message)
			# response = requests.get(send_text)
			r = requests.get(send)

			print(r)

		
