from bs4 import BeautifulSoup

from models import TechnicalAnalysisContent
from repositories.http_handler import HttpHandler

url = '##'
    
def get() -> list[TechnicalAnalysisContent] | None:
    try:
        response = HttpHandler.session.get(url)
        if response.status_code == 200:
            
            html_string = response.text
            soup = BeautifulSoup(html_string, 'html.parser')

            raw_contents = soup.find('div', attrs= {'class':'archive-posts-container'})
            
            ta_content : list[TechnicalAnalysisContent] = []

            for raw_content in raw_contents.findAll('div', attrs= {'class': 'archive-posts-item'}):
                content_image = raw_content.find('div', attrs= {'class':'archive-posts-item-image-cover'}).get('style')
                content_title = raw_content.a.get_text()
                content_url = raw_content.a.get('href')

                ta_content.append(
                    TechnicalAnalysisContent(
                        title = content_title,
                        image = content_image,
                        url = content_url,
                    )
                )

            return ta_content
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