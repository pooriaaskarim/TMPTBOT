from .prices import Price
from enum import StrEnum

class SymbolCategory(StrEnum):
    FOREX = 'forex'
    BOURSE = 'bourse'
    CRYPTO = 'crypto'
    
    def __str__(self) -> str:
        return self._value_
    
    def __repr__(self) -> str:
        return self.__str__()

class SymbolSearchResult:
    def __init__(
            self,
            ticker: str,
            title: str,
            ):
        self.ticker = ticker 
        self.title = title

    def matches(self, value:str) -> bool:
        '''
        return true of value matches ticker or title'''
        return (value.upper() == self.ticker.upper() or value == self.title)
    
    def __str__(self):
        return f'''
            ticker: {self.ticker},
            title: {self.title},
        '''
    def __repr__(self):
        return self.__str__()

class Symbol:
    def __init__(
            self,
            prices: dict[str,Price],
            category: SymbolCategory | None,
            ticker: str | None = None,
            title: str | None = None,
            ):
        self.ticker = ticker 
        self.category  = category,
        self.title = title
        self.prices = prices

    def get_pivot(self,price:str) :
        return self.prices[price].pivot()

    def get_pivot_markdown_formatted_string(self,price:str,) -> str :
        return f"{self.title}\nپیوت {self.prices[price].faName()}\n{self.prices[price].pivot().markDownFormattedString(floatFormatter='.0f' if self.category[0] is SymbolCategory.BOURSE else '.2f' if self.category[0] is SymbolCategory.CRYPTO else '.5f')}"
        # return self.get_pivot(price=price)
        
    def __str__(self):
        return f'''
ticker: {self.ticker}
title: {self.title}
category: {self.category}
prices: {self.prices}
        '''
    def __repr__(self):
        return self.__str__()
        
