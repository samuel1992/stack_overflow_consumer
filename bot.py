import logging

from stackoverflow.stackoverflow import StackOverFlow

from telegram.ext import Updater, CommandHandler

# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)
logger = logging.getLogger(__name__)

TOKEN = '1128284111:AAFGvQIDozd-LUgbpurm__NKeKZCiZGpFZg'

def error(update, context):
    logger.warning('Update %s caused error %s', update, context.error)

def message(questions):
    questions.sort(key=lambda q: q.score, reverse=True)

    message = ""
    for question in questions[:10]:
        message += f"Title: {question.title}\n"
        message += f"Votes: {question.score}\n"
        message += f"Link: {question.link}\n\n"

    return message

def search(update, context):
    text_to_search = ' '.join(context.args)
    text = message(StackOverFlow().search(text_to_search))

    update.message.reply_text(text)


def main():
    updater = Updater(TOKEN, use_context=True)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('search', search, pass_args=True))
    dp.add_error_handler(error)

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
