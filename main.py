from telegram.ext import Updater, InlineQueryHandler, CommandHandler,CallbackContext
import requests
# import re
import logging
import os
# import schedule
from telegram import Update

PORT = int(os.environ.get('PORT', '8443'))
TOKEN = '5323869763:AAFI2Rlf3csFljCrcjTYG_Z6P114qqmeBu4'
m_help = "You can use the following commands:\n"\
"/practiceword : First select the destination language then select the right answer\n"\

def help(update: Update, context: CallbackContext):
    """Send a message when the command /help is issued."""
    update.message.reply_text(m_help)


def error(update, context):
    """Log Errors caused by Updates."""
    logging.warning('Update "%s" ', update)
    logging.exception(context.error)
# def get_url():
#     contents = requests.get('https://dog.ceo/api/breeds/image/random').json()
#     url = contents['message']
#     return url

# aaaa
# def get_image_url():
#     allowed_extension = ['jpg', 'jpeg', 'png']
#     file_extension = ''
#     while file_extension not in allowed_extension:
#         url = get_url()
#         file_extension = re.search("([^.]*)$", url).group(1).lower()
#     return url


# def bop(update, context):
#     url = get_image_url()
#     chat_id = update.message.chat.id
#     context.bot.send_photo(chat_id=chat_id, photo=url)


def main():
    updater = Updater(TOKEN)
    dp = updater.dispatcher
    # dp.add_handler(CommandHandler('bop', bop))
    dp.add_handler(CommandHandler("help", help))
    



    # PORT = int(os.environ.get('PORT', '8443'))
    # updater.start_webhook(listen="0.0.0.0",
    #                         port=PORT,
    #                         url_path=TOKEN,
    #                         webhook_url='https://newtele-app.herokuapp.com/'+TOKEN)
                        #   https://web.telegram.org/z/#5323869763
    updater.start_polling()
    updater.idle()
    # while True:
        # schedule.run_pending()
    #     # The sleep prevents the CPU to work unnecessarily.
    #     time.sleep(1)
    dp.add_error_handler(error) 



if __name__ == '__main__':
    print("Starting...")
    main()

