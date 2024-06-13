from telegram import (
    Update,
    ReplyKeyboardMarkup,
    KeyboardButton,
    )
from telegram.ext import ContextTypes

from enum import StrEnum

class CommandAction(StrEnum):
    START = "Start"
    SYMBOLS_HELP = "SymbolsHelp"
    INTRODUCTION = "Introduction"
    TERMS_OF_USE = "TermsOfUse"
    DISCOUNT = "Discount"

async def start(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE,
    ) -> None:

    await update.message.reply_text(
        f'''👋 به ربات تلگرام ## خوش آمدید!

💎 در ربات تلگرام ## میتوانید به نرخ‌های لحظه‌ای، هشدارهای قیمتی، ابزارهای محاسباتی، مطالب آموزشی، تحلیل‌های بازار و سایر امکانات کاربردی که به مرور به ربات اضافه خواهند شد دسترسی داشته باشید!

برای استفاده از این ربات در گروه‌های تلگرامی کافیست ابتدا ربات را عضو گروه کرده و سپس قبل از نام نماد مدنظرتان یک نقطه قرار دهید. به عنوان مثال 👇
. خودرو
. btcusdt
. xauusd

✅ آشنایی با امکانات ربات: /{CommandAction.INTRODUCTION}
📝 قوانین و شرایط: /{CommandAction.TERMS_OF_USE}
💻 ##.ir
📱 @## 🤖 @##_Bot
‌''',
        reply_markup=_create_buttons_markup(),
    )
    
async def symolsHelp(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE,
    ) -> None:

    await update.message.reply_text(
        f'''⭕️ در صورتی که نماد جستجو شده توسط شما وجود ندارد ممکن است نام نماد مدنظر را به شکل نادرست وارد کرده باشید. 

✅ نحوه وارد کردن نام نمادها به شکل صحیح برای بازارهای مختلف
⭐️ بازار بورس
نام نماد را به صورت فارسی و مطابق آنچه که در وبسایت سازمان بورس وجود دارد وارد کنید. به عنوان مثال برای جستجوی نماد شرکت ایران خودرو باید دقیقا کلمه خودرو برای ربات ارسال نمایید. 

⭐️ بازار فارکس
برای این بازار باید نام نمادها را به صورت انگلیسی و به شکل زیر وارد کنید. 
مثلا برای جفت ارز یورو/دلار باید عبارت EURUSD را وارد کنید و یا برای اونس جهانی طلا عبارت XAUUSD را ارسال نمایید.

⭐️ بازار ارزهای دیجیتال
برای جستجوی نمادهای بازار ارزهای دیجیتال نیز بایستی مطابق بازار فارکس عمل کنید. در واقع نام ارسالی نمادها به صورت انگلیسی باشد. 
به عنوان مثال برای دسترسی به اطلاعات نماد بیت کوین عبارت BTCUSDT را ارسال نمایید. یا برای دسترسی به قیمت جفت ارز اتریوم/بیت کوین عبارت ETHBTC را وارد کنید.

✅ برای استفاده از قابلیت جستجوی نمادها در گروه‌های تلگرامی باید در ابتدای نام نماد مدنظرتان یک نقطه تایپ کنید. به عنوان مثال 👇
. خودرو
. btcusdt
. xauusd


💻 ##.ir
📱 @## 🤖 @##_Bot
‌''',
    )
    
async def termsOfUse(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE,
    ) -> None:

    await update.message.reply_text(
        f'''قوانین و شرایط استفاده از ربات تلگرام ##

⭐️ استفاده از ربات تلگرام ## (آیدی ربات اینجا قرار گیرد) به معنای پذیرفتن تمامی قوانین و شرایطی است که در ادامه ذکر شده‌اند. 

✅ داده‌های قیمتی موجود در این ربات از منابع معتبر تامین شده و ## دخل و تصرفی در آنها ندارد. 

✅ برخی داده‌های موجود در ربات ممکن است به صورت محاسباتی ارائه شوند که فرمول‌های آنها از روش‌های معتبر بدست آمده‌اند. 

✅ داده‌های موجود در ربات کاملا بروز می‌باشند. با این حال ممکن است بر اثر اختلالات اینترنت و ارتباطات سرورها با شبکه داخل و خارج از کشور، مشکلاتی بوجود بیایند که باعث اخلال در بروزرسانی داده‌ها گردند. این موارد به طور دائم توسط بخش فنی ## در حال مانیتورینگ بوده و رفع خواهند شد. بنابراین قبل از انجام هر معامله‌ای داده‌ها را با محل انجام معامله (کارگزاری و ...) تطبیق دهید. 

✅ داده‌های موجود در ربات تلگرام ## صرفا حالت اطلاع رسانی داشته و نباید ملاک انجام معاملات شما قرار گیرند. قبل از انجام هر گونه معامله‌ در هر بازاری، تمامی اطلاعات را بررسی کرده و با تصمیم خودتان اقدام کنید. 

✅ تحلیل‌های ارایه شده در ربات تلگرام ## صرفا جنبه آموزشی داشته و به هیچ عنوان سیگنال معاملاتی محسوب نمی‌شوند. بنابراین مسئولیت معامله بر اساس این تحلیل‌ها متوجه شخص معامله‌گر می‌باشد. 

✅ در ربات تلگرام ## امکان خرید و فروش در هیچ بازاری (سهام، طلا، ارز، کالا، ارزهای دیجیتال و ...) وجود ندارد و صرفا نمایش دهنده داده‌های بازار می‌باشد.

✅ در حال حاضر به دلیل وجود ممنوعیت از سوی نهادهای قانونی، ارائه نرخ بازار داخلی طلا و ارز از طریق ربات تلگرام ## انجام نمیشود. در صورتی که موانع مذکور برطرف شوند، این بازار نیز به سرعت تحت پوشش قرار خواهد گرفت. با این حال نمودارهای طلا و ارز را میتوانید از طریق وبسایت ## به سادگی مشاهده کنید.

✅ هشدارهای قیمتی ارسال شده از طریق ربات تلگرام ## صرفا جنبه اطلاع رسانی داشته و نباید ملاک انجام معاملات قرار گیرند. بنابراین قبل از انجام هر معامله‌ای داده‌ها را با محل انجام معامله (کارگزاری و ...) تطبیق دهید. 

⚠️ این توافقنامه ممکن است در هر زمانی بروزرسانی شود. بنابراین به صورت دوره‌ای این بخش را بررسی کرده تا از شرایط جدید استفاده از خدمات ## مطلع شوید.

💻 ##.ir
📱 @## 🤖 @##_Bot
‌''',
    )
    
