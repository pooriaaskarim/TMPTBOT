from telegram import (
    Update,
    InlineKeyboardButton,
    InlineKeyboardMarkup,
    MessageEntity,
    )
from telegram.ext import ContextTypes

import scraper
import assets

async def getProducts(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE,
    ) -> None:
    buttons: list[InlineKeyboardButton] = []
    reply_markup: InlineKeyboardMarkup

    products = scraper.products.get()
    for product in products:
        buttons.append(
            InlineKeyboardButton(
                text=product.title,
                url=product.url,
            ),
        )

    reply_markup = InlineKeyboardMarkup.from_column(buttons)
    title = 'دوره‌ها - آکادمی ##'
    description = 'دوره‌های آموزشی ## فرصت مناسبی برای یادگیری اصول تحلیل تکنیکال، استراتژی‌های معاملاتی و یا آشنایی با ابزارهای کاربردی در تحلیل بازار هستند. این دوره‌ها به ساده‌ترین شکل ممکن آموزش داده شده‌اند و به همین خاطر به هیچ پیش نیازی برای یادگیری آنها نیاز ندارید!'
    await update.message.reply_photo(
        photo=f'{assets.paths.CONTENT_IMAGES}products.png',
        caption=f'{title}\n{description}',
        caption_entities=[MessageEntity(
            type=MessageEntity.TEXT_LINK,
            url=scraper.products.url,
            offset=0, length=title.__len__(),
        ),
        ],
        reply_markup=reply_markup,
    )

async def getTechnicalAnalysis(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE,
    ) -> None:
    analysis = scraper.technical_analysis.get()
    keyboard = [
        [InlineKeyboardButton(
            text=analysis.title, url=analysis.url)],
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)

    await update.message.reply_photo(
        photo=analysis.image,
        reply_markup=reply_markup,
        caption='''
    {}
    هزینه: {}'''.format(analysis.description, analysis.active_price),
    )

async def getEducationaContent(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE,
    ):
    contents = scraper.educational_content.get()
    buttons: list[InlineKeyboardButton] = []
    reply_markup: InlineKeyboardMarkup

    for content in contents:
        buttons.append(
            InlineKeyboardButton(
                text = content.title[0],
                url = content.url,
            ),
        )

    reply_markup = InlineKeyboardMarkup.from_column(buttons)
    title = 'مطالب آموزشی - آکادمی ##'
    description = 'مطالب آموزشی آکادمی ## میتوانند مهمترین نکات در تحلیل بازار و معامله‌گری را به شکل جامع اما ساده و مختصر به شما منتقل کنند. با مثال‌های متعدد از نمودارهای واقعی و ویدئوهای آموزشی کوتاه!'
    await update.message.reply_photo(
        photo=f'{assets.paths.CONTENT_IMAGES}educational_contents.png',
        caption=f'{title}\n{description}',
        caption_entities=[MessageEntity(
            type = MessageEntity.TEXT_LINK,
            url = scraper.educational_content.url,
            offset = 0,
            length = title.__len__(),
        )],
        reply_markup = reply_markup,
    )

async def getTechnicalAnalysisContent(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE,
    ):
    contents = scraper.technical_analysis_content.get()
    buttons: list[InlineKeyboardButton] = []
    reply_markup: InlineKeyboardMarkup

    for content in contents[0 : min(3,contents.__len__())]:
        buttons.append(
            InlineKeyboardButton(
                text = content.title[0],
                url = content.url,
            ),
        )

    reply_markup = InlineKeyboardMarkup.from_column(buttons)
    title = 'تحلیل‌ها - آکادمی ##'
    description = 'تحلیل‌های بازار جهانی به شما یک دید گسترده از شرایط بازار و همچنین نواحی حساس بازار را ارائه خواهند کرد. نکته: این تحلیل‌ها صرفا جنبه آموزشی داشته و سیگنال خرید و فروش محسوب نمی‌شوند. بنابراین ## مسئولیتی در قبال سود و زیان ناشی از آنها را نخواهد پذیرفت.'
    await update.message.reply_photo(
        photo = f"{assets.paths.CONTENT_IMAGES}technical_analysis_content.png",
        caption = f'{title}\n{description}',
        caption_entities = [MessageEntity(
            type = MessageEntity.TEXT_LINK,
            url = scraper.technical_analysis_content.url,
            offset = 0,
            length = title.__len__(),
        )],
        reply_markup = reply_markup,
    )