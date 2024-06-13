class Pivot:
    def __init__(
            self,
            pivotPoint : float,
            r1 : float,
            r2 : float,
            r3 : float,
            r4 : float,
            r5 : float,
            s1 : float,
            s2 : float,
            s3 : float,
            s4 : float,
            s5 : float,
            ):
        self.pivotPoint = pivotPoint
        self.r1 = r1
        self.r2 = r2
        self.r3 = r3
        self.r4 = r4
        self.r5 = r5
        self.s1 = s1
        self.s2 = s2
        self.s3 = s3
        self.s4 = s4
        self.s5 = s5

    def __str__(self) -> str:
        return f'''
pivotPoint: {self.pivotPoint}
r1: {self.r1}
r2: {self.r2}
r3: {self.r3}
r4: {self.r4}
r5: {self.r5}
s1: {self.s1}
s2: {self.s2}
s3: {self.s3}
s4: {self.s4}
s5: {self.s5}
    '''
    
    def __repr__(self) -> str:
        return self.__str__()
    
    def markDownFormattedString(
        self,
        floatFormatter:str = '.5f',
        ) -> str:
        def get_formater(value:float) ->str:
            if value >= 1:
                return floatFormatter
            else:
                return ''
        return f"""
🔵 Pivot Point: `{self.pivotPoint:{get_formater(self.pivotPoint)}}`

🔴 R1: `{self.r1:{get_formater(self.r1)}}`
🔴 R2: `{self.r2:{get_formater(self.r2)}}`
🔴 R3: `{self.r3:{get_formater(self.r3)}}`
🔴 R4: `{self.r4:{get_formater(self.r4)}}`
🔴 R5: `{self.r5:{get_formater(self.r5)}}`

🟢 S1: `{self.s1:{get_formater(self.s1)}}`
🟢 S2: `{self.s2:{get_formater(self.s2)}}`
🟢 S3: `{self.s3:{get_formater(self.s3)}}`
🟢 S4: `{self.s4:{get_formater(self.s4)}}`
🟢 S5: `{self.s5:{get_formater(self.s5)}}`

💻 ##.ir
📱 @## 🤖 @##\_Bot
‌
"""