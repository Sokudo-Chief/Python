compnum = 50
at = 0
answer = int(input('Число:'))

while answer != compnum:
    if answer < compnum:
        print('Больше')
    elif answer > compnum:
        print('Меньше')
    answer = int(input('Введите новое число:'))
    at = at + 1

print('Well done you took', at, 'attempts')