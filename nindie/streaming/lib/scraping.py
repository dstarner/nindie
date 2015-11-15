from urllib.request import urlopen
from bs4 import BeautifulSoup


def get_similar_artists(artist_name):
    """
    Gets similar artists of a band
    :param artist_name: string of artist name
    :return: List of similar artist strings
    """
    url = "http://www.last.fm/music/" + artist_name.replace(" ", "+") + "/+similar"
    html_string = urlopen(url).read()

    # Open Beautiful soup for artist url
    soup = BeautifulSoup(html_string)
    similar_artists = []

    # Go through and find everything
    for hit in soup.find_all(attrs={'class': "link-block-target"}):
        similar_artists.append(str(hit.text))

    print(similar_artists)
    # Returns artist list
    return similar_artists


if __name__ == "__main__":
    artists = get_similar_artists("Rise Against")
    print(artists)
