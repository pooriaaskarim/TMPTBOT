from bs4 import BeautifulSoup

from models import TechnicalAnalysisProduct
from repositories.http_handler import HttpHandler

url = '##'

def get() -> TechnicalAnalysisProduct | None:
    try:
        response = HttpHandler.session.get(url)
        if response.status_code == 200:
            html_string = response.text
            soup = BeautifulSoup(html_string, 'html.parser')
            wrapper = soup.find('div', attrs= {'class':'product-single-header-wrapper'})
            product_image = wrapper.find('div', attrs= {'class':'product-single-header-preview-video-cover'}).find('img').get('src')
            product_title = wrapper.find('div', attrs= {'class':'product-single-header-title'}).get_text()
            product_url = wrapper.find('div', attrs= {'class':'product-single-header-action-singup'}).find('a').get('href')
            product_description = wrapper.find('div', attrs= {'class':'product-single-header-desc'}).get_text()
            price_div = wrapper.find('div', attrs= {'class':'product-price'})
            product_active_price = price_div.find('span', attrs={'class':'product-price-active'}).get_text()
            product_discount_price = price_div.find('span', attrs={'class':'product-price-del'}).get_text()

            return TechnicalAnalysisProduct(
                active_price=product_active_price,
                discount_price=product_discount_price,
                description=product_description,
                image=product_image,
                title=product_title,
                url=product_url,
                )
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