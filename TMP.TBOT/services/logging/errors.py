import logging
import logging.handlers

from services.logging.files import getLogFilename, LogDirectory

LOGGER = 'errors'
logger = logging.getLogger(LOGGER)
logger.setLevel(logging.ERROR)

handler = logging.handlers.TimedRotatingFileHandler(
        filename = getLogFilename(
            log_directory = LogDirectory.ERRORS_LOG,
            file = f'error',
            ),
        when = 'midnight',
        interval = 1,
        backupCount=30,
    )
handler.suffix = "%Y-%m-%d.log"
formatter = logging.Formatter('%(asctime)s %(name)s %(levelname)s\n%(message)s\n',)
handler.setFormatter(formatter)

logger.addHandler(handler)