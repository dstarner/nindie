from streaming.lib.pyitunes.pyItunes import Library


def xml_artist_list(xmlfile):
    xmlfile = Library(xmlfile)

    artistList = set()

    for id, song in xmlfile.songs.items():
        if not song.artist in artistList:
            artistList.add(song.artist)

    return list(artistList)

if __name__ is "__main__":
    artist = xml_artist_list("Library.xml")
    print(artist)

