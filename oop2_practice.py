#!/usr/bin/env python
# coding: utf-8

# ### Инкапсуляция
# 
# Инкапсуляция заключается в том, что данные скрыты за пределами определения объекта. Это позволяет разработчикам создавать удобный интерфейс взаимодействия и защитить данные от доступа извне

# In[ ]:


class Character:
    def __init__(self, name, power, energy=100):
        self.name = name
        self.power = power
        self.energy = energy
        self.backpack = [] 
    
    def eat(self, food):
        if self.energy < 100:
            self.energy += food
        else:
            print("Not hungry")
        
    
    def do_exercise(self, hours):
        if self.energy > 0:
            self.energy -= hours * 2
            self.power += hours * 2
        else:
            print("Too tired")
    
    def change_alias(self, new_alias):
        self.alias = new_alias

    def fight(self, foe):
        if not isinstance(foe, Character): 
            return
        if foe.power < self.power:
            foe.status = "проигравший"
            self.status = "победитель"
        else:
            print("отступить!")


# In[ ]:


# что здесь плохо, как можно "сломать" экземпляр класса?
peter = Character("Peter Parker", 80)
peter.do_exercise(5)
print(peter.power)
print(peter.backpack)

Три модификатора (видимости и доступности) в классе: public, __private, _protected
Защищаем переменную и метод (впереди появится одинарное подчеркивание). Это protected члены класса
# In[ ]:


# реализуем защищенную переменную и метод
class Character:
    def __init__(self, name, power, energy=100):
        self.name = name
        self.power = power
        self.energy = energy
        self._backpack = [] 
    
    def eat(self, food):
        if self.energy < 100:
            self.energy += food
        else:
            print("Not hungry")
    
    def do_exercise(self, hours):
        if self.energy > 0:
            self.energy -= hours * 2
            self.power += hours * 2
        else:
            print("Too tired")
    
    def _change_alias(self, new_alias):
        self.alias = new_alias
    
    def fight(self, foe):
        if not isinstance(foe, Character): 
            return
        if foe.power < self.power:
            foe.status = "проигравший"
            self.status = "победитель"
        else:
            print("отступить!")
            
    

peter = Character('Peter Parker', 80)
peter._change_alias('Spider-Man')
print(peter.alias)
print(peter._backpack)


# На самом деле, технически для интерпретатора это не имеет никакого значения. Это просто соглашение, согласно которому, такие атрибуты и методы не стоит использовать за рамками класса и дочерних классов.

# Модификатор private = Двойное подчеркивание в начале имени атрибута/метода дает большую защиту: атрибут становится недоступным по этому имени вне самого класса.

# In[ ]:


# реализуем приватную переменную и метод

class Character:
    def __init__(self, name, power, energy=100):
        self.name = name
        self.power = power
        self.energy = energy
        self.__backpack = [] 
    
    def eat(self, food):
        if self.energy < 100:
            self.energy += food
        else:
            print("Not hungry")
        
    
    def do_exercise(self, hours):
        if self.energy > 0:
            self.energy -= hours * 2
            self.power += hours * 2
        else:
            print("Too tired")
    
    def __change_alias(self, new_alias):
        self.alias = new_alias

    def fight(self, foe):
        if not isinstance(foe, Character): 
            return
        if foe.power < self.power:
            foe.status = "проигравший"
            self.status = "победитель"
        else:
            print("отступить!")

peter = Character("Peter Parker", 80)
peter.__change_alias("Spider-Man")
print(peter.__backpack)


# Но и это можно обойти при помощи прямого указания класса (пишем имя класса с одинарным подчеркиванием впереди + имя приватного метода или атрибута)

# In[ ]:


peter = Character("Peter Parker", 80)
peter._Character__change_alias("Spider-Man")
print(peter.alias)
print(peter._Character__backpack)


# Таким образом, реализация инкапсуляции в Python носит формальный характер и работает только на уровне соглашения.
# 
# 
# 

# ### Наследование

# In[ ]:


# и сразу реализуем множественное наследование!
# как думаете, почему результаты именно такие?

class Character:
    name = ""
    power = 0
    energy = 100
    hands = 2

class Spider:
    power = 10
    energy = 50
    hands = 8
    
    def webshoot(self):
        print("Pew-Pew!")

        
