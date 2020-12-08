DROP TABLE IF EXISTS artists;

DROP TABLE IF EXISTS albums;

CREATE TABLE artists (
    id serial PRIMARY KEY,
    first_name varchar(255),
    last_name varchar(255),
    dob date,
    stage_name varchar(255),
    place_of_birthvarchar (255)
);

CREATE TABLE album (
    id serial PRIMARY KEY,
    title varchar(255),
    genre varchar(255),
    tracklist text,
    runtime int,
    artist_id int REFERENCES artists (id)
);

