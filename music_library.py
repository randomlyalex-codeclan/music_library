from models.artist import Artist
from models.album import Album
import repositories.artist_repository as artist_repository
import repositories.album_repository as album_repository

artist_1 = Artist("Gerge", "Harrison")
artist_2 = Artist("Iggy", "Pop")
artist_3 = Artist("John", "Lennon")
artist_4 = Artist("Noel", "Gallagher")
artist_5 = Artist("Jack", "White")

album_1 = Album("All Things Must Pass", "Pop-Rock", 1970, artist_1)
album_2 = Album("Lust For Life", "Rock", 1977, artist_2)
album_3 = Album("Plastic Ono Band", "Pop-Rock", 1970, artist_3)
album_4 = Album("Who Built The Moon", "Indie Rock", 2017, artist_4)
album_5 = Album("Blunderbuss", "Blues Rock", 2012, artist_5)
album_6 = Album("Lazaretto", "Rock", 2014, artist_5)
album_7 = Album("Boarding House Reach", "Experimental", 2018, artist_5)

# artist_repository.delete_all() - for testing for dropping the table gives repeatable reliable tests ID's

# ADD SOME ARTISTS
artist_repository.save(artist_1)
artist_repository.save(artist_2)
artist_repository.save(artist_3)
artist_repository.save(artist_5)

# ADD SOME ALBUMBS WITH ARTISTS

album_repository.save(album_1)
album_repository.save(album_2)
album_repository.save(album_3)
album_repository.save(album_5)
album_repository.save(album_6)
album_repository.save(album_7)


# CHECK I CAN SELECT ALL AND PRINT THE LIST.__DICT__
artists = artist_repository.select_all()
print(len(artists))
for artist in artists:
    print(artist.__dict__)

print("--------------------------")

# CREATED A SEARCH BY NAME FOR FUNSIES AND ALSO CHECK THE DELETE BY ID HERE
first_name_results = artist_repository.select_by_first_name("Iggy")
for artist in first_name_results:
    artist_repository.delete_id(artist.id)

artists = artist_repository.select_all()
print(len(artists))
for artist in artists:
    print(artist.__dict__)

print("--------------------------")

# LOAD IN AN ARTIST BY ID
artist_to_change = artist_repository.select_id(1)
# CHANGE THE DETAILS IN THE OBJECT
artist_to_change.first_name = "George"
# UPDATE IT IN THE DATABASE
artist_repository.update(artist_to_change)

print("--------------------------")

# SANITY CHECK TO PRINT OUT WHAT IM DOING
artists = artist_repository.select_all()
print(len(artists))
for artist in artists:
    print(artist.__dict__)

albums = album_repository.select_all()
print(len(albums))
for album in albums:
    print(album.__dict__)

print("--------------------------")


# CHECK AND PRINT ALBUM BY ARTIST
albums_by_artist_search = album_repository.albums_by_artist(artist_5)
print(len(albums_by_artist_search))
for album in albums_by_artist_search:
    print(album.__dict__)


# DELETE ONE JACK WHITE ALBUM
album_repository.delete_id(4)

print("--------------------------")
# CHECK ALBUM WAS DELETED
albums_by_artist_search = album_repository.albums_by_artist(artist_5)
print(len(albums_by_artist_search))
for album in albums_by_artist_search:
    print(album.__dict__)
