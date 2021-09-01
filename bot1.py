import telebot

bot = telebot.TeleBot("1831377953:AAF3aR6A4Bw9tleOHX_fA1xOLYZU6xbSwjM")
@bot.message_handler(commands=["help","start"])

def enviar(message):
    bot.reply_to(message,"Hola,Como estas?")

@bot.message_handler(func=lambda message:True)

def mensaje(message):
    bot.reply_to(message, message.text)

bot.polling()    
