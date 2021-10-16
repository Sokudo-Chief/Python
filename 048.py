answer = 'да'
n = 0

while answer != 'нет':
    name = input('Имя:')
    print(name, 'has been invited')
    n = n + 1
    answer = input('Хотите пригласить кого то ещё?:')

print(n)