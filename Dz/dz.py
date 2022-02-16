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
def createTable2():
    try:
        sqlite_connection = sqlite3.connect("visitors.db")
        cursor = sqlite_connection.cursor()
        print("База данных успешно подключена.")

        create_table = '''CREATE TABLE visitors (
                            ID INTEGER PRIMARY KEY,
                            number INTEGER NOT NULL,
                            name TEXT NOT NULL,
                            surname TEXT NOT NULL,
                            adress TEXT NOT NULL);'''
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
def insertVisitors(records):
    try:
        sqlite_connection = sqlite3.connect('visitors.db')
        cursor = sqlite_connection.cursor()
        print('База данных подключена.')

        insert_query = '''INSERT INTO visitors (id, number, name, surname, adress)
                            VALUES (?, ?, ?, ?, ?);'''               
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
def makingRecords():
    records = []
    while True:
        records.append((
            maxID() + 1,
            int(input('Номер: ')),
            input('Имя: '),
            input('Фамилия: '),
            input('Адресс: ')
        ))
        question = input('Выйти? y/n: ')
        if question == 'y':
            return records
def recordAuthor(author):
    try:
        sqlite_connection = sqlite3.connect('baze.db')
        cursor = sqlite_connection.cursor()
        print('База данных подкючена.')

        sqlite_selection_query = "SELECT * From books WHERE author=?Max;"
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
def SelectRecords(author, toms):
    try:
        sqlite_connection = sqlite3.connect('baze.db')
        cursor = sqlite_connection.cursor()
        print('База данных подкючена.')

        sqlite_selection_query = "SELECT * FROM books WHERE author=? AND toms=?;"
        cursor.execute(sqlite_selection_query, (author, toms))
        record = cursor.fetchall()
        cursor.close()
        return record
    except sqlite3.Error as error:
        print("Не удалось выбрать данные из таблицы.", error)
    finally:
        if sqlite_connection:
            sqlite_connection.close()
            print("Соединение с SQLite закрыто")
def printV(visitors):
    try:
        for visitor in visitors:
            print()
            print("ID:", visitor[0])
            print("number:", visitor[1])
            print("name:", visitor[2])
            print("surname:", visitor[3])
            print("Adress:", visitor[4])
    except sqlite3.Error as error:
        print("Ничего не выбрано!")     
def recordID(id):
    try:
        sqlite_connection = sqlite3.connect('visitors.db')
        cursor = sqlite_connection.cursor()

        sqlite_selection_query = "SELECT * FROM visitors WHERE id=?;"
        cursor.execute(sqlite_selection_query, (id,))
        record = cursor.fetchall()
        cursor.close()
        return record
    except sqlite3.Error as error:
        print("Не удалось выбрать данные из таблицы.", error)
    finally:
        if sqlite_connection:
            sqlite_connection.close()
def recordName1(name):
    try:
        sqlite_connection = sqlite3.connect('visitors.db')
        cursor = sqlite_connection.cursor()

        sqlite_selection_query = "SELECT * FROM visitors WHERE name=?;"
        cursor.execute(sqlite_selection_query, (name,))
        record = cursor.fetchall()
        cursor.close()
        return record
    except sqlite3.Error as error:
        print("Не удалось выбрать данные из таблицы.", error)
    finally:
        if sqlite_connection:
            sqlite_connection.close()
def recordSurname(surname):
    try:
        sqlite_connection = sqlite3.connect('visitors.db')
        cursor = sqlite_connection.cursor()

        sqlite_selection_query = "SELECT * FROM visitors WHERE surname=?;"
        cursor.execute(sqlite_selection_query, (surname,))
        record = cursor.fetchall()
        cursor.close()
        return record
    except sqlite3.Error as error:
        print("Не удалось выбрать данные из таблицы.", error)
    finally:
        if sqlite_connection:
            sqlite_connection.close()
def recordAdress(adress):
    try:
        sqlite_connection = sqlite3.connect('visitors.db')
        cursor = sqlite_connection.cursor()

        sqlite_selection_query = "SELECT * FROM visitors WHERE adress=?;"
        cursor.execute(sqlite_selection_query, (adress,))
        record = cursor.fetchall()
        cursor.close()
        return record
    except sqlite3.Error as error:
        print("Не удалось выбрать данные из таблицы.", error)
    finally:
        if sqlite_connection:
            sqlite_connection.close()
def recordNumber(number):
    try:
        sqlite_connection = sqlite3.connect('visitors.db')
        cursor = sqlite_connection.cursor()

        sqlite_selection_query = "SELECT * FROM visitors WHERE number=?;"
        cursor.execute(sqlite_selection_query, (number,))
        record = cursor.fetchall()
        cursor.close()
        return record
    except sqlite3.Error as error:
        print("Не удалось выбрать данные из таблицы.", error)
    finally:
        if sqlite_connection:
            sqlite_connection.close()
def delete(id):
    try:
        sqlite_connection = sqlite3.connect('visitors.db')
        cursor = sqlite_connection.cursor()

        sqlite_delete_query = "DELETE FROM visitors WHERE id=?;"
        cursor.execute(sqlite_delete_query, (id,))
        sqlite_connection.commit()
        print("Запись", id, "успешна удалена.")
        cursor.close()
    except sqlite3.Error as error:
        print("Не удалось выбрать данные из таблицы.", error)
    finally:
        if sqlite_connection:
            sqlite_connection.close()
            print("Соединение с SQLite закрыто")
