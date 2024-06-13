from enum import StrEnum
from datetime import (
    datetime,
    timedelta,
    date,)
import jdatetime
jdatetime.set_locale('fa_IR')

from telegram import (
    Update,
    InlineKeyboardButton,
    InlineKeyboardMarkup,
    )
from telegram.constants import ParseMode
from telegram.ext import ContextTypes

from models import EconomicNewsData
from services import caching

class NewsType(StrEnum):
    CURRENT_WEEK = 'خبر‌های هفته‌ی جاری'
    NEXT_WEEK = 'خبر‌های هفته‌ی آینده'
    # ALL = 'همه‌ی خبر‌ها'
    UPCOMMING = 'خبر‌های جاری'

def _retriveAllNews() -> list[EconomicNewsData]:
    return caching.economic_calendar.get()

def _retriveUpcommingNews(upcommingDate:datetime.date = datetime.now().date()):
    allNews = _retriveAllNews()
    upcommingNews = list[EconomicNewsData]()
    maxDate = max([x.date for x in allNews])
    for news in allNews:
        if news.date == upcommingDate:
            upcommingNews.append(news)
    if upcommingNews.__len__() > 0:
        return upcommingNews
    else:
        if upcommingDate >= maxDate:
            return upcommingNews
        else:
            return _retriveUpcommingNews(upcommingDate=upcommingDate+timedelta(days=1))
                
def _retriveCurrentWeekNews():
    allNews = _retriveAllNews()
    currentDate = date.today()
    dayOfWeek = currentDate.weekday()
    currentWeekStart = currentDate - timedelta(days=dayOfWeek)
    currentWeekEnd = currentWeekStart + timedelta(days=6)
    currentWeekNews = list[EconomicNewsData]()
    
    for news in allNews:
        if currentWeekStart <= news.date <= currentWeekEnd:
            currentWeekNews.append(news)
    
    return currentWeekNews
    
def _retriveNextWeekNews():
    allNews = _retriveAllNews()
    currentDate = date.today()
    dayOfWeek = currentDate.weekday()
    currentWeekStart = currentDate - timedelta(days=dayOfWeek)
    currentWeekEnd = currentWeekStart + timedelta(days=6)
    nextWeekStart = currentWeekEnd + timedelta(days=1)
    nextWeekEnd = nextWeekStart + timedelta(days=6)
    currentWeekNews = list[EconomicNewsData]()
    
    for news in allNews:
        if nextWeekStart <= news.date <= nextWeekEnd:
            currentWeekNews.append(news)
    
    return currentWeekNews

async def getEconomicNews(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE,
    callback: bool = False,
    ) -> None:
    from handlers.callback_handler import CallbackKey
    from handlers.message_handler import MessageAction
    
    buttons: list[InlineKeyboardButton] = [
            # [
            #     # InlineKeyboardButton(
            #     #     text= NewsType.ALL,
            #     #     callback_data=f'{CallbackKey.ECONOMICCALENDAR}\n{MessageAction.GET_ECONOMIC_CALENDAR}:{NewsType.ALL}',
            #     #     ),
            #     InlineKeyboardButton(
            #         text= NewsType.UPCOMMING,
            #         callback_data=f'{CallbackKey.ECONOMICCALENDAR}\n{MessageAction.GET_ECONOMIC_CALENDAR}:{NewsType.UPCOMMING}',
            #        ),

            # ],
            [
               InlineKeyboardButton(
                text= NewsType.NEXT_WEEK,
                callback_data=f'{CallbackKey.ECONOMICCALENDAR}\n{MessageAction.GET_ECONOMIC_CALENDAR}:{NewsType.NEXT_WEEK}',
                ),
               InlineKeyboardButton(
                text= NewsType.CURRENT_WEEK,
                callback_data=f'{CallbackKey.ECONOMICCALENDAR}\n{MessageAction.GET_ECONOMIC_CALENDAR}:{NewsType.CURRENT_WEEK}',
                ),

            ],
        ]
    reply_markup = InlineKeyboardMarkup(inline_keyboard=buttons)
    async def printNews(
        title:str,
        newsDataList: list[EconomicNewsData],
        ) -> None:
        reply_message = f'🔔 فهرست {f"{title}"}\n'
        if newsDataList.__len__() > 0:
            for newsData in newsDataList:
                for news in newsData.items:
                    reply_message += f'\n'
                    reply_message += f'''
📈 خبر: {news.title}   
🌎 ارز: {news.currency} 
✅ واقعی: {news.actual}
🔅 پیشبینی: {news.forecast}
🔅 قبلی: {news.previous}
⏰ ساعت انتشار: {newsData.time}
🗓 تاریخ: {jdatetime.datetime.fromgregorian(datetime=newsData.date,).strftime("%a %d %b")} | {newsData.date.strftime("%Y/%m/%d")}
'''
        else:
            reply_message += 'داده‌ای وجود ندارد'
        
        reply_message += '''
💻 ##.ir
📱 @## 🤖 @##_Bot'''

        await update.effective_chat.send_message(
                text=reply_message,
                reply_markup=reply_markup
            )

    message = ''.join(update.callback_query.data.splitlines(keepends=True)[1:]) if callback else update.effective_message.text
    
    if f'{MessageAction.GET_ECONOMIC_CALENDAR}:{NewsType.NEXT_WEEK}' in message:
        await printNews(
            title=NewsType.NEXT_WEEK,
            newsDataList=_retriveNextWeekNews(),
        )
    elif f'{MessageAction.GET_ECONOMIC_CALENDAR}:{NewsType.CURRENT_WEEK}' in message:
        await printNews(
            title=NewsType.CURRENT_WEEK,
            newsDataList=_retriveCurrentWeekNews(),
        )
    # elif f'{MessageAction.GET_ECONOMIC_CALENDAR}:{NewsType.ALL}' in message:
    #     await printNews(
    #         title=NewsType.ALL,
    #         newsDataList=retriveAllNews(),
    #     )
    else:
        await printNews(
            title=NewsType.UPCOMMING,
            newsDataList=_retriveUpcommingNews(),
        )