async def introduction(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE,
    ) -> None:

    await update.message.reply_text(
        f'''✅🤖 امکانات ربات تلگرام ##

💎 دسترسی به نرخ‌های بازارهای مختلف
در ربات تلگرام ## میتوانید به نرخ‌های لحظه‌ای بازارهای مختلف دسترسی داشته باشید. این بازارها شامل موارد زیر می‌شوند: 
🔅 بورس
🔅فارکس
🔅ارزهای دیجیتال 
علاوه بر نرخ‌های لحظه‌ای، اطلاعات OHLC روزانه قیمت نیز در اختیار شما قرار خواهند گرفت. 

💎 پیوت‌ها
در ربات تلگرام ## میتوانید به سادگی پیوت‌های ۱ ساعته، ۴ ساعته، روزانه، هفتگی و ماهانه هر نماد را مشاهده کنید. کافیست نماد مدنظر خود را جستجو کرده و روی دکمه مربوط به پیوت‌ها کلیک کنید.

💎 هشدارهای قیمتی
در صورتی که کاربر وبسایت ## باشید و روی نمادهای مختلف هشدار تنظیم کرده باشید، این هشدار از طریق ربات تلگرام ## برای شما ارسال خواهند شد. 

💎 تقویم اقتصادی
دسترسی به گزارش‌های مهم اقتصادی (و آمار و ارقام مرتبط با آنها) که همه روزه از سوی اقتصادهای بزرگ جهان منتشر شده و گاها تاثیرات بسیار قدرتمندی روی قیمت‌ها دارند یکی دیگر از قابلیت‌های ربات تلگرام ## میباشد. 
علاوه بر این در صورتی که کاربر وبسایت ## باشید و روی گزارش‌های اقتصادی هشدار تنظیم کرده باشید، هشدارهای مربوطه را از طریق ربات نیز دریافت خواهید کرد. 

💎 مطالب آموزشی و تحلیل‌ها
## صرفا یک پلتفرم ارائه نمودار نیست. بلکه از طریق آکادمی ## میتوانید به مطالب آموزشی و تحلیلی نیز دسترسی پیدا کنید. کافیست روی دکمه "مطالب آموزشی" یا "تحلیل بازار" کلیک کنید تا آخرین موارد موجود برای شما ارسال شوند. 


🔥 منتظر قابلیت‌ها و امکانات بیشتر در ربات تلگرام ## باشید...
‌''',
    )

async def discount(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE,
    ) -> None:

    await update.message.reply_text(
        f'''💚 برای دریافت کدهای تخفیف میتوانید عضو کانال تلگرام ما شده و یا صفحه اینستاگرام ما را دنبال کنید! کدهای تخفیف مناسبتی و همچنین کدهای #سه‌شنبه_طلایی را میتوانید از این طریق دریافت کنید.

✅ کانال تلگرام: t.me/##
✅ صفحه اینستاگرام: https://##.ir/INST
✅ صفحه‌های آفرهای ##: https://##.ir/offer

💻 ##.ir
📱 @## 🤖 @##_Bot
‌''',
    )



def _create_buttons_markup():
    from handlers.message_handler import MessageAction
    
    buttons: list[list[KeyboardButton]] = [
        [
            MessageAction.GET_ECONOMIC_CALENDAR,
            ],
        [
            MessageAction.GET_EDUCATIONAL_CONTENT,
            MessageAction.GET_PRODUCTS,
            ],
        [
            MessageAction.GET_TECHNICAL_ANALYSIS,
            MessageAction.GET_TECHNICAL_ANALYSIS_CONTENTS,
            ]
    ]

    reply_markup = ReplyKeyboardMarkup(keyboard=buttons)
    return reply_markup