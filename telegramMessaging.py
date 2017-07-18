import telebot
import data

telegramToken = data.get('telegramToken')
telegramChatID = data.get('telegramChatID')

def sendMessage(message):
    bot = telebot.TeleBot(telegramToken)
    bot.config['api_key'] = telegramToken
    bot.send_message(telegramChatID, message)