class SpiderMan(Character, Spider):
    pass


peter_parker = SpiderMan()
print("name", peter_parker.name)
print("power", peter_parker.power)
print("energy", peter_parker.energy)
print("hands", peter_parker.hands)
peter_parker.webshoot()


# Линеаризация - способ представления дерева (графа, дерева) в линейную модель (плоскую структуру, список) для определения порядка наследования.
# **MRO (Method Resolution Order)** - в каком порядке искать атрибуты и методы в цепочке классов

# In[ ]:


print(SpiderMan.mro())


# In[ ]:


# лирическое отступление про наследование и типы
print(isinstance(peter_parker, Character))
print(isinstance(peter_parker, Spider))
print(isinstance(peter_parker, SpiderMan))
print(isinstance(peter_parker, object))
# получаем тип объекта
print(type(peter_parker))
# получаем имя класса объекта
print(type(peter_parker).__name__)


# In[ ]:


# перенесем все в init
# и посмотрим на различие между классами

class Character:
     def __init__(self, name, power, energy=100, hands=2):
        self.name = name
        self.power = power
        self.energy = energy
        self.hands = hands
    

class Spider:
    def __init__(self, power, energy=50, hands=8):
        self.power = power
        self.energy = energy
        self.hands = hands
    
    def webshoot(self):
        print('Pew-Pew!')

        
    
class SpiderMan(Character, Spider):
    def turn_spider_sense(self):
        self.energy -= 10
        self.power += 20

              
        
peter_parker = SpiderMan("Peter Parker", 80)
print("energy", peter_parker.energy)
print("power", peter_parker.power)
print("hands", peter_parker.hands)

peter_parker.turn_spider_sense()

print("energy", peter_parker.energy)
print("power", peter_parker.power)


# ### Полиморфизм
# 
# Полиморфизм позволяет методам с одинаковыми именами реализовывать разную функциональность для разных классов (в т.ч. дочерних).

# In[ ]:


# добавим в наши родительские классы новые методы

class Character:
    def __init__(self, name, power, energy=100, hands=2):
        self.name = name
        self.power = power
        self.energy = energy
        self.hands = hands

    def move(self):
        print("Перемещаюсь")

        
class Spider:
    def __init__(self, power, energy=50, hands=8):
        self.power = power
        self.energy = energy
        self.hands = hands
    
    def webshoot(self):
        print("Pew-Pew!")
    
    def move(self):
        self.webshoot()
        print("Перемещаюсь")

        
    
class SpiderMan(Spider, Character):
    def turn_spider_sense(self):
        self.energy -= 10
        self.power += 20


# In[ ]:


# что выведет метод move()?
peter_parker = SpiderMan('Peter Parker', 80)
peter_parker.move()


# In[ ]:


# пусть наши персонажи "ходят" по-разному
class Character:
    def __init__(self, name, power, energy=100, hands=2):
        self.name = name
        self.power = power
        self.energy = energy
        self.hands = hands

    def move(self):
        print("Перемещаюсь на 2 позиции")

        
class Spider:
    def __init__(self, power, energy=50, hands=8):
        self.power = power
        self.energy = energy
        self.hands = hands
    
    def webshoot(self):
        print('Pew-Pew!')
    
    def move(self):
        self.webshoot()
        print("Перемещаюсь на 1 позицию")

        
    
class SpiderMan(Character, Spider):
    
    def turn_spider_sense(self):
        self.energy -= 10
        self.power += 20
    
    def move(self):
        self.webshoot()
        print("Перемещаюсь на 3 позиции")

        
peter_parker = SpiderMan("Peter Parker", 80)
peter_parker.move()

Как воспользоваться инициализацией (методом __init__) класса-родителя из дочернего класса
# In[ ]:


# инициализация в потомке вручную. а можно ли проще?
class Character:
    def __init__(self, name, power, energy=100, hands=2):
        self.name = name
        self.power = power
        self.energy = energy
        self.hands = hands

    def move(self):
        print("Перемещаюсь на 2 позиции")

        
class Spider:
    def __init__(self, power, energy=50, hands=8):
        self.power = power
        self.energy = energy
        self.hands = hands
    
    def webshoot(self):
        print("Pew-Pew!")
    
    def move(self):
        self.webshoot()
        print("Перемещаюсь на 1 позици.")

        
    
