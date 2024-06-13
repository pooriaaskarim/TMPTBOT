import os
from enum import StrEnum
from io import FileIO

import assets

class CacheFile(StrEnum):
    TICKERS_CACHE = f'{assets.paths.DATA_CACHE}tickers.dbm'
    ECONOMIC_CALENDAR_CACHE = f'{assets.paths.DATA_CACHE}ec.dbm'

def get(
        cache_file: CacheFile,
        mode:str,
        ) -> FileIO:
    assert cache_file.startswith(assets.paths.DATA_CACHE), 'Invalid Directory'
    if not os.path.exists(assets.paths.CACHE_BASE):
        os.mkdir(assets.paths.CACHE_BASE)
    if not os.path.exists(assets.paths.DATA_CACHE):
        os.mkdir(assets.paths.DATA_CACHE)
        
    return open(
        file=cache_file,
        mode=mode,
        )