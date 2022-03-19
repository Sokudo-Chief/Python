import logging
from multiprocessing.sharedctypes import Value
from os import execlp
from select import select
from aiogram import Bot, Dispatcher, executor, types
import books as b
import logs as l
import visitors as v

API_TOKEN = '5139167255:AAH2Us5ha8MxcrW-UTaetjk-oxgVcqlVagw'

logging.basicConfig(level=logging.INFO)

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

# ================================== Приветствие ====================================

@dp.message_handler(commands=['start', 'help'])
async def welcome(message: types.Message):
    await message.reply("Йоу я бот, мой владелец - @Sokudo_Chief.")

# ================================== Вывод посетителей ====================================

@dp.message_handler(commands=['visitors'])
async def send_visitors(message: types.Message):
    visitors = v.SelectTable()
    answer = ''
    for visitor in visitors:
        answer = answer + str(visitor[0]) + ' ' + visitor[1] + ' ' + visitor[2] + ' ' + visitor[3] + '\n'
    print(answer)
    await message.reply(answer[:-1])

# ================================== Вывод книг ====================================

@dp.message_handler(commands=['books'])
async def send_books(message: types.Message):
    books = b.SelectTable()
    answer = ''
    for book in books:
        answer = answer + str(book[0]) + ' ' + book[1] + ' ' + book[2] + ' ' + str(book[3]) + '\n'
    print(answer)
    await message.reply(answer[:-1])

# ================================== Вывод записанных книг ====================================

@dp.message_handler(commands=['library'])
async def library(message: types.Message):
    visitors = v.SelectTable()
    answer = ''

    try:

        for visitor in visitors:
            
            visitor = v.recordNumber(visitor[0])
            sLogs = l.selectLogs(visitor)
            answer = answer + sLogs[0][1] + ': ' 

            for book in sLogs:
                kniga = b.recordID(book[4])[0][1]
                answer = answer + str(kniga) + '; '

            answer = answer + '\n'

    except IndexError:
        answer = answer + str(visitor[0][1]) + ': книг нет.\n'
    await message.reply(answer)

# ================================== Вывод записанных книг у читателя ====================================

@dp.message_handler(lambda message: message.text.startswith("/biv "))
async def library(message: types.Message):
    parsed_message = message.text.split(' ')

    answer = ''
    try:

        visitor = v.recordNumber(parsed_message[1])
        sLogs = l.selectLogs(visitor)
        answer = answer + sLogs[0][1] + ': '

        for book in sLogs:
            kniga = b.recordID(book[4])[0][1]
            answer = answer + str(kniga) + '; '

    except IndexError:
        answer = answer + str(visitor[0][1]) + ': книг нет.\n'
    
    await message.reply(answer)

# ================================== Удалениие книги у читателя ====================================

@dp.message_handler(lambda message: message.text.startswith("/db "))
async def library(message: types.Message):
    parsed_message = message.text[4:].split(' ')

    l.delete(int(parsed_message[0]))
    await message.reply('Книга успешно удалена.')

# ================================== Удаление посетителя ====================================

@dp.message_handler(lambda message: message.text.startswith("/delVisitor "))
async def delete_visitor(message: types.Message):
    try:
        parsed_message = message.text[12:].split(' ')
        v.delete(int(parsed_message[0]))
        await message.answer('Посетитель успешно удалён')
    except ValueError:
        await message.reply("Некорректное сообщение. Пример: /delVisitor Айди")

# ================================== Удаление книги ====================================

@dp.message_handler(lambda message: message.text.startswith("/delBook "))
async def delete_book(message: types.Message):
    try:
        parsed_message = message.text[9:].split(' ')
        b.delete(int(parsed_message[0]))
        await message.answer('Книга успешна удалена')
    except ValueError:
        await message.reply("Некорректное сообщение. Пример: /delBook Айди")

# ================================== Добавление посетителя ====================================

@dp.message_handler(lambda message: message.text.startswith("/addVisitor "))
async def add_visitor(message: types.Message):
    try:
        parsed_message = message.text.split(' ')
        records = [(parsed_message[1], parsed_message[2], parsed_message[3], parsed_message[4])]
        v.insert(records)
        await message.answer("Посетитель добавлен.")
    except ValueError:
        await message.reply("Некорректное сообщение.")

# ================================== Добавление книги ====================================

@dp.message_handler(lambda message: message.text.startswith("/addBook "))
async def add_book(message: types.Message):
    parsed_message = message.text.split(' ')
    b.insert(parsed_message[1], parsed_message[2], parsed_message[3])
    await message.answer("Книга добавлена.")

# ================================== Поиск посетителя ====================================

@dp.message_handler(lambda message: message.text.startswith("/sVisitor "))
async def search_visitor(message: types.Message):
    parsed_message = message.text.split(' ')
    await message.answer(v.recordNumber(parsed_message[1]))

# ================================== Поиск книги ====================================

@dp.message_handler(lambda message: message.text.startswith("/sBook "))
async def search_book(message: types.Message):
    parsed_message = message.text.split(' ')
    await message.answer(b.recordID(parsed_message[1]))

# ================================== Редактирование посетителя ====================================

@dp.message_handler(lambda message: message.text.startswith("/updVisitor "))
async def update_visitor(message: types.Message):
    parsed_message = message.text.split(' ')
    v.update(parsed_message[1], parsed_message[2], parsed_message[3], parsed_message[4])
    await message.reply("Посетитель отредактирован.")

# ================================== Редактирование книги ====================================

@dp.message_handler(lambda message: message.text.startswith("/updBook "))
async def update_book(message: types.Message):
    parsed_message = message.text.split(' ')
    b.update(parsed_message[1], parsed_message[2], parsed_message[3], parsed_message[4])
    await message.reply("Посетитель отредактирован.")

# ================================== Добавление книги к посетителю ====================================

@dp.message_handler(lambda message: message.text.startswith("/add_book "))
async def add_book(message: types.Message):
    parsed_message = message.text.split(' ')
    try:
        visitor = v.recordNumber(parsed_message[1])
        book = b.recordID(parsed_message[2])[0]
        l.addBook(book, visitor)
    except:
        await message.answer('Введите по примеру, пример: Number Id')
    await message.answer("Книга добавлена.")

# ================================== Удаление книги добавленную к посетителю ====================================



# ================================== Редактирование книги добавленную к посетителю ====================================



# ================================== Запуск ====================================

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)