class SpiderMan(Character, Spider):
    # такой вариант допустимый, но зачем нам перезаписывать инициализацию,
    # которая полностью совпадает с родителем?
    def __init__(self, name, power, energy=100, hands=2):
        self.name = name
        self.power = power
        self.energy = energy
        self.hands = hands
        self.backpack = []
    
    def turn_spider_sense(self):
        self.energy -= 10
        self.power += 20

    def move(self):
        self.webshoot()
        print("Перемещаюсь на 3 позиции")

        
peter_parker = SpiderMan("Peter Parker", 80)
print(peter_parker.backpack)


# Функция super() дает доступ к методам родителей!

# In[ ]:


class Character:
    def __init__(self, name, power, energy=100, hands=2):
        self.name = name
        self.power = power
        self.energy = energy
        self.hands = hands

    def move(self):
        print("Перемещаюсь на 2 позиции")

class Spider:
    def __init__(self, power, energy=50, hands=8):
        self.power = power
        self.energy = energy
        self.hands = hands
    
    def webshoot(self):
        print("Pew-Pew!")
    
    def move(self):
        self.webshoot()
        print("Перемещаюсь на 1 позицию")   
    
class SpiderMan(Character, Spider):
    
    # мы полностью наследуем от родителя инициализацию через super, 
    # а потом вручную добавляем новый атрибут для экземпляра (рюкзак)
    def __init__(self, name, power):
        super().__init__(name, power)

        # можно сделать то же самое, явно указав базовый родительский класс Character 
        # (раскомментируйте строку ниже)
        # если вызов метода родителя идет через класс родителя, self первым параметром обязателен! 
#         Character.__init__(self, name, power)

        # мы можем даже вызвать метод инициализации второго, неосновного родителя 
        # (раскомментируйте строку ниже)
#         Spider.__init__(self, 80)
    
        # а вот этот атрибут мы задаем уже только в дочернем классе 
        self.backpack = []
        
    def turn_spider_sense(self):
        self.energy -= 10
        self.power += 20

    def move(self):
        self.webshoot()
        print("Перемещаюсь на 3 позиции")


peter_parker = SpiderMan("Peter Parker", 80)
print(peter_parker.backpack)
print(peter_parker.power)
print(peter_parker.energy)
print(peter_parker.hands)

print(SpiderMan.mro())


# Итак, можно вызвать методы родительского класса:
# 
# 1) через super()
# super().__init__(name, power)
# Тогда self не пишем!
# 
# 2) явно указать базовый родительский класс
# Character.__init__(self, name, power)
# Можно вызывать любого родителя по вашему выбору. Так тоже работает:
# Spider.__init__(self, 80)

# In[ ]:


# чтобы персонаж SpiderMan мог использовать паутину, ее сначала нужно добавить в рюкзак
class Character:
    def __init__(self, name, power, energy=100, hands=2):
        self.name = name
        self.power = power
        self.energy = energy
        self.hands = hands

    def move(self):
        print("Перемещаюсь на 2 позиции")

        
class Spider:
    def __init__(self, power, energy=50, hands=8):
        self.power = power
        self.energy = energy
        self.hands = hands
    
    def webshoot(self):
        print("Pew-Pew!")
    
    def move(self):
        self.webshoot()
        print("Перемещаюсь на 1 позицию")   
    
    
class SpiderMan(Character, Spider):
    def __init__(self, name, power):
        super().__init__(name, power)
        self.backpack = []
        
    def turn_spider_sense(self):
        self.energy -= 10
        self.power += 20
 
    # наш персонаж не может пользоваться паутиной, если ее нет! попробуем исправить
    def webshoot(self):
        if "web" in self.backpack:
            self.webshoot() 
        else:
            print("Нет паутины!")

    def move(self):
        self.webshoot()
        print("Перемещаюсь на 3 позиции")



peter_parker = SpiderMan("Peter Parker", 80)
peter_parker.webshoot()
peter_parker.backpack


# In[ ]:


peter_parker.backpack.append("web")
# что не так в этом коде? почему он выпадает в рекурсию после добавления паутины в рюкзак?
peter_parker.webshoot()


