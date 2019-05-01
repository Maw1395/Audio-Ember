import requests
from bs4 import BeautifulSoup
def youtube_search(Title):
    textToSearch = Title 
    url = "https://www.youtube.com/results?search_query=" + Title
    html = requests.get(url).text
    soup = BeautifulSoup(html, "lxml")
    vid = soup.findAll(attrs={'class':'yt-uix-tile-link'})
    x= vid[0]['href']
    url = "https://www.youtube.com/embed/" + x[9:]
   
    #vid = 'https://www.youtube.com' + vid[0]['href']
    

    return url
