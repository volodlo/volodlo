import random


class Warrior:
    def __init__(self, name, health=100):
        self.name = name
        self.health = health
        print('Создан воин {} со здоровьем {}'.format(self.name, self.health))

    def strike(self, enemyWarrior):
        if True:
            print('Воин {} нанес урон -20 воину {}'.format(self.name, enemyWarrior.name))
            enemyWarrior.setHealth(
                enemyWarrior.getHealth() - 20
            )
        else:
            print('Некорректно задано здоровье для воина {}'.format(enemyWarrior.name))
            print(type(enemyWarrior.getHealth()))

    def setHealth(self, health):
        self.health = health
        print('Установлено здоровье {} для воина {}'.format(self.health, self.name))

    def getHealth(self):
        try:
            return self.health
            print('Здоровье воина {} — {}'.format(self.name, self.health))
        except:
            return 'Здоровье не задано'
            print('Здоровье для воина {} не задано'.format(self.name))


one = Warrior('Математичка', 100)
two = Warrior('Степан', 100)

while (one.health > 0) and (two.health > 0):
    round = random.randint(1, 2)

    if round == 1:
        one.strike(two)
    elif round == 2:
        two.strike(one)

if round == 1:
    name = one.name
    enemy_name = two.name
elif round == 2:
    name = two.name
    enemy_name = one.name

print('Поздравляем воина {}! Он одержал победу над воином {}'.format(name, enemy_name))