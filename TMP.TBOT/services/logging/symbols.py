import logging
import logging.handlers

from services.logging.files import LogDirectory, getLogFilename 

LOGGER = 'symbols'
logger = logging.getLogger(LOGGER)
logger.setLevel(logging.DEBUG)

handler = logging.handlers.TimedRotatingFileHandler(
        filename = getLogFilename(
            log_directory = LogDirectory.SYMBOLS_LOG,
            file = f'symbols',
            ),
        when = 'midnight',
        interval = 1,
        backupCount=30,
    )
handler.suffix = "%Y-%m-%d.log"
formatter = logging.Formatter('%(asctime)s %(name)s %(levelname)s\n%(message)s\n',)
handler.setFormatter(formatter)

logger.addHandler(handler)