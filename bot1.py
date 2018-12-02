# -*- coding: utf-8 -*-
import telebot

bot = telebot.TeleBot("736744887:AAEb0flmzZmRLH5_Y7VXg-FxEeGhxW25F4k")
@bot.message_handler(content_types=["text"])
def handle_text(message):
    if message.text == "Hi":
        bot.send_message(message.from_user.id, "Hello! I am HabrahabrExampleBot. How can i help you?")
    
    elif message.text == "How are you?" or message.text == "How are u?":
        bot.send_message(message.from_user.id, "I'm fine, thanks. And you?")
        
bot.polling(none_stop=True, interval=0)

# Обработчик команд '/start' '/skip' '/help'.
@bot.message_handler(commands=['start', 'skip', 'help'])
def handle_start_help(message):
    pass

 # Обработчик для документов и аудиофайлов
@bot.message_handler(content_types=['document', 'audio'])
def handle_document_audio(message):
    pass

bot.polling(none_stop=True, interval=0)