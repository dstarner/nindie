import json
import pafy
from urllib.request import urlopen
from bs4 import BeautifulSoup


def search_youtube(artist_name):
    """
    Returns a JSON object of a list of Songs with a name and url
    :param artist_name: artist to find music for
    :return: JSON object
    """
    scrapable_urls = scrape_yl_urls(artist_name)
    video_data = []

    print("On youtube looking for: " + artist_name)
    print(scrapable_urls)

    for url in scrapable_urls[:3]:
        video = pafy.new(url)
        title = video.title
        song = {'title': title, 'url': url}
        video_data.append(song)
        print(title)

    return video_data


def scrape_yl_urls(artist_name):
    """
    This returns links to the videos for a specific artist
    :param artist_name: specific artist string
    :return: list of string urls
    """
    # Get youtube to web scrape
    url = "https://www.youtube.com/results?search_query=" + artist_name.replace(" ", "+")
    html_string = urlopen(url).read()
    soup = BeautifulSoup(html_string)

    urls = []

    yolo = soup.find_all(attrs={'class': 'yt-uix-sessionlink yt-uix-tile-link yt-ui-ellipsis yt-ui-ellipsis-2       spf-link '})
    print(yolo)

    for hit in yolo:
        good_hit = hit['href'][9:]
        if len(good_hit):
            good_hit = good_hit[:11]
        urls.append(str(good_hit))
        print(hit['href'])

    return urls


if __name__ is "__main__":
    search_youtube("The Who")



