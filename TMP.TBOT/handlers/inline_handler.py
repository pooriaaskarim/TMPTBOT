from uuid import uuid4

from telegram import (
    Update,
    InlineQueryResultArticle,
    InputTextMessageContent,
    )

from telegram.constants import ParseMode
from telegram.ext import ContextTypes

from repositories import SymbolsRepository
from services import logging
from handlers import middlewares

async def inlineSymbolSearch(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE,
    ) -> None:
    """Handle the inline query. This is run when you type: @botusername <query>"""
    if await middlewares.joinedChannel(update=update,context=context):
        query = update.inline_query


        if not query.query:  # empty query should not be handled
            return

        log = f'''HANDLER:INLINE:QUERY
    User: {update.effective_user.id}:@{update.effective_user.username}:{update.effective_user.full_name}
    Query: {query}
    Data: {query.query}'''

        try:
            queryResults : list[InlineQueryResultArticle] = []
            searchResults = SymbolsRepository.search(query.query)
            if searchResults:
                for searchResult in searchResults:
                    queryResults.append(
                        InlineQueryResultArticle(
                            id=str(uuid4()),
                            title=searchResult.title,
                            input_message_content=InputTextMessageContent(
                            message_text=  f'.`{searchResult.ticker}`',
                            parse_mode=ParseMode.MARKDOWN
                            ),
                            ))
            else:
                    queryResults.append(
                        InlineQueryResultArticle(
                            id=str(uuid4()),
                            title='موردی یافت نشد.',
                            input_message_content=InputTextMessageContent(
                            message_text=  'موردی یافت نشد.',
                                ),
                            ))

            await update.inline_query.answer(
                results=queryResults,
                cache_time=10,
                auto_pagination=True,
                )

            logging.requests.logger.info(log)

        except Exception as e:
            log += f'\nError: {e}'

            logging.errors.logger.error(log)
            logging.requests.logger.error(log)


























