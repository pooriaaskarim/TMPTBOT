import pickle

from services.logging import caching
from services.caching import files
from repositories.economic_calendar import EconomicCalendarRepository
from models.economic_calendar import EconomicNewsData

def cache() -> bool:
    '''
    Returns True on data cached, False on NoData'''
    try:
        data = EconomicCalendarRepository.get()
        if data:
            cache_file = files.get(files.CacheFile.ECONOMIC_CALENDAR_CACHE,'wb')
            pickle.dump(data, cache_file)
            cache_file.close()
            
            caching.logger.info(msg='Cached Economic Calendar')
            return True
        else:
            return False
    except Exception as e:
        caching.logger.error(msg=e)
        return False

    
def get() -> list[EconomicNewsData]:
        econimic_calendar_cache = files.get(
            files.CacheFile.ECONOMIC_CALENDAR_CACHE,
            'rb',
            )
        cached_results : list[EconomicNewsData] = pickle.load(econimic_calendar_cache)
        econimic_calendar_cache.close()
        
        return cached_results