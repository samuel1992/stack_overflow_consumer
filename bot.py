import logging

from stackoverflow import StackOverFlow

from telegram.ext import Updater, CommandHandler

# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)
logger = logging.getLogger(__name__)

TOKEN = '1128284111:AAFGvQIDozd-LUgbpurm__NKeKZCiZGpFZg'

def search(update, context):
    text_to_search = ' '.join(context.args)

    result = StackOverFlow().search(text_to_search)
    message = ""
    for i in result[:10]:
        message += f"Title: {i.title}\n"
        message += f"Votes: {i.score}\n"
        message += f"Link: {i.link}\n\n"

    update.message.reply_text(message)

def error(update, context):
    logger.warning('Update %s caused error %s', update, context.error)

def main():
    updater = Updater(TOKEN, use_context=True)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('search', search, pass_args=True))
    dp.add_error_handler(error)

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
