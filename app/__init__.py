import logging

from telegram.ext import (CommandHandler, ConversationHandler, Filters,
                          MessageHandler, Updater, CallbackQueryHandler)

from config import PROXY_URL, PROXY_USERNAME, PROXY_PASSWORD, API_KEY
from .main_dialog import start_bot, FIRST_STEP, selected, SECOND_STEP, selected_course

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

logger = logging.getLogger(__name__)

PROXY = {
    'proxy_url': PROXY_URL,
    'urllib3_proxy_kwargs':
        {'username': PROXY_USERNAME,
         'password': PROXY_PASSWORD}
}


def create_app():
    mybot = Updater(API_KEY, use_context=True, request_kwargs=PROXY)
    dp = mybot.dispatcher

    conv = ConversationHandler(
        entry_points=[CommandHandler('start', start_bot)],
        states={
            FIRST_STEP: [
                CallbackQueryHandler(selected)
            ],
            SECOND_STEP: [CallbackQueryHandler(selected_course)]
        },
        fallbacks=[]
    )

    dp.add_handler(conv)

    mybot.start_polling()
    mybot.idle()
