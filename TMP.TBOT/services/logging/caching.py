import logging
import logging.handlers

from services.logging.files import LogDirectory, getLogFilename 

LOGGER = 'caching'
logger = logging.getLogger(LOGGER)
logger.setLevel(logging.INFO)

handler = logging.handlers.TimedRotatingFileHandler(
        filename = getLogFilename(
            log_directory = LogDirectory.CACHES_LOG,
            file = f'cache',
            ),
        when = 'midnight',
        interval = 1,
        backupCount=30,
    )
handler.suffix = "%Y-%m-%d.log"
formatter = logging.Formatter('%(asctime)s %(name)s %(levelname)s\n%(message)s\n',)
handler.setFormatter(formatter)

logger.addHandler(handler)