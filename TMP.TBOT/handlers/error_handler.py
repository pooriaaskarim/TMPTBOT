from telegram import Update
from telegram.ext import ContextTypes

from services import logging


def errorHandler(
        update: Update | None,
        context: ContextTypes.DEFAULT_TYPE | None,
        ):
    try:
        raise context.error
    except Exception as e:
        log = f'HANDLER:ERROR\n'
        if update:
            log += f'User: {update.effective_user.id}:@{update.effective_user.username}:{update.effective_user.full_name}\n'
        log += f'Error: {e}'

        logging.errors.logger.error(log)