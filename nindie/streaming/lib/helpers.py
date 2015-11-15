

def create_url_from_artist(name):
    """
    Turns a string into a last.fm url for that artist
    :param name: artist name
    :return: url string
    """
    new_name = "last.fm/music/" + name.replace(" ", "+") + "/+similar"
    return new_name
