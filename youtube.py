""" Find youtube URL for song  """
import urllib
import urllib2
from bs4 import BeautifulSoup


def youtube_search(Title):
    text_to_search = Title
    query = urllib.quote(text_to_search)
    url = "https://www.youtube.com/results?search_query=" + query
    response = urllib2.urlopen(url)
    html = response.read()
    soup = BeautifulSoup(html, "lxml")
    vid = soup.findAll(attrs={'class': 'yt-uix-tile-link'})
    x = vid[0]['href']
    url = "https://www.youtube.com/embed/" + x[9:] + "?autoplay=1"
    return url
