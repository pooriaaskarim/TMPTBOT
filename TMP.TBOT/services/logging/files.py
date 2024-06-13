import os
from enum import StrEnum

import assets

class LogDirectory(StrEnum):
    ERRORS_LOG = f'{assets.paths.LOGS_CACHE}errors/'
    REQUESTS_LOG = f'{assets.paths.LOGS_CACHE}requests/'
    CACHES_LOG = f'{assets.paths.LOGS_CACHE}caches/'
    SYMBOLS_LOG = f'{assets.paths.LOGS_CACHE}symbols/'

def getLogFilename(
        log_directory:LogDirectory,
        file:str,
        ) -> str:
    assert log_directory.startswith(assets.paths.LOGS_CACHE), 'Invalid Directory'
    if not os.path.exists(assets.paths.LOGS_CACHE):
        os.mkdir(assets.paths.LOGS_CACHE)
    if not os.path.exists(log_directory):
        os.mkdir(log_directory)
        
    return f'{log_directory}{file}'