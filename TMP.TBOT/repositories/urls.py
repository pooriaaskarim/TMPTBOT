base_url = '##'

symbols_base = '##'
symbols_get_all_tickers = f'{base_url}{symbols_base}##'
def symbolsSearchUrl(tickerOrTitle:str)-> str: return f'{base_url}{symbols_base}##{tickerOrTitle}'
def symbolsGetUrl(ticker:str)-> str: return f'{base_url}{symbols_base}##{ticker}'

economic_calendars_get_url =  f'{base_url}##'