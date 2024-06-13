import jdatetime
from zoneinfo import ZoneInfo

from telegram import (
    Update,
    Message,
    InlineKeyboardButton,
    InlineKeyboardMarkup,
    )
from telegram.ext import ContextTypes

from services import (
    caching, 
    logging,
    )
from repositories import SymbolsRepository
from models import Symbol

async def getSymbol(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE,
    symbol_or_ticker:str,
    override_offline_search: bool = False,
    ) -> None:

    
    symbol : Symbol | None = None
    ticker : str | None = None
    
    if override_offline_search:
        ticker = symbol_or_ticker
    else:
        cachedTickers = caching.symbols.get()
        for searchResult in cachedTickers:
            if searchResult.matches(symbol_or_ticker):
                ticker = searchResult.ticker
                break
            
    if ticker:
        symbol = SymbolsRepository.getSymbol(ticker = ticker)
    log = f'''SYMOLSGET
User: {update.effective_user.id}:@{update.effective_user.username}:{update.effective_user.first_name}
Overrided_Offline_search: {override_offline_search}
Message: {update.message}
symbol_or_ticker: {symbol_or_ticker}'''

    if symbol:
        log += f'\nTicker: {ticker}'
        logging.symbols.logger.info(log)
        await update.message.reply_text(
            text=_pretify(symbol),
            reply_markup=_getSymbolsMarkup(symbol.ticker),
            )
    else:
        logging.symbols.logger.error(log)
        await update.message.reply_text(
            text=_getTickerNotFound(),
            )

        
async def updateSymbol(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE,
    ticker: str,
    ) -> None:
    
    symbol = SymbolsRepository.getSymbol(ticker)

    if symbol:
        await update.effective_message.edit_text(
            text=_pretify(symbol),
            reply_markup=_getSymbolsMarkup(symbol.ticker),
            )
    else:
        await update.effective_message.edit_text(
            text=_getTickerNotFound(),
            )
        
async def openPivots(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE,
    ticker: str,
    ) -> None:
    
    symbol = SymbolsRepository.getSymbol(ticker)

    if symbol:
        await update.effective_message.edit_text(
            text=_pretify(symbol),
            reply_markup=_getSymbolsMarkupExpanded(symbol),
            )
    else:
        await update.effective_message.edit_text(
            text=_getTickerNotFound(),
            )
        
async def closePivots(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE,
    ticker: str,
    ) -> None:
    
    await update.effective_message.edit_reply_markup(
        reply_markup=_getSymbolsMarkup(ticker),
        )


def _getSymbolsMarkup(ticker:str):
    from handlers.callback_handler import CallbackKey
    
    return InlineKeyboardMarkup(
            inline_keyboard = [
            [           
            InlineKeyboardButton(
                text= 'پیوت',
                callback_data= f"{CallbackKey.OPENSYMBOLPIVOTS} {ticker}",
            ),
            InlineKeyboardButton(
                text= '🔄 به‌روز‌رسانی',
                callback_data= f"{CallbackKey.UPDATESYMBOL} {ticker}",
            ),
            ],
                ])
    
def _getSymbolsMarkupExpanded(symbol:Symbol):
    from handlers.callback_handler import CallbackKey
    
    return InlineKeyboardMarkup(
            inline_keyboard = [
            [           
            InlineKeyboardButton(
                text= 'بازگشت',
                callback_data= f"{CallbackKey.CLOSESYMBOLPIVOTS} {symbol.ticker}",
            ),
            InlineKeyboardButton(
                text= '🔄 به‌روز‌رسانی',
                callback_data= f"{CallbackKey.UPDATESYMBOL} {symbol.ticker}",
            ),
            ],
            [
            InlineKeyboardButton(
                text= 'پیوت روزانه',
                callback_data= f"{CallbackKey.ECHO} SymbolPivotData\n{symbol.get_pivot_markdown_formatted_string(price='Yesterday')}",
            ),
            ],
            [           
            InlineKeyboardButton(
                text= 'پیوت یک ساعته',
                callback_data= f"{CallbackKey.ECHO} SymbolPivotData\n{symbol.get_pivot_markdown_formatted_string(price='OneHour')}",
            ),
            InlineKeyboardButton(
                text= 'پیوت چهار ساعته',
                callback_data= f"{CallbackKey.ECHO} SymbolPivotData\n{symbol.get_pivot_markdown_formatted_string(price='FourHour')}",
            ),
            ],
            [
            InlineKeyboardButton(
                text= 'پیوت ماهانه',
                callback_data= f"{CallbackKey.ECHO} SymbolPivotData\n{symbol.get_pivot_markdown_formatted_string(price='Monthly')}",
            ),
            InlineKeyboardButton(
                text= 'پیوت هفتگی',
                callback_data= f"{CallbackKey.ECHO} SymbolPivotData\n{symbol.get_pivot_markdown_formatted_string(price='Weekly')}",
            ),
            ],
                ])

def _pretify(symbol):
    return f'''
💎 نام نماد: {symbol.title}
✅ آخرین قیمت: {symbol.prices['Daily'].close}

🔅 شروع: {symbol.prices['Daily'].open}
🔅 بالاترین: {symbol.prices['Daily'].high}
🔅 پایین‌ترین: {symbol.prices['Daily'].low}
🔅 آخرین قیمت: {symbol.prices['Daily'].close}

📅 {jdatetime.datetime.now(tz=ZoneInfo('Asia/Tehran')).strftime("%Y/%m/%d %H:%M:%S")}

💻 ##.ir
📱 @## 🤖 @##_Bot
‌
'''

def _getTickerNotFound():
    return '''❌ موردی یافت نشد! لطفا نام نماد ارسالی خود را بررسی کنید.
برای دریافت راهنمای دریافت نماد از /SymbolsHelp استفاده کنید.'''