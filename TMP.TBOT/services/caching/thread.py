from threading import Thread
import schedule  
from time import sleep

from services import caching


def scheduleFlush():
    '''
    Flushes pending schedules every Minute
    '''
    while True:
        schedule.run_pending()
        sleep(60)
        # sleep(3600)
        
cache_thread = Thread(
    target=scheduleFlush,
    daemon=True,
    name='Cache Daemon',
    )


def initialize() -> None:
    schedule.every().day.at(time_str="01:00",tz='Etc/UCT').do(caching.symbols.cache).run()
    schedule.every(1).minute.do(caching.economic_calendar.cache).run()
    cache_thread.start()
    
def dispose() -> None:
    cache_thread.join()

    