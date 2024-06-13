from telegram.ext import (
    ApplicationBuilder, 
    CommandHandler, 
    MessageHandler, 
    InlineQueryHandler, 
    filters,
    CallbackQueryHandler,
    )
from telegram import Update

import handlers


def runner() -> None:
    BOT_TOKEN = '##'
   
    application = (ApplicationBuilder()
    .token(BOT_TOKEN)
    .arbitrary_callback_data(True)
    .build()
    )

    application.add_handlers(
        handlers = [
        CommandHandler(
            command = handlers.command_handlers.CommandAction.START,
            callback = handlers.command_handlers.start,
        ),
        CommandHandler(
            command = handlers.command_handlers.CommandAction.INTRODUCTION,
            callback = handlers.command_handlers.introduction,
        ),
        CommandHandler(
            command = handlers.command_handlers.CommandAction.TERMS_OF_USE,
            callback = handlers.command_handlers.termsOfUse,
        ),
        CommandHandler(
            command = handlers.command_handlers.CommandAction.SYMBOLS_HELP,
            callback = handlers.command_handlers.symolsHelp,
        ),
        CommandHandler(
            command = handlers.command_handlers.CommandAction.DISCOUNT,
            callback = handlers.command_handlers.discount,
        ),
        ]
    )
    
    application.add_handler(
        handler = MessageHandler(
            filters = filters.TEXT,
            callback = handlers.message_handler.messageHandler,
            ),
        )
    
    application.add_handler(
        handler = CallbackQueryHandler(
            callback = handlers.callback_handler.callbackHandler,
            )
        )
    
    application.add_handler(
        handler = InlineQueryHandler(
            callback = handlers.inline_handler.inlineSymbolSearch,
            )
        )
    
    application.add_error_handler(
        callback = handlers.error_handler.errorHandler,
        )
    
    application.run_polling(
        allowed_updates = Update.ALL_TYPES,
        )