import telebot
import time
token = '6522302180:AAE1liTMwfnmBNhqy7ZAxjZgeL0iXoR-OFM'
bot = telebot.TeleBot(token)
@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, 'Присетствую, чем могу помочь?')

@bot.message_handler(commands=['timer'])
def say(message):
    for i in range(5):
        time.sleep(1)
        bot.send_message(message.chat.id, i+1)
@bot.message_handler(commands=['say'])
def say(message):
    text = ' '.join(message.text.split(' ')[1:])
    bot.reply_to(message, f'***{text.upper()}!***')
@bot.message_handler(content_types='text')
def reverse_text(message):
    if 'плохой' in message.text.lower():
        bot.reply_to(message, 'текст содержит слово плохой')
        return
    text = message.text[::-1]
    bot.reply_to(message,text)

@bot.message_handler(content_types=['stiker'])
def send_sticker(message):
    print(message)
    file_ID = ''
bot.polling()