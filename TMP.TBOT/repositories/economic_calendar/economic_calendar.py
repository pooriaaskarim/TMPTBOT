from datetime import datetime
from repositories.http_handler import HttpHandler
from repositories.urls import economic_calendars_get_url
from repositories.token_handler import getToken

from models import (
    EconomicNewsData,
    EconomicNews,
    )

class EconomicCalendarRepository:
    def get() -> list[EconomicNewsData] | None:
        response = HttpHandler.session.request(
            url=economic_calendars_get_url,
            method='GET',
            headers={
            "Authorization": getToken(),
            },
        )
        try:
            if response.status_code == 200:
                data : dict = response.json()['data']
                economicNewsData = list[EconomicNewsData]()
                for newsDataJson in data:
                    date_string = newsDataJson["date"]
                    time_string = newsDataJson["time"]
                    date_time_string = newsDataJson["date_time"]
                    
                    date_news_date = datetime.strptime(
                        f'{date_string}',
                        f'%Y-%m-%d',
                        ).date(),
                    date_news_time = datetime.strptime(
                        f'{"00:00" if time_string == "Tentative" else time_string}',
                        '%H:%M',
                        ).time(),
                    date_news_date_time = datetime.strptime(
                        f'{date_time_string}'.strip(' Tentative'),
                        f'%Y-%m-%d{"" if f"{date_time_string}".endswith(" Tentative") else " %H:%M:%S"}',
                        ), 
                    economicNewsData.append(
                        EconomicNewsData(
                            date = date_news_date[0],
                            time = date_news_time[0],
                            date_time = date_news_date_time[0],
                            items=[
                                    EconomicNews(
                                        id = newsJson['id'],
                                        title = newsJson['title'],
                                        currency = newsJson['currency'],
                                        measures = newsJson['measures'],
                                        description = newsJson['description'],
                                        usual_effect = newsJson['usual_effect'],
                                        frequency = newsJson['frequency'],
                                        ff_notes = newsJson['ff_notes'],
                                        why_traders_care = newsJson['why_traders_care'],
                                        actual = newsJson['actual'],
                                        forecast = newsJson['forecast'],
                                        previous = newsJson['previous'],
                                        impacts = newsJson['impacts'],
                                        ) for newsJson in newsDataJson['items']
                                ]
                        )
                    )
                return economicNewsData
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