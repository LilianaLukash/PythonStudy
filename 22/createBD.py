import random
import sqlite3
import string
import time
from datetime import datetime


db = sqlite3.connect('../my.sqlite')
curr = db.cursor()
table_tusers = ("CREATE TABLE IF NOT EXISTS tusers "
                "( user_id integer primary key autoincrement, first_name TEXT, "
                "last_name TEXT, age INTEGER default 18)")

table_phouse = ("CREATE TABLE IF NOT EXISTS publishing_house "
                "( pub_id integer primary key autoincrement, name TEXT, "
                "rating INTEGER default 5)")

table_books = ("CREATE TABLE IF NOT EXISTS books  "
                "( b_id integer primary key autoincrement, title TEXT, "
               "author TEXT, year INTEGER, price REAL, publishing_house_id INTEGER, "
               "FOREIGN KEY (publishing_house_id) references publishing_house(pub_id))")

table_purchases = ("CREATE TABLE IF NOT EXISTS purchases  "
                "( purch_id integer primary key autoincrement, user_id INTEGER, book_id integer, "
                   " p_data REAL, FOREIGN KEY (user_id) REFERENCES tusers(user_id), "
                   "FOREIGN KEY (book_id) REFERENCES tusers(user_id))")

curr.execute(table_tusers)
curr.execute(table_phouse)
curr.execute(table_books)
curr.execute(table_purchases)

first_name_list = [ "Ira", "Angela","Ivan", "George", "Max", "Alex"]
last_name_list = ["Ivanov","Sidorov","London","Maxwell","Jordan",'Sousa',"Lukash"]
publishing_house_list = ['Paranoia puplicis', 'Fake news', 'Last choice', 'Porno star']
book_title_list = ['My life', 'How to earn a million', 'How to say No', 'Exciting night']
author_list = ['Lenin', 'Jack London', 'Adolf Hitler', 'Lois Budjold', 'Asimov', 'Lulu']

# tusers = []
# for x in first_name_list:
#     for n in last_name_list:
#         k = random.randint(18,79)
#         tusers.append((x, n, k))
# print(tusers)
# curr.executemany("INSERT INTO tusers(first_name, last_name, age) VALUES (?,?,?)", tusers)
# db.commit()

# publishing_house = []
# for n in publishing_house_list:
#     k = random.randint(1, 5)
#     publishing_house.append((n, k))
# print(publishing_house)
# curr.executemany("INSERT INTO publishing_house(name, rating) VALUES (?,?)", publishing_house)
# db.commit()

# title TEXT, "author TEXT, year INTEGER, price REAL, publishing_house_id INTEGER,
# books = []
# for n in book_title_list:
#     for t in author_list:
#         books.append((n, t, (random.randint(1900,2023)), random.randint(20,100), random.randint(1,5)))
# print(books)
# curr.executemany("INSERT INTO books(title, author, year, price, publishing_house_id) VALUES (?,?,?,?,?)", books)
# db.commit()

# user_id INTEGER, book_id integer, "" p_data REAL
# current_dateTime = datetime.now()
# purchases = []
# for _ in range(20):
#     purchases.append((random.randint(1,42), random.randint(1,42), current_dateTime.day))
# curr.executemany("INSERT INTO purchases(user_id, book_id, p_data) VALUES (?,?,?)", purchases)
# db.commit()
curr.executemany("SELECT  purchases.p_data, tusers.first_name "
                 "FROM purchases, tusers JOIN purchases "
                 "ON tusers.user_id = purchases.user_id")