# In[ ]:


# ошибка исправлена - код больше не будет создавать рекурсию.
# см. комментарий у метода SpiderMan.webshoot()
class Character:
    def __init__(self, name, power, energy=100, hands=2):
        self.name = name
        self.power = power
        self.energy = energy
        self.hands = hands

    def move(self):
        print("Перемещаюсь на 2 позиции")

        
class Spider:
    def __init__(self, power, energy=50, hands=8):
        self.power = power
        self.energy = energy
        self.hands = hands
    
    def webshoot(self):
        print('Pew-Pew!')
        print("вызывали Spider.webshoot()")
    
    def move(self):
        self.webshoot()
        print("Перемещаюсь на 1 позицию")   
    
    
class SpiderMan(Character, Spider):
    def __init__(self, name, power):
        super().__init__(name, power)
        self.backpack = []
        
    def turn_spider_sense(self):
        self.energy -= 10
        self.power += 20
    
    # исправляем
    def webshoot(self):
        if "web" in self.backpack:
            # спасибо методу родительского класса - теперь все работает!            
            super().webshoot() 
        else:
            print("Нет паутины!")
        print("вызывали SpiderMan.webshoot()")

    def move(self):
        self.webshoot()
        print("Перемещаюсь на 3 позиции")

        
peter_parker = SpiderMan("Peter Parker", 80)
peter_parker.webshoot()

peter_parker.backpack.append("web")
peter_parker.webshoot()


# Можем ли наследовать что-то не от родителя по mro (по порядку вызова), а от другого родителя?

# In[ ]:


# добавим родительским классам метод fight и проверим, как будет наследоваться

class Character:
    def __init__(self, name, power, energy=100, hands=2):
        self.name = name
        self.power = power
        self.energy = energy
        self.hands = hands

    def move(self):
        print("Перемещаюсь на 2 позиции")
    
# добавили метод
    def fight(self, foe):
        foe.health -= 10
        print("вызывали Character.fight()")
        
        
class Spider:
    def __init__(self, power, energy=50, hands=8):
        self.power = power
        self.energy = energy
        self.hands = hands
    
    def webshoot(self):
        print("Pew-Pew!")
    
    def move(self, foe):
        self.webshoot()
        print("Перемещаюсь на 1 позицию")   
        
    def fight(self, foe):
        if foe.energy < self.energy:
            foe.status = "остановлен"
        else:
            foe.status = "победил"
        print("вызывали Spider.fight()")
    
    
class SpiderMan(Character, Spider):
    def __init__(self, name, power):
        super().__init__(name, power)
        self.backpack = []
        
    def turn_spider_sense(self):
        self.energy -= 10
        self.power += 20
    
    def webshoot(self):
        if "web" in self.backpack:
            super().webshoot() 
        else:
            print("Нет паутины!")

    def move(self):
        self.webshoot()
        print("Перемещаюсь на 3 позиции")
        


# создаем двух персонажей. пусть персонаж класса SpiderMan сразится с персонажем класса Character        
peter_parker = SpiderMan("Peter Parker", 80)
venom = Character("Venom", 10)
venom.health = 100

peter_parker.fight(venom)

print(venom.health)
# в коде ниже будет ошибка - в методе fight класса Character не присваивается status!
# то есть просто так столкнуть Character со SpiderMan не получится...
print(venom.status)


# In[ ]:


# сделаем у дочернего класса SpiderMan свой метод fight
# он будет вызывать методы fight обоих родительских классов
# и поэтому он сможет задать значения обоих атрибутов сразу: health и status

class Character:
    def __init__(self, name, power, energy=100, hands=2):
        self.name = name
        self.power = power
        self.energy = energy
        self.hands = hands

    def move(self):
        print("Перемещаюсь на 2 позиции")
    
    def fight(self, foe):
        foe.energy -= 10
        print("вызывали Character.fight()")
        
        
class Spider:
    def __init__(self, power, energy=50, hands=8):
        self.power = power
        self.energy = energy
        self.hands = hands
    
    def webshoot(self):
        print("Pew-Pew!")
    
    def move(self):
        self.webshoot()
        print("Перемещаюсь на 1 позицию")   
        
    def fight(self, foe):
        if foe.energy < self.energy:
            foe.status = "остановлен"
        else:
            foe.status = "победил"
        print("вызывали Spider.fight()")
    
    
