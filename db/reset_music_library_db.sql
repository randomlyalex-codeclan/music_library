DROP TABLE IF EXISTS artists, albums CASCADE;

CREATE TABLE artists (
    id serial PRIMARY KEY,
    first_name varchar(255),
    last_name varchar(255),
    dob date,
    stage_name varchar(255),
    place_of_birth varchar(255)
);

CREATE TABLE albums (
    id serial PRIMARY KEY,
    title varchar(255),
    genre varchar(255),
    release_year int,
    tracklist text,
    runtime int,
    artist_id int REFERENCES artists (id)
);

