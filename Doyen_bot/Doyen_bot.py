# -*- coding: utf-8 -*-
"""
Created on Sat Jun 12 17:54:19 2021

t.me/Doyen_bot
Use this token to access the HTTP API:
1783334306:AAF2tQGG8wO09U_eqqIxoBwQuSZ9fwicka0
Keep your token secure and store it safely, it can be used by anyone to control your bot.
For a description of the Bot API, see this page: https://core.telegram.org/bots/api
Webhook - https://api.telegram.org/bot1783334306:AAF2tQGG8wO09U_eqqIxoBwQuSZ9fwicka0/setWebHook?url=https://script.google.com/macros/s/AKfycbzsRuUsSR9PjDY4bohheVnmERyzzEjZtQIEK1NRwH1wO0EKtAsYEnt6STsg9ofV6ZJJQQ/exec

@author: Marlou
"""

import telebot
import config

bot = telebot.TeleBot(config.TOKEN)

@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Здарова, бандит!')
    keyboard = telebot.types.ReplyKeyboardMarkup(True)
    keyboard.row('Дай ссылку на google диск')
    bot.send_message(message.chat.id, 'Чего хочешь?', reply_markup=keyboard)

    
@bot.message_handler(content_types=['text'])
def send_text(message):
    if message.text.lower() == 'дай ссылку на google диск':
        bot.send_message(message.chat.id, 'Ссылка на Google диск https://drive.google.com/drive/u/0/folders/11mFDNnRwSTJ9Vouz4i0xhL21sIa0YD19')

bot.polling(none_stop=True)

# print('Everything is okey')