import telebot
from telebot import types
import random

token = '6011626036:AAE7HxqRMERDRSKs86807qDNkQ-ksicTfRg'

bot = telebot.TeleBot(token)

markup_menu = types.ReplyKeyboardMarkup(resize_keyboard=True)
btns = ["Noțiune"]
for btn in btns:
    markup_menu.add(types.KeyboardButton(btn))

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, 'Salut, eu sunt DreptMDBOT. Te voi ajuta sa înveți definițiile din domeniul dreptului. Scrie-mi orice. ')
    
@bot.message_handler(content_types="text")
def send_random_word(message):
    with open("words.txt") as words_list:
        lines = words_list.readlines()
        random_word = random.choice(lines)    
    bot.send_message(message.chat.id, random_word, reply_markup=markup_menu)

bot.infinity_polling()