from telegram import Update
from telegram.ext import ContextTypes
from telegram.constants import ChatType
import handlers

from handlers import middlewares
from services import logging

from enum import StrEnum

class MessageAction(StrEnum):
    GET_ECONOMIC_CALENDAR = "تقویم اقتصادی"
    GET_PRODUCTS = "دوره‌های آموزشی"
    GET_TECHNICAL_ANALYSIS = "دوره‌ی تحلیل بازار"
    GET_EDUCATIONAL_CONTENT = "مطالب آموزشی"
    GET_TECHNICAL_ANALYSIS_CONTENTS = "تحلیل‌های بازار جهانی"

async def messageHandler(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE,
    ):
    if await middlewares.joinedChannel(update=update,context=context):
            message = update.effective_message

            log = f'''HANDLER:MESSAGE:QUERY
User: {update.effective_user.id}:@{update.effective_user.username}:{update.effective_user.full_name}
Message: {message}
Data: {message.text}'''

            try:
                validRequest = False
                parsting_message = message.text

                if update.effective_chat.type != ChatType.PRIVATE:  # if not in bot chat
                                                                    # donot parse messages
                                                                    # that dont start with a .
                    if not parsting_message.startswith('.'):
                        return
                    
                parsting_message = parsting_message.lstrip('.').lstrip(' ') # strip '.'s and ' 's from left
                   

                if MessageAction.GET_ECONOMIC_CALENDAR in parsting_message:
                    await handlers.economic_calendar.getEconomicNews(update=update, context=context)
                    validRequest = True
                elif MessageAction.GET_PRODUCTS in parsting_message:
                    await handlers.scraper.getProducts(update=update, context=context)
                    validRequest = True
                elif MessageAction.GET_TECHNICAL_ANALYSIS in parsting_message:
                    await handlers.scraper.getTechnicalAnalysis(update=update, context=context)
                    validRequest = True
                elif MessageAction.GET_EDUCATIONAL_CONTENT in parsting_message:
                    await handlers.scraper.getEducationaContent(update=update, context=context)
                    validRequest = True
                elif MessageAction.GET_TECHNICAL_ANALYSIS_CONTENTS in parsting_message:
                    await handlers.scraper.getTechnicalAnalysisContent(update=update, context=context)
                    validRequest = True
                else:
                    await handlers.symbols.getSymbol(
                        update = update,
                        context = context,
                        symbol_or_ticker = parsting_message,
                        )
                    validRequest = True

                if validRequest:
                    logging.requests.logger.info(log)




            except Exception as e:
                log += f'\nError: {e}'

                logging.errors.logger.error(log)
                logging.requests.logger.error(log)