class SpiderMan(Character, Spider):
    def __init__(self, name, power):
        super().__init__(name, power)
        self.backpack = []
        
    def turn_spider_sense(self):
        self.energy -= 10
        self.power += 20
    
    def webshoot(self):
        if "web" in self.backpack:
            super().webshoot() 
        else:
            print("Нет паутины!")

    def move(self, foe):
        self.webshoot()
        print("Перемещаюсь на 3 позиции")
        Spider.fight(self, foe)
        
    # делаем классу свою атаку   
    def fight(self, foe):
        super().fight(foe)
        Spider.fight(self, foe)
        print("вызывали SpiderMan.fight()")
        
peter_parker = SpiderMan("Peter Parker", 80)
venom = Character("Venom", 80)

peter_parker.fight(venom)
print(venom.energy)
print(venom.status)
print()
peter_parker.move(venom)
print(venom.energy)
print(venom.status)


# Магические методы – это общий термин, относящийся к "специальным" методам классов, для которых нет единого определения, поскольку их применение разнообразно. 
# Это те самые методы с двойным подчеркиванием с двух сторон
И мы также можем перегрузить эти магические методы. 
Посмотрим на примере __str__ (выводит информацию о классе в print) и __lt__ (он же оператор <)
# In[ ]:


class Character:
    def __init__(self, name, power, energy=100, hands=2):
        self.name = name
        self.power = power
        self.energy = energy
        self.hands = hands

    def move(self):
        print("Перемещаюсь на 2 позиции")
        
        
class Spider:
    def __init__(self, power, energy=50, hands=8):
        self.power = power
        self.energy = energy
        self.hands = hands
    
    def webshoot(self):
        print("Pew-Pew!")
    
    def move(self):
        self.webshoot()
        print("Перемещаюсь на 1 позицию")   
    
    
class SpiderMan(Character, Spider):
    def __init__(self, name, power):
        super().__init__(name, power)
        self.backpack = []
        
    def turn_spider_sense(self):
        self.energy -= 10
        self.power += 20
    
    def webshoot(self):
        if "web" in self.backpack:
            super().webshoot() 
        else:
            print("Нет паутины!")

    def move(self):
        self.webshoot()
        print("Перемещаюсь на 3 позиции")
        
        
    # добавим возможность сравнения персонажей lesser then <
    # __lt__ __gt__
    # __le__ __ge__
    def __lt__(self, other):
        if not isinstance(other, Character):
            print('Not a Character!')
            return
        return self.power < other.power
    
    # переопределим метод __str__
    # теперь при выполнении print(peter_parker) будет выводиться "Сила персонажа Peter Parker = 80"
    # вместо <__main__.SpiderMan object at 0x00000212D0FA5348>
    def __str__(self):
        res = f"Сила персонажа {self.name} = {self.power}"
        return res
#         return "Привет"

# примерно так работает метод __str__ по умолчанию
#     def __str__(self):
#         return f"<__main__.{type(self).__name__} object at {hex(id(self))}>"
    
    
peter_parker = SpiderMan("Peter Parker", 80)
miles_morales = SpiderMan("Miles Morales", 85)
print(peter_parker)
print(miles_morales)

# __lt__
print(peter_parker < miles_morales)
print(peter_parker.__lt__(miles_morales))
# и даже знак "больше" будет работать!
print(peter_parker > miles_morales)
# а вот метод _gt__ просто так работать не будет
# print(peter_parker.__gt__(miles_morales))


# dir(peter_parker)


# __Дополнение1: Как добавить внешний метод внутрь класса__

# In[ ]:


# внешний метод
def external_can_attack(self, foe):
    if not isinstance(foe, Character):
        print("Not a Character!")
        return
    return self.power > foe.power

class Character:
    def __init__(self, name, power, energy=100, hands=2):
        self.name = name
        self.power = power
        self.energy = energy
        self.hands = hands

    def move(self):
        print("Перемещаюсь на 2 позиции")
    
    def fight(self, foe):
        foe.energy -= 10
        
        
