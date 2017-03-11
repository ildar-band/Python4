from telegram.ext import Updater, CommandHandler, MessageHandler, Filters # CommandHandler - модуль содержащий диспеитчер , message handler -обработчик текстовых сообщений
def main():
	updater = Updater('357554854:AAHRJPfmVlbrysK8OjL96wfyyccBK_9gLnc') # экземпляр класса Updater - updater
	dp = updater.dispatcher # создаем короткую переменную диспетчер
	dp.add_handler(CommandHandler("start", greet_user))# добавляем обработчик, который реагирует на команду /start и greet_user - это функция которая будет вызываться, когда юзер пришлет команду
	dp.add_handler(MessageHandler([Filters.text], talk_to_me)) # хендлер будет вызывать эту функцию только когда придет текстовое сообщение, для видео или картинки она не будет вызываться
	updater.start_polling() # подключись к платформе и получи обновления
	updater.idle() # жди сообщение от телеграмма
	# мы проимпортировали апдейтер, передали ему ключ, сказали подключись и жди дальнейших указаний.
	dp.add_error_handler(show_error)# обработчик ошибок, функция которая вызывается если что то пошло не так, отвалился вай фай например

def talk_to_me(bot, update):
	print(update.message.text)
	bot.sendMessage(update.message.chat_id, update.message.text)

def greet_user(bot,update):
	print('Вызван /start')
	#print(update)	
	bot.sendMessage(update.message.chat_id, text = "Привет! Давай общаться") # переменная бот отдает команды боту отправить сообщения, апдейт мессадж идентификатор чата и сам мессадж который мы отправляем

def show_error(bot, update, error):
	print(error)

main()

