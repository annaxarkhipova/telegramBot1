# -*- coding: utf-8 -*-
import telebot

bot = telebot.TeleBot("")
@bot.message_handler(content_types=["text"])
def handle_text(message):
    if message.text == "Hi":
        bot.send_message(message.from_user.id, 'Hi, babe. My name is Jack. And I want to get aquainted with you. '
        'Send /cancel to get me off.\n\n'
        'Whatcha name?')
    
    elif message.text == 'Name of %s: %s' or message.text == "How are you?":
        bot.send_message(message.from_user.id, "Okay, nice to meet ya. Are you able to send me a pic of yourself, "
                              "so I can know what you look like, or send /skip if you don't want to.")

    else:
        bot.send_message(message.from_user.id, 'Um. What?')                      
        
bot.polling(none_stop=True, interval=0)

# Обработчик команд '/start' '/cancel' '/help'.
@bot.message_handler(commands=['/start', '/cancel', '/help'])
def handle_start_help(message):
    pass

 # Обработчик для документов и аудиофайлов
@bot.message_handler(content_types=['document', 'audio'])
def handle_document_audio(message):
    bot.send_message(message.from_user.id, "thanks")
    pass

bot.polling(none_stop=True, interval=0)