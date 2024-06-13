from telegram import (
    Update,
    InlineKeyboardButton,
    InlineKeyboardMarkup,
    ChatMember,
    )
from telegram.ext import ContextTypes
from telegram.constants import ChatMemberStatus

async def joinedChannel(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE,
    ) -> None:
    user : ChatMember |None = await context.bot.get_chat_member(chat_id='@##', user_id=update.effective_user.id)
    if user and user.status not in [ChatMemberStatus.LEFT, ChatMemberStatus.RESTRICTED,ChatMemberStatus.BANNED] :
        return True
    else:
        buttons : list[InlineKeyboardButton] = [
            InlineKeyboardButton(
                text='عضویت در کانال',
                url='https://t.me/##',
                ),
        ]
        reply_markup : InlineKeyboardMarkup = InlineKeyboardMarkup.from_column(button_column=buttons)
        await update.effective_chat.send_message(
            text=f'''
💚 برای استفاده از ربات ## ابتدا عضو کانال تلگرام ## شوید.
سپس به ربات برگشته و روی دکمه "در کانال عضو شدم" را کلیک کنید.
''',
            reply_markup=reply_markup,
            )
        return False