def updateNumber(number, id):
    try:
        sqlite_connection = sqlite3.connect("visitors.db")
        cursor = sqlite_connection.cursor()

        sqlite_selection_query = "UPDATE visitors SET number=? WHERE ID=?;"
        cursor.execute(sqlite_selection_query, (number, id))
        sqlite_connection.commit()
        print("Запись", id, "успешна обновлена.")
        cursor.close
        
    except sqlite3.Error as error:
        print("Не удалось изменить данные из таблицы.", error)
    finally:
        if sqlite_connection:
            sqlite_connection.close()
def updateName(name, id):
    try:
        sqlite_connection = sqlite3.connect("visitors.db")
        cursor = sqlite_connection.cursor()

        sqlite_selection_query = "UPDATE visitors SET name=? WHERE ID=?;"
        cursor.execute(sqlite_selection_query, (name, id))
        sqlite_connection.commit()
        print("Запись", id, "успешна обновлена.")
        cursor.close
    except sqlite3.Error as error:
        print("Не удалось изменить данные из таблицы.", error)
    finally:
        if sqlite_connection:
            sqlite_connection.close()
def updateSurname(surname, id):
    try:
        sqlite_connection = sqlite3.connect("visitors.db")
        cursor = sqlite_connection.cursor()

        sqlite_selection_query = "UPDATE visitors SET surname=? WHERE ID=?;"
        cursor.execute(sqlite_selection_query, (surname, id))
        sqlite_connection.commit()
        print("Запись", id, "успешна обновлена.")
        cursor.close

    except sqlite3.Error as error:
        print("Не удалось изменить данные из таблицы.", error)
    finally:
        if sqlite_connection:
            sqlite_connection.close()
def updateAdress(adress, id):
    try:
        sqlite_connection = sqlite3.connect("visitors.db")
        cursor = sqlite_connection.cursor()

        sqlite_selection_query = "UPDATE visitors SET adress=? WHERE ID=?;"
        cursor.execute(sqlite_selection_query, (adress, id))
        sqlite_connection.commit()
        print("Запись", id, "успешна обновлена.")
        cursor.close
        
    except sqlite3.Error as error:
        print("Не удалось изменить данные из таблицы.", error)
    finally:
        if sqlite_connection:
            sqlite_connection.close()
def maxID():
    try:
        sqlite_connection = sqlite3.connect('visitors.db')
        cursor = sqlite_connection.cursor()
        print('Соединение с базой данных прошло успешно.')

        sqlite_selection_query = "SELECT MAX(id) FROM visitors;"
        cursor.execute(sqlite_selection_query)
        record = cursor.fetchone()
        cursor.close()
        return record[0]
    except sqlite3.Error as error:
        print("Не удалось выбрать данные из таблицы.", error)
    finally:
        if sqlite_connection:
            sqlite_connection.close()
            print("Соединение с SQLite закрыто")


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


# authorInp = input("Автор: ")
# tomsInp = int(input("Кол-во томов: "))
# nameInp = input("Название: ")

# authorR = recordtAuthor(authorInp)
# tomsR = recordtToms(tomsInp)
# nameR = recordtName(nameInp)

# print()
# print("По автору: ")
# printR(authorR)   

# print("По количеству томов: ")    
# printR(tomsR)

# print("Вывод по названию: ")
# printR(nameR)

# visitors = makingRecords()
# insertVisitors(visitors)

vopros = input("Хотите удалить посетителя? (y/n): ")
if vopros == "y":
    idD = int(input("ID посетителя: "))
    delete(idD)
while True:
    print()
    print("1. Добавление нового посетителя")
    print("2. Редактирование посетителя")
    print("3. Удаление посетителя")
    print("4. Вывод посетителя")
    print()
    vopros3 = int(input("Выберите нужный вариант (1/2/3/4): "))

    if vopros3 == 1:
        visitors = makingRecords()
        insertVisitors(visitors)

    if vopros3 == 2:
        vopros2 = input("Хотите отредактировать посетителя? (y/n): ")
        if vopros2 == "y":
            idI = int(input("ID посетителя: "))
            print("Старые данные:")
            printV(recordID(idI))
            print()
            nameI = input("Новое имя посетителя: ")
            updateName(nameI, idI)
            print()
            surnameI = input("Новую фамилию посетителя: ")
            updateSurname(surnameI, idI)
            print()
            adressI = input("Новый адрес посетителя: ")
            updateAdress(adressI, idI)
            print()
            numberI = input("Новый номер посетителя: ")
            updateNumber(numberI, idI)
            print()
            print("Новые данные:")
            printV(recordID(idI))
            
    if vopros3 == 3:
        vopros = input("Хотите удалить посетителя? (y/n): ")
        if vopros == "y":
            idD = int(input("ID посетителя: "))
            delete(idD)

    if vopros3 == 4:
        nameInp = input("Имя: ")
        surnameInp = input("Фамилия: ")
        adressInp = input("Адрес: ")
        numberInp = int(input("Номер: "))

        nameR = recordName1(nameInp)
        surnameR = recordSurname(surnameInp)
        adressR = recordAdress(adressInp)
        numberR = recordNumber(numberInp)

        print("Вывод по имени: ")
        printV(nameR)
        print("Вывод по фамилии: ")
        printV(surnameR)
        print("Вывод по адресу: ")
        printV(adressR)
        print("Вывод по номеру: ")
        printV(numberR)