class Spider:
    def __init__(self, power, energy=50, hands=8):
        self.power = power
        self.energy = energy
        self.hands = hands
    
    def webshoot(self):
        print("Pew-Pew!")
    
    def move(self):
        self.webshoot()
        print("Перемещаюсь на 1 позицию")   
        
    def fight(self, foe):
        if foe.energy < self.energy:
            foe.status = "остановлен"
        else:
            foe.status = "победил"
    
    
class SpiderMan(Character, Spider):
    def __init__(self, name, power):
        super().__init__(name, power)
        self.backpack = []
        
    def turn_spider_sense(self):
        self.energy -= 10
        self.power += 20
    
    def webshoot(self):
        if "web" in self.backpack:
            super().webshoot() 
        else:
            print("Нет паутины!")

    def move(self):
        self.webshoot()
        print("Перемещаюсь на 3 позиции")
        
    def fight(self, foe):
        super().fight(foe)
        Spider.fight(self, foe)

    
    # добавляем внешний метод внутрь класса SpiderMan
    # теперь класс "видит" функцию external_can_attack, которая объявлена снаружи,
    # но при этом написана по всем правилам метода класса! и у нее есть self!
    can_attack = external_can_attack
    
    
peter_parker = SpiderMan('Peter Parker', 90)
miles_morales = SpiderMan('Miles Morales', 85)
# наш новый метод can_attack работает!
print(peter_parker.can_attack(miles_morales))

# print("Пусть подерутся :)")
# if peter_parker.can_attack(miles_morales):
#     peter_parker.fight(miles_morales)
#     print(peter_parker.name, peter_parker.energy)
#     print(miles_morales.name, miles_morales.energy, miles_morales.status)

# проверяем, что теперь метод can_attack есть у peter_parker и у всех других объектов этого класса
# print()
# print(dir(peter_parker))
# print(dir(miles_morales))


# __Дополнение 2: Как удалить что-то из класса__

# In[ ]:


# удаляем атрибут вариант 1
peter_parker = SpiderMan('Peter Parker', 90)
miles_morales = SpiderMan('Miles Morales', 85)

# удаляем атрибут hands у peter_parker при помощи delattr
delattr(peter_parker, "hands")
print(peter_parker.__dict__)
# а что с miles_morales? у него hands остались
print(miles_morales.__dict__)


# In[ ]:


# удаляем атрибут вариант 2
peter_parker = SpiderMan('Peter Parker', 90)
miles_morales = SpiderMan('Miles Morales', 85)

# как мы знаем, к атрибутам класса можно получить доступ через 
# магический метод __dict__. но он же словарь? 
# поэтому просто воспользуемся методом удаления ключа из словаря...
del peter_parker.__dict__["hands"]
print(peter_parker.__dict__)
# а что с miles_morales? у него hands остались
print(miles_morales.__dict__)


# In[ ]:


# удаляем метод 
# а вот метод из экземпляра класса удалить не получится. зато из самого класса - да
# это можно сделать при инициализации класса

# удалим метод webshoot класса-родителя Spider
# теперь метод peter_parker.move(), пытаясь внутри себя вызвать Spider.webshoot, будет генерировать исключение
class Character:
    def __init__(self, name, power, energy=100, hands=2):
        self.name = name
        self.power = power
        self.energy = energy
        self.hands = hands
        
        
class Spider:
    def __init__(self, power, energy=50, hands=8):
        self.power = power
        self.energy = energy
        self.hands = hands
    
    def webshoot(self):
        print('Pew-Pew!')

class SpiderMan(Character, Spider):
    def __init__(self, name, power):
        super().__init__(name, power)
        self.backpack = []
        # мы можем удалить "ненужный" метод родителя сразу при инициализации
        # раскомментируйте строку ниже и проверьте    
#         del Spider.webshoot
    
    def webshoot(self):
        if 'web' in self.backpack:
            super().webshoot() 
        else:
            print('No web!')

    def move(self):
        self.webshoot()
        print('Moving on 3 square')


peter_parker = SpiderMan('Peter Parker', 90)
peter_parker.backpack.append("web")
# мы также можем удалить "ненужный" метод родителя в любой момент из всех объектов класса
# раскомментируйте строку ниже и проверьте   
# del Spider.webshoot
peter_parker.move()


# In[ ]:




