import pickle

from services.logging import caching
from services.caching import files
from repositories.symbols import SymbolsRepository
from models.symbols import SymbolSearchResult

def cache() -> bool:
    '''
    Returns True on data cached, False on NoData'''
    try:
        data = SymbolsRepository.getAllTickers()
        if data:
            cache_file = files.get(files.CacheFile.TICKERS_CACHE,'wb')
            pickle.dump(data, cache_file)
            cache_file.close()

            caching.logger.info(
                'Cached Symbol Tickers',
                )
            return True
        else:
            return False
    except Exception as e:
        caching.logger.error(e)
        return False
    
def get() -> list[SymbolSearchResult]:
        symbols_cache = files.get(
            files.CacheFile.TICKERS_CACHE,
            'rb',
            )
        cached_results : list[SymbolSearchResult] =  pickle.load(symbols_cache)
        symbols_cache.close()
        
        return cached_results