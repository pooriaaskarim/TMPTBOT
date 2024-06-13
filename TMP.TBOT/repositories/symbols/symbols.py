from models import (
    Symbol, 
    SymbolSearchResult,
    SymbolCategory,
    prices
    )
from repositories.http_handler import HttpHandler
from repositories.urls import (
    symbols_get_all_tickers,
    symbolsGetUrl,
    symbolsSearchUrl,
    )
from repositories.token_handler import getToken

class SymbolsRepository:
    @staticmethod
    def getSymbol(ticker:str) -> Symbol | None:
        try:
            response =  HttpHandler.session.request(
                url = symbolsGetUrl(ticker),
                method = 'GET',
                headers = {
                         "Authorization": getToken(),
                         },
                )
        
            if response.status_code == 200:
                result :dict = response.json()['data']
                prices_data = result['prices']
                symbol_category : SymbolCategory = next((category for category in list(SymbolCategory) if  result['category'] in category), None)
                symbol_ticker = result['ticker'] if result.__contains__('ticker') else None
                symbol_title = result['title'] if result.__contains__('title') else None

                symbolPrices= {
                    prices.Daily.__name__: prices.Daily(
                        close=prices_data['daily']['close'],
                        high=prices_data['daily']['high'],
                        low=prices_data['daily']['low'],
                        open=prices_data['daily']['open']
                        ),
                    prices.Yesterday.__name__: prices.Yesterday(
                        close=prices_data['yesterday']['close'],
                        high=prices_data['yesterday']['high'],
                        low=prices_data['yesterday']['low'],
                        open=prices_data['yesterday']['open']
                        ),
                    prices.OneHour.__name__: prices.OneHour(
                        close=prices_data['oneHour']['close'],
                        high=prices_data['oneHour']['high'],
                        low=prices_data['oneHour']['low'],
                        open=prices_data['oneHour']['open']
                        ),
                    prices.FourHour.__name__: prices.FourHour(
                        close=prices_data['fourHour']['close'],
                        high=prices_data['fourHour']['high'],
                        low=prices_data['fourHour']['low'],
                        open=prices_data['fourHour']['open']
                        ),
                    prices.Weekly.__name__: prices.Weekly(
                        close=prices_data['weekly']['close'],
                        high=prices_data['weekly']['high'],
                        low=prices_data['weekly']['low'],
                        open=prices_data['weekly']['open']
                        ),
                    prices.Monthly.__name__: prices.Monthly(
                        close=prices_data['monthly']['close'],
                        high=prices_data['monthly']['high'],
                        low=prices_data['monthly']['low'],
                        open=prices_data['monthly']['open']
                        ),
                }

                symbol = Symbol(
                    title=symbol_title,
                    ticker=symbol_ticker,
                    category=symbol_category,
                    prices=symbolPrices,
                    )

                return symbol
            elif response.status_code == 204:
                return None
            else: 
                raise(Exception(f'''
got {response.status_code} from respose:
\t{response.status_code}
'''))
        except Exception as e:
                raise(Exception(f'''
got {response.status_code} from respose:
\t{response.status_code}
with Exception:
{e}
'''))
 
    @staticmethod
    def search(tickerOrTitle: str) -> list[SymbolSearchResult] | None:
        try:
            response =  HttpHandler.session.request(
            url = symbolsSearchUrl(tickerOrTitle),
            method = 'GET',
            headers = {
                     "Authorization": getToken(),
                     },
            )
        
            if response.status_code == 200:
                results = list[SymbolSearchResult]()
                for item in response.json()['data']:
                    results.append(SymbolSearchResult(
                    ticker=item['ticker'],
                    title=item['title'],
                    ))
                return results
            elif response.status_code == 204:
                return None
            else: 
                raise(Exception(f'''
got {response.status_code} from respose:
\t{response.status_code}
'''))
        except Exception as e:
                raise(Exception(f'''
got {response.status_code} from respose:
\t{response.status_code}
with Exception:
{e}
'''))

    @staticmethod
    def getAllTickers() -> list[SymbolSearchResult] | None:
        try:
            response =  HttpHandler.session.request(
                url = symbols_get_all_tickers,
                method = 'GET',
                headers = {
                         "Authorization": getToken(),
                         },
                )

            if response.status_code == 200:
                results = list[SymbolSearchResult]()

                for item in response.json()['data']:
                    results.append(
                        SymbolSearchResult(
                            ticker = item['ticker'],
                            title = item['title'],
                            )
                        )

                return results
            elif response.status_code == 204:
                return None
            else: 
                raise(Exception(f'''
got {response.status_code} from respose:
\t{response.status_code}
'''))
        except Exception as e:
                raise(Exception(f'''
got {response.status_code} from respose:
\t{response.status_code}
with Exception:
{e}
'''))
 