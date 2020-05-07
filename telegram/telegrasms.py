import requests
import datetime

class Telegram(object):



    def bot_sendtextinfo(self, mensagem):
            global bot_message
          
            bot_message = ''.format()


            bot_token = '1038036762:AAHAkPA4grLaDft7C7jYEbisqzox5z3GpZ8'
            bot_chatID = '-1001239394424'
            send_text = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + bot_chatID + '&parse_mode=html&text=' + str(bot_message)

            response = requests.get(send_text)

            return response.json()
