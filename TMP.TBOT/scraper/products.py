from bs4 import BeautifulSoup

from models import Product
from repositories.http_handler import HttpHandler

url = '##'

def get() -> list[Product] | None:
    try:
        response = HttpHandler.session.get(url)
        if response.status_code == 200:
            html_string = response.text
            soup = BeautifulSoup(html_string, 'html.parser')
            
            products : list[Product] = []
            
            for raw_product in soup.find_all('div', attrs={'class': 'products-item'}):
                product_title = raw_product.find(
                    attrs={'class': 'products-item-title'}).get_text()
                product_url = raw_product.find(
                    attrs={'class': 'products-item-title'}).a.get('href')
                product_image = raw_product.find(
                    'img', attrs={'class': 'products-item-cover'}).get('src')
                price_div = raw_product.find(
                    'div', attrs={'class': 'product-price'})
                if (price_div.span.get_text() == 'رایگان'):
                    product_active_price= price_div.span.get_text()
                    product_discount_price = ''
                else:
                    product_active_price= price_div.find('span', attrs={'class': 'product-price-active'}).get_text()
                    product_discount_price = price_div.find('span', attrs={'class': 'product-price-del'}).get_text()

                products.append(
                    Product(
                        title=product_title,
                        image=product_image,
                        url=product_url,
                        active_price=product_active_price,
                        discount_price=product_discount_price,
                        )
                    )

            return products
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