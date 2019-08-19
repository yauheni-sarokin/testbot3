import telebot
#new comment
#from colorama import init
#from colorama import Fore, Back, Style
#init()

#print(Back.GREEN)

print("started")
#sys.stdout.flush()

bot =  telebot.TeleBot("759571628:AAFtmCaDudbElJMu9COkXhTMjUFSc5wXDtY")

@bot.message_handler(content_types=['text'])
def send_welcome(message):
	#bot.reply_to(message, "Howdy, how are you doing?")
	bot.send_message(message.chat.id,"responce: " +  message.text)
	if message.text == "lol":
#		id = str(2)
#		type(id)
#		print("wow you know it: " + str(message.chat.id))
#		print("wow you know it: " + id)
		bot.send_message(message.chat.id, "wow you know it, your id is : " + str(message.chat.id))

#	print(message.text)

bot.polling( none_stop = True )