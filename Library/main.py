import sqlite3
import visitors
import books
import logs

def script(name_file):
    try:
        sqlite_connection = sqlite3.connect("library.db")
        cursor = sqlite_connection.cursor()
        try:
            with open(name_file, 'r') as file:
                sql_script = file.read()
        except Exception as error:
            if sqlite_connection:
                cursor.close()
            exit(error)
        cursor.executescript(sql_script)
        sqlite_connection.commit()
        print("Скрипт выполнен успешно.")
        cursor.close()
    except sqlite3.Error as error:
        print("Ошибка при подключении к SQLite:", error)
    finally:
        if sqlite_connection:
            sqlite_connection.close()
            print("Соединение с SQLite закрыто.")


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

# class Вывод:
#     while True:
#         print()
#         print("1. Добавление нового посетителя")
#         print("2. Редактирование посетителя")
#         print("3. Удаление посетителя")
#         print("4. Вывод посетителя")
#         print()
#         vopros = int(input("Выберите нужный вариант (1/2/3/4): "))

#         if vopros == 1:
#             vis = visitors.makingRecords()
#             visitors.insert(vis)

#         if vopros == 2:
#             idI = int(input("ID посетителя: "))
#             print("Старые данные:")
#             visitors.print(visitors.recordID(idI))
#             print()
#             nameI = input("Новое имя посетителя: ")
#             visitors.updateName(nameI, idI)
#             print()
#             surnameI = input("Новую фамилию посетителя: ")
#             visitors.updateSurname(surnameI, idI)
#             print()
#             adressI = input("Новый адрес посетителя: ")
#             visitors.updateAdress(adressI, idI)
#             print()
#             numberI = input("Новый номер посетителя: ")
#             visitors.updateNumber(numberI, idI)
#             print()
#             print("Новые данные:")
#             visitors.print(visitors.recordID(idI))
                
#         if vopros == 3:
#             idD = int(input("ID посетителя: "))
#             visitors.delete(idD)

#         if vopros == 4:
#             nameInp = input("Имя: ")
#             surnameInp = input("Фамилия: ")
#             adressInp = input("Адрес: ")
#             numberInp = int(input("Номер: "))

#             nameR = visitors.recordName(nameInp)
#             surnameR = visitors.recordSurname(surnameInp)
#             adressR = visitors.recordAdress(adressInp)
#             numberR = visitors.recordNumber(numberInp)

#             print("Вывод по имени: ")
#             visitors.print(nameR)
#             print("Вывод по фамилии: ")
#             visitors.print(surnameR)
#             print("Вывод по адресу: ")
#             visitors.print(adressR)
#             print("Вывод по номеру: ")
#             visitors.print(numberR)

# script('create_tables.sql')
# print(visitors.recordNumber(222))
# print(books.recordID(5))

# logs.addBook(books.recordID(12), visitors.recordNumber(555))

print(logs.selectLogs(visitors.recordNumber(333)))