# DROP TABLES

songplay_table_drop = "DROP TABLE IF NOT EXISTS songplays;"
user_table_drop = "DROP TABLE IF NOT EXISTS users;"
song_table_drop = "DROP TABLE IF NOT EXISTS songs;"
artist_table_drop = "DROP TABLE IF NOT EXISTS artists;"
time_table_drop = "DROP TABLE IF NOT EXISTS time;"

# CREATE TABLES

songplay_table_create = ("""
    CREATE TABLES IF NOT EXISTS songplays (
        songplay_id int NOT NULL,
        start_time int NOT NULL,
        user_id text NOT NULL,
        level text NOT NULL,
        song_id text NOT NULL,
        artist_id text NOT NULL,
        session_id int NOT NULL,
        location text NOT NULL,
        user_agent text NOT NULL,
        PRIMARY KEY (songplay_id),
        FOREIGN KEY (start_time) REFERENCES time(start_time),
        FOREIGN KEY (user_id) REFERENCES users(user_id),
        FOREIGN KEY (song_id) REFERENCES songs(song_id),
        FOREIGN KEY (artist_id) REFERENCES artists(artist_id)
    );
""")

user_table_create = ("""
    CREATE TABLE IF NOT EXISTS users (
        user_id text NOT NULL,
        first_name text NOT NULL,
        last_name text NOT NULL,
        gender text NOT NULL,
        level text NOT NULL,
        PRIMARY KEY (user_id)
    );
""")

song_table_create = ("""
    CREATE TABLE IF NOT EXISTS songs (
        song_id text NOT NULL,
        title text NOT NULL,
        artist_id text NOT NULL,
        year int NOT NULL,
        duration double precicion NOT NULL,
        PRIMARY KEY (song_id)
    );
""")

artist_table_create = ("""
    CREATE TABLE IF NOT EXISTS artists (
        artist_id text NOT NULL,
        name text NOT NULL,
        location text NOT NULL,
        latitude double precision NOT NULL,
        longitude double precision NOT NULL,
        PRIMARY KEY (artist_id)
    );
""")

time_table_create = ("""
    CREATE TABLE IF NOT EXISTS time (
        start_time int NOT NULL,
        hour int NOT NULL,
        day int NOT NULL,
        week int NOT NULL,
        month int NOT NULL,
        year int NOT NULL,
        weekday int NOT NULL,
        PRIMARY KEY (start_time)
    );
""")

# INSERT RECORDS

songplay_table_insert = ("""
""")

user_table_insert = ("""
""")

song_table_insert = ("""
""")

artist_table_insert = ("""
""")


time_table_insert = ("""
""")

# FIND SONGS

song_select = ("""
""")

# QUERY LISTS

create_table_queries = [songplay_table_create, user_table_create, song_table_create, artist_table_create, time_table_create]
drop_table_queries = [songplay_table_drop, user_table_drop, song_table_drop, artist_table_drop, time_table_drop]