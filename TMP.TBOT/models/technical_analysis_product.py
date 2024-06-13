class TechnicalAnalysisProduct:
    def __init__(self,
            title: str,
            image: str,
            description: str,
            url: str,
            active_price: str,
            discount_price: str,
            ):
        self.title = title
        self.image = image
        self.description = description
        self.url = url
        self.active_price = active_price
        self.discount_price = discount_price

    def __str__(self) -> str:
        return f"""
title: {self.title},
image: {self.image},
description: {self.description},
url: {self.url},
active_price: {self.active_price},
discount_price: {self.discount_pric},
"""