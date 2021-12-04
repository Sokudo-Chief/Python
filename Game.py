import random

class Hero:
    def __init__(self):
        self.__power = 25
        print("Герой вошёл в комнату, в которой 10 дверей")
    
    def buff(self, buff):
        self.__power += buff
        print("Герой получил усиление на", buff)

    def power(self):
        return self.__power



class Artefact:
    def __init__(self):
        self.__power = random.randint(10, 80)
        print("В этой комнате был артефакт с силой", self.__power)

    def power(self):
        return self.__power



class Monster:
    def __init__(self):
        self.__power = random.randint(5, 100)
        print("В этой комнате был монстр с силой", self.__power)

    def power(self):
        return self.__power



door = [random.randint(0, 1) for i in range(10)]
hero = Hero()



for i in range(10):
    choise = int(input("Выберите дверь:"))
    if door[choise - 1] == 0:
        artefact = Artefact()
        hero.buff(artefact.power())
    else:
        monster = Monster()
        if hero.power() >= monster.power():
            print("Вы выиграли в этой битве")
        else:
            print("Вы проиграли")
            exit()
print("Вы выиграли!")