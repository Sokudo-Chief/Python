import sqlite3

def sqliteVersion():
    try:
        sqlite_connection = sqlite3.connect("baze.db")
        cursor = sqlite_connection.cursor()
        print("База данных успешно подключена.")

        sqlite_select_version_query = "SELECT sqlite_version();"
        cursor.execute(sqlite_select_version_query)
        record = cursor.fetchall()
        print("Версия SQLite:", record[0][0])
        cursor.close()
    except sqlite3.Error as error:
        print("Ошибка при подключении к SQLite:", error)
    finally:
        if sqlite_connection:
            sqlite_connection.close()
            print("Соединение с SQLite закрыто.")

def createTable():
    try:
        sqlite_connection = sqlite3.connect("baze.db")
        cursor = sqlite_connection.cursor()
        print("База данных успешно подключена.")

        create_table = '''CREATE TABLE books (
                            id INTEGER PRIMARY KEY,
                            name TEXT NOT NULL,
                            author TEXT NOT NULL,
                            toms INTEGER NOT NULL);'''
        cursor.execute(create_table)
        sqlite_connection.commit()
        print("Таблица создана.")
        cursor.close()
    except sqlite3.Error as error:
        print("Ошибка при подключении к SQLite:", error)
    finally:
        if sqlite_connection:
            sqlite_connection.close()
            print("Соединение с SQLite закрыто.")

def recordtAuthor(author):
    try:
        sqlite_connection = sqlite3.connect('baze.db')
        cursor = sqlite_connection.cursor()
        print('База данных подкючена.')

        sqlite_selection_query = "SELECT * FROM books WHERE author=?;"
        cursor.execute(sqlite_selection_query, (author,))
        record = cursor.fetchall()
        cursor.close()
        return record
    except sqlite3.Error as error:
        print("Не удалось выбрать данные из таблицы.", error)
    finally:
        if sqlite_connection:
            sqlite_connection.close()
            print("Соединение с SQLite закрыто")

def recordtToms(toms):
    try:
        sqlite_connection = sqlite3.connect('baze.db')
        cursor = sqlite_connection.cursor()
        print('База данных подкючена.')

        sqlite_selection_query = "SELECT * FROM books WHERE toms=?;"
        cursor.execute(sqlite_selection_query, (toms,))
        record = cursor.fetchall()
        cursor.close()
        return record
    except sqlite3.Error as error:
        print("Не удалось выбрать данные из таблицы.", error)
    finally:
        if sqlite_connection:
            sqlite_connection.close()
            print("Соединение с SQLite закрыто")

def recordtName(name):
    try:
        sqlite_connection = sqlite3.connect('baze.db')
        cursor = sqlite_connection.cursor()
        print('База данных подкючена.')

        sqlite_selection_query = "SELECT * FROM books WHERE name=?;"
        cursor.execute(sqlite_selection_query, (name,))
        record = cursor.fetchall()
        cursor.close()
        return record
    except sqlite3.Error as error:
        print("Не удалось выбрать данные из таблицы.", error)
    finally:
        if sqlite_connection:
            sqlite_connection.close()
            print("Соединение с SQLite закрыто")

def insert(records):
    try:
        sqlite_connection = sqlite3.connect('baze.db')
        cursor = sqlite_connection.cursor()
        print('База данных подключена.')

        insert_query = '''INSERT INTO books (id, name, author, toms)
                            VALUES (?, ?, ?, ?);'''               
        cursor.executemany(insert_query, records)
        sqlite_connection.commit()
        print('Запись успешно добавлена.')
        cursor.close()
    except sqlite3.Error as error:
        print("Ошибка при подключении к SQlite", error)
    finally:
        if sqlite_connection:
            sqlite_connection.close()
            print("Соединение с SQLite закрыто")

def SelectTable():
    try:
        sqlite_connection = sqlite3.connect('baze.db')
        cursor = sqlite_connection.cursor()
        print('База данных подкючена.')

        sqlite_selection_query = "SELECT * From books;"
        cursor.execute(sqlite_selection_query)
        record = cursor.fetchall()
        cursor.close()
        return record
    except sqlite3.Error as error:
        print("Не удалось выбрать данные из таблицы.", error)
    finally:
        if sqlite_connection:
            sqlite_connection.close()
            print("Соединение с SQLite закрыто")

def printR(records):
    try:
        for record in records:
            print()
            print("ID:", record[0])
            print("Name:", record[1])
            print("Author:", record[2])
            print("Toms:", record[3])
    except sqlite3.Error as error:
        print("Ничего не выбрано!")       

# def recordAuthor(author):
#     try:
#         sqlite_connection = sqlite3.connect('baze.db')
#         cursor = sqlite_connection.cursor()
#         print('База данных подкючена.')

#         sqlite_selection_query = "SELECT * From books WHERE author=?Max;"
#         cursor.execute(sqlite_selection_query, (author,))
#         record = cursor.fetchall()
#         cursor.close()
#         return record
#     except sqlite3.Error as error:
#         print("Не удалось выбрать данные из таблицы.", error)
#     finally:
#         if sqlite_connection:
#             sqlite_connection.close()
#             print("Соединение с SQLite закрыто")

# def SelectRecords(author, toms):
#     try:
#         sqlite_connection = sqlite3.connect('baze.db')
#         cursor = sqlite_connection.cursor()
#         print('База данных подкючена.')

#         sqlite_selection_query = "SELECT * FROM books WHERE author=? AND toms=?;"
#         cursor.execute(sqlite_selection_query, (author, toms))
#         record = cursor.fetchall()
#         cursor.close()
#         return record
#     except sqlite3.Error as error:
#         print("Не удалось выбрать данные из таблицы.", error)
#     finally:
#         if sqlite_connection:
#             sqlite_connection.close()
#             print("Соединение с SQLite закрыто")


#books = [(1, 'Liver', 'Sokolov', 5),
#        (2, 'Toxic', 'Sokolov', 2),
#        (3, 'Friendly', 'Sokolov', 1),
#        (4, 'PC', 'Max', 3),
#        (5, 'Micro', 'Max', 6),
#        (6, 'Adom', 'Maximov', 8),
#        (7, 'Picture', 'Maximov', 8),
#        (8, 'Home', 'Popusk', 4),
#        (9, 'Sun', 'Popusk', 1),
#        (10, 'Bihand', 'Point', 7),
#        (11, 'Table', 'Point', 9),
#        (12, 'About me', 'Nitro', 2),
#        (13, 'Window', 'Nitro', 1),
#        (14, 'Door', 'Cooler', 1),
#        (15, 'Okey, go!', 'Cooler', 6),]



authorInp = input("Автор: ")
tomsInp = int(input("Кол-во томов: "))
nameInp = input("Название: ")

authorR = recordtAuthor(authorInp)
tomsR = recordtToms(tomsInp)
nameR = recordtName(nameInp)

print()
print("По автору: ")
printR(authorR)   

print("По количеству томов: ")    
printR(tomsR)

print("Вывод по названию: ")
printR(nameR)