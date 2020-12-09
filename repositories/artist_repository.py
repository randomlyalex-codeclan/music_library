from db.run_sql import run_sql

from models.album import Album
from models.artist import Artist


def save(artist):
    sql = "INSERT INTO artists (first_name, last_name) VALUES (%s, %s) RETURNING *"
    values = [artist.first_name, artist.last_name]
    results = run_sql(sql, values)
    id = results[0]['id']
    artist.id = id
    return artist


def delete_all():
    sql = "DELETE FROM artists"
    run_sql(sql)


def delete_id(id):
    sql = "DELETE FROM artists WHERE id = %s"
    values = [id]
    run_sql(sql, values)


def select_all():
    artists = []

    sql = "SELECT * FROM artists"
    results = run_sql(sql)

    for row in results:
        artist = Artist(row['first_name'], row['last_name'],
                        row['stage_name'], row['place_of_birth'], row['id'])
        artists.append(artist)
    return artists


def select_id(id):
    artist = None
    sql = "SELECT * FROM artists WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]

    if result != None:
        artist = Artist(result['first_name'],
                        result['last_name'], result['stage_name'], result['place_of_birth'], result['id'])
    return artist


def select_by_first_name(first_name):
    artists = []

    sql = "SELECT * FROM artists WHERE first_name = %s"
    values = [first_name]
    results = run_sql(sql, values)

    for row in results:
        artist = Artist(row['first_name'], row['last_name'],
                        row['stage_name'], row['place_of_birth'], row['id'])
        artists.append(artist)
    return artists


def update(artist):
    sql = "UPDATE artists SET (first_name, last_name) = (%s, %s) WHERE id = (%s)"
    values = [artist.first_name, artist.last_name, artist.id]
    run_sql(sql, values)



