from datetime import datetime

class EconomicNews:
    def __init__(
            self,
            id : int,
            title : str,
            currency : str,
            measures : str | None,
            description : str | None,
            usual_effect : str | None,
            frequency : str | None,
            ff_notes : str | None,
            why_traders_care : str | None,
            actual : float | None,
            forecast : float | None,
            previous : float | None,
            impacts : float | None,
            ) -> None:
        id
        self.title = title
        self.currency = currency
        self.measures = measures
        self.description = description
        self.usual_effect = usual_effect
        self.frequency = frequency
        self.ff_notes = ff_notes
        self.why_traders_care = why_traders_care
        self.actual = actual
        self.forecast = forecast
        self.previous = previous
        self.impacts = impacts
    
    def __str__(self) -> str:
        return f'''
title: {self.title}
currency: {self.currency}
measures: {self.measures}
description: {self.description}
usual_effect: {self.usual_effect}
frequency: {self.frequency}
ff_notes: {self.ff_notes}
why_traders_care: {self.why_traders_care}
actual: {self.actual}
forecast: {self.forecast}
previous: {self.previous}
impacts: {self.impacts}
'''

    def __repr__(self) -> str:
        return self.__str__()

class EconomicNewsData:
    def __init__(
            self,
            date : datetime,
            time : datetime,
            date_time : datetime,
            items : list[EconomicNews],
            ) -> None:
        self.date = date    
        self.time = time
        self.date_time = date_time
        self.items = items

    def __str__(self) -> str:
        return f'''
date: {self.date}
time: {self.time}
date_time: {self.date_time}
items: {self.items}
'''
    def __repr__(self) -> str:
        return self.__str__()

