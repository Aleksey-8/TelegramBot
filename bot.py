	#библиотеки, которые загружаем из вне
import telebot
import config

from telebot import types

bot = telebot.TeleBot(config.TOKEN)

@bot.message_handler(commands=['start'])
def welcome(message):
	sti = open('static/welcome2.webp', 'rb')
	bot.send_sticker(message.chat.id, sti)

	#клавиатура
	markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
	item1 = types.KeyboardButton("Команды Bash")
	item2 = types.KeyboardButton("Linux")

	markup.add(item1, item2)

	bot.send_message(message.chat.id, "Привет, {0.first_name}!".format(message.from_user, bot.get_me()),
		parse_mode='html', reply_markup=markup)

#назначаем действие для клавиатуры
@bot.message_handler(content_types=['text'])
def lalala(message):
	if message.chat.type == 'private':
		if message.text == 'Команды Bash':
			bot.send_message(message.chat.id, 'https://docs.google.com/document/d/1NoE_u8BlKXNlMcVyFh6708PE39BCgO-s3Cp4Z9MJatM/edit?usp=sharing ')
		elif message.text == 'Linux':
			bot.send_message(message.chat.id, 'https://docs.google.com/document/d/1InUCjgYyQqZJUZu-0VcIiuH9BrCDTdjqAMgbSDdMTu4/edit ')
		else:
			bot.send_message(message.chat.id, 'Не знаю что ответить😢')


bot.polling(none_stop=True)

##sdfsdf








#https://core.telegram.org/bots/api#available-methods

