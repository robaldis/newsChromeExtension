#process_article.py 
from bs4 import BeautifulSoup
import requests
    
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
    
def article_to_string(url):
    """
    Process the body of the article from the given url
    """
    #NOTE: this may need to be chagned for different ways different sites lay
    # the website out.

    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'html.parser')
    # find all the p tages int the article tag. 
    p = soup.article.find_all('p')
    finalString = "" 
    for s in p:
        try:    
            finalString += s.string
        except:
            # This tag has no text, the text is probably in a child tag
            # this is usualy text with styling
            # NOTE: This may need to changed to make the recomendations work better
            pass
    return finalString


# Testing
if __name__ == "__main__":
    p = ProcessArticle()
    string = p.setUrl("https://www.bbc.co.uk/news/uk-england-bristol-55173667")
