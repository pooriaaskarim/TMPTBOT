from models.pivot import Pivot
from enum import StrEnum

class Price:
    def __init__(
            self,
            close: float,
            open: float,
            high: float,
            low: float,
            ):
        self.close = close
        self.open = open
        self.high = high
        self.low = low
    
    def faName(self): pass
    
    def pivot(self) -> Pivot:
        pivotPoint = (self.high + self.low + self.close) / 3
        r1 = (pivotPoint * 2) - self.low
        r2 = (pivotPoint * 1) + (self.high - (1 * self.low))
        r3 = (pivotPoint * 2) + (self.high - (2 * self.low))
        r4 = (pivotPoint * 3) + (self.high - (3 * self.low))
        r5 = (pivotPoint * 4) + (self.high - (4 * self.low))
        s1 = (pivotPoint * 2) - self.high
        s2 = (pivotPoint * 1) - ((1 * self.high) - self.low)
        s3 = (pivotPoint * 2) - ((2 * self.high) - self.low)
        s4 = (pivotPoint * 3) - ((3 * self.high) - self.low)
        s5 = (pivotPoint * 4) - ((4 * self.high) - self.low)
        
        return Pivot(
            pivotPoint = pivotPoint,    
            r1 = r1,    
            r2 = r2,    
            r3 = r3,    
            r4 = r4,    
            r5 = r5,    
            s1 = s1,    
            s2 = s2,    
            s3 = s3,    
            s4 = s4,    
            s5 = s5,    
        )
    
    def __str__(self) -> str:
        return f'''
close: {self.close}
open: {self.open}
high: {self.high}
low: {self.low}
'''
    def __repr__(self):
        return self.__str__()

class Daily(Price):
    def faName(self):
        return 'امروز'
    
class Yesterday(Price):
    def faName(self):
        return 'روزانه'
    
class OneHour(Price):
    def faName(self):
        return 'یک ساعته'
    
class FourHour(Price):
    def faName(self):
        return 'چهار ساعته'
    
class Weekly(Price):
    def faName(self):
        return 'هفتگی'
    
class Monthly(Price):
    def faName(self):
        return 'ماهانه'
    
