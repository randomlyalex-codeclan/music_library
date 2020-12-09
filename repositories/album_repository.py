from db.run_sql import run_sql

from models.album import Album
from models.artist import Artist

import repositories.artist_repository as artist_repository


def save(album):
    sql = "INSERT INTO albums (title, genre, release_year, artist_id) VALUES (%s, %s, %s, %s) RETURNING *"
    values = [album.title, album.genre, album.release_year, album.artist.id]
    results = run_sql(sql, values)
    id = results[0]['id']
    album.id = id
    return album


def delete_all():
    sql = "DELETE FROM albums"
    run_sql(sql)


def delete_id(id):
    sql = "DELETE FROM albums WHERE id = %s"
    values = [id]
    run_sql(sql, values)


def select_all():
    albums = []

    sql = "SELECT * FROM albums"
    results = run_sql(sql)

    for row in results:
        artist = artist_repository.select_id(row['artist_id'])
        album = Album(row['title'], row['genre'],
                      row['release_year'], artist, row['id'])
        albums.append(album)
    return albums


def select_id(id):
    album = None
    sql = "SELECT * FROM albums WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]

    if result != None:
        artist = artist_repository.select_id(result['artist_id'])
        album = Album(result['title'], result['genre'],
                      result['release_year'], artist, result['id'])
    return album


def albums_by_artist(artist):
    albums = []
    sql = "SELECT * FROM albums WHERE artist_id = %s"
    values = [artist.id]
    results = run_sql(sql, values)

    for row in results:
        album = Album(row['title'], row['genre'],
                      row['release_year'], artist, row['id'])
        albums.append(album)
    return albums
