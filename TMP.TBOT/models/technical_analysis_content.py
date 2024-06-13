class TechnicalAnalysisContent:
    def __init__(self,
            title: str,
            image: str,
            url: str,
            ):
        self.title = title,
        self.image = image,
        self.url = url
        
    def __str__(self):
        return f'''
title: {self.title}
image: {self.image}
url : {self.url}
'''