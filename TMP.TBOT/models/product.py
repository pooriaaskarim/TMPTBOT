class Product:
    def __init__(
            self,
            title: str,
            active_price: str,
            discount_price: str,
            image: str,
            url: str,
            ):
        self.title = title
        self.url = url
        self.image = image
        self.active_price = active_price
        self.discount_price = discount_price

    def __str__(self, ) -> str:
        return f'''
title: {self.title},
active_price: {self.active_price},
discount_price: {self.discount_price},
url: {self.url},
image: {self.image},
'''