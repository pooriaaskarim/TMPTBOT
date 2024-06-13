from enum import StrEnum

from telegram import Update
from telegram.constants import ParseMode
from telegram.ext import ContextTypes

from handlers.economic_calendar import getEconomicNews
from handlers import symbols
from handlers import middlewares

from services import logging

class CallbackKey(StrEnum):
    ECHO = '#ECHO'
    ECONOMICCALENDAR = '#ECONOMICCALENDAR'
    UPDATESYMBOL = '#UPDATESYMBOL'
    OPENSYMBOLPIVOTS = '#OPENSYMBOLPIVOTS'
    CLOSESYMBOLPIVOTS = '#CLOSESYMBOLPIVOTS'
    


async def callbackHandler(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE,
    ):
    '''
    Handles CallBack queries:
            If the query starts with CallbackKey.ECHO, the first line is trimmed and
        the rest is echoed back to chat.
            If the query starts with  CallbackKey.ECONOMICCALENDAR, apropriate economic
        calendar data is echoed back to chat.
            If the query starts with  CallbackKey.UPDATESYMBOL, mentioned ticker will be
        updated.
    '''
    if await middlewares.joinedChannel(update=update,context=context):
        query = update.callback_query

        log = f'''HANDLER:CALLBACK:QUERY
User: {update.effective_user.id}:@{update.effective_user.username}:{update.effective_user.full_name}
Query: {query}
Data: {query.data}'''

        try:
            if query.data.startswith(CallbackKey.ECHO):
                await update.effective_chat.send_message(
                    text=''.join(query.data.splitlines(keepends=True)[1:]),
                    parse_mode= ParseMode.MARKDOWN,
                    )
            elif query.data.startswith(CallbackKey.ECONOMICCALENDAR):
                await getEconomicNews(
                    update=update,
                    context=context,
                    callback=True,
                    )
            elif query.data.startswith(CallbackKey.UPDATESYMBOL):
                ticker = query.data.split(' ')[1]
                await symbols.updateSymbol(
                    update=update,
                    context=context,
                    ticker=ticker,
                    )
            elif query.data.startswith(CallbackKey.OPENSYMBOLPIVOTS):
                ticker = query.data.split(' ')[1]
                await symbols.openPivots(
                    update=update,
                    context=context,
                    ticker=ticker,
                    )
            elif query.data.startswith(CallbackKey.CLOSESYMBOLPIVOTS):
                ticker = query.data.split(' ')[1]
                await symbols.closePivots(
                    update=update,
                    context=context,
                    ticker=ticker,
                    )

            logging.requests.logger.info(log)

        except Exception as e:
            log += f'\nError: {e}'

            logging.errors.logger.error(log)
            logging.requests.logger.error(log)