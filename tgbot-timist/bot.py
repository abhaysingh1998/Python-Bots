from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import logging
from google import search

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)


greet_words = ['hey', 'Hey', 'HEY' , 'HI', 'hi', 'Hi', 'Hello', 'hello']
def start(bot, update):
    user = update.message.from_user
    update.message.reply_text('Hi {} ! Use /set <seconds> to set a timer '.format(user['username']))


def alarm(bot, job):
    bot.send_message(job.context, text='Beep! Beep! Beep!')


def set_timer(bot, update, args, job_queue, chat_data):
    chat_id = update.message.chat_id
    try:
        due = int(args[0])
        if due < 0:
            update.message.reply_text('Sorry we can not go back in Ancient times!')
            return

        job = job_queue.run_once(alarm, due, context=chat_id)
        chat_data['job'] = job

        update.message.reply_text('Timer successfully set!')
        update.message.reply_text('Now u can unset it anytime. Usage: /unset')

    except (IndexError, ValueError):
        update.message.reply_text('Usage: /set <seconds>')


def unset(bot, update, chat_data):
    if 'job' not in chat_data:
        update.message.reply_text('You have no active timer')
        return

    job = chat_data['job']
    job.schedule_removal()
    del chat_data['job']

    update.message.reply_text('Timer successfully unset!')
def reply(bot, update):
    for word in update.message.text.split(' '):
        if word in greet_words:
            update.message.reply_text("Hey ....!! May i help with something ? May be i can do some searching for you XD ..!")
            break
    else:
        update.message.reply_text("Ohk fine ..!")
        result = list(search(update.message.text, stop=20))
        update.message.reply_text("Here You Go XD!!!")
        for url in result[:5]:
            update.message.reply_text(url)
        update.message.reply_text("Job Done ......")

def error(bot, update, error):
    logger.warning('Update "%s" caused error "%s"', update, error)

def main():
    updater = Updater("<Token>")

    dp = updater.dispatcher

    # commands in bot
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("help", start))
    dp.add_handler(CommandHandler("set", set_timer,
                                  pass_args=True,
                                  pass_job_queue=True,
                                  pass_chat_data=True))
    dp.add_handler(CommandHandler("unset", unset, pass_chat_data=True))
    dp.add_handler(MessageHandler(Filters.text, reply))

    # log all errors
    dp.add_error_handler(error)

    # Start the Bot
    updater.start_polling()

    updater.idle()


if __name__ == '__main__':
    main()
