import urllib
import urllib.parse
from bs4 import BeautifulSoup
def youtube_search(Title):
    textToSearch = Title 
    query = urllib.parse.quote(textToSearch)
    url = "https://www.youtube.com/results?search_query=" + query
    response = urllib.request.urlopen(url)
    html = response.read()
    soup = BeautifulSoup(html, "lxml")
    vid = soup.findAll(attrs={'class':'yt-uix-tile-link'})
    x= vid[0]['href']
    url = "https://www.youtube.com/embed/" + x[9:]
    #vid = 'https://www.youtube.com' + vid[0]['href']

    return url
