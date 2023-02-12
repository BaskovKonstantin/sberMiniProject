import sqlite3
from random import randint
from faker import Faker

def populate_table(conn, table_name, num_rows):
    c = conn.cursor()
    fake = Faker()

    for i in range(num_rows):
        if table_name == 'books':
            title = fake.sentence(nb_words=3, variable_nb_words=True, ext_word_list=None)
            author = fake.name()
            publication_date = fake.date_between(start_date='-100y', end_date='today').strftime('%Y-%m-%d')
            pages = randint(100, 1000)
            rating = round(fake.random_number(digits=1) + fake.random_number(digits=1) / 10, 1)
            c.execute(
                f"INSERT INTO books (title, author, publication_date, pages, rating) VALUES ('{title}', '{author}', '{publication_date}', {pages}, {rating})")

        if table_name == 'movies':
            title = fake.sentence(nb_words=3, variable_nb_words=True, ext_word_list=None)
            director = fake.name()
            release_date = fake.date_between(start_date='-100y', end_date='today').strftime('%Y-%m-%d')
            duration = randint(60, 180)
            rating = round(fake.random_number(digits=1) + fake.random_number(digits=1) / 10, 1)
            c.execute(
                f"INSERT INTO movies (title, director, release_date, duration, rating) VALUES ('{title}', '{director}', '{release_date}', {duration}, {rating})")

        if table_name == 'albums':
            title = fake.sentence(nb_words=3, variable_nb_words=True, ext_word_list=None)
            artist = fake.name()
            release_date = fake.date_between(start_date='-100y', end_date='today').strftime('%Y-%m-%d')
            tracks = randint(5, 20)
            rating = round(fake.random_number(digits=1) + fake.random_number(digits=1) / 10, 1)
            c.execute(
                f"INSERT INTO albums (title, artist, release_date, tracks, rating) VALUES ('{title}', '{artist}', '{release_date}', {tracks}, {rating})")

    print(f"{num_rows} rows inserted into {table_name} table successfully")
    conn.commit()

def create_table(conn):
    c = conn.cursor()
    c.execute('''
        CREATE TABLE books (
            id INTEGER PRIMARY KEY,
            title TEXT NOT NULL,
            author TEXT NOT NULL,
            publication_date TEXT NOT NULL,
            pages INTEGER NOT NULL,
            rating REAL NOT NULL
        )
    ''')
    c.execute('''
        CREATE TABLE movies (
            id INTEGER PRIMARY KEY,
            title TEXT NOT NULL,
            director TEXT NOT NULL,
            release_date TEXT NOT NULL,
            duration INTEGER NOT NULL,
            rating REAL NOT NULL
        )
    ''')
    c.execute('''
        CREATE TABLE albums (
            id INTEGER PRIMARY KEY,
            title TEXT NOT NULL,
            artist TEXT NOT NULL,
            release_date TEXT NOT NULL,
            tracks INTEGER NOT NULL,
            rating REAL NOT NULL
        )
    ''')
    print("Tables created successfully")
    conn.commit()

def main():
    conn = sqlite3.connect('entertainment.db')
    create_table(conn)
    populate_table(conn, 'books', 50)
    populate_table(conn, 'movies', 50)
    populate_table(conn, 'albums', 50)
    conn.close()

if __name__ == '__main__':
    main()