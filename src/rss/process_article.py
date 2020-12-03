
from bs4 import BeautifulSoup
import requests

class ProcessArticle():
    def __init__(self):
        pass

    def setUrl(self, url):
        # get the body of the text from the RSS url
        r = requests.get(url)
        soup = BeautifulSoup(r.text, 'html.parser')
        p = soup.article.find_all('p')
        finalString = "" 
        for s in p:
            try:    
                finalString += s.string
            except:
                pass
        return finalSString

# give a URL
# process the url to get the right data
# process that data to get to a cosine silimarity matrix 


if __name__ == "__main__":
    p = ProcessArticle()
    string = p.setUrl("https://www.bbc.co.uk/news/uk-england-bristol-55173667")
