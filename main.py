"""
ООП- обьектно ориентированное программирование:
                                                Инкапсуляция;
                                                Абстракция;
                                                Полиморфизм;
                                                Наследование;

                Наследование
                     /\
        родительский>||<дочерний
"""
"""
snake case - hello_world
camel case - HelloWorld
"""
class House():
    """Уйдун макети"""
    def __init__(self, prospekt, number):
        """Уйдун тузулушу"""
        self.prospect = prospekt
        self.number = number
        self.age = 0

    def stroyka(self):
        """Уйдун курулушу"""
        print(f"{self.prospect} кочосундогу {self.number}- уй бутту")

    def age_of_house(self, years):
        """Курулган жылы"""
        self.age += years


class ChuyHouse(House):
    """Жаны курулуш"""
    def __init__(self, street, number1, prospect):
        super().__init__(prospect, number1)

        self.street = street


chuy = ChuyHouse('пр. Чуй', 166, 'пр, Манаса')
house1 = House('пр, Манаса', 64.1)
house2 = House('пр, Манаса', 64.2)
house2.age_of_house(4)
print(house1.prospect, house1.number)
print(chuy.street, chuy.number)
print(house1.number)
print(chuy.street)

























