class chels:
    chels_list = []

    def __init__(self, name:str, age:int, health:int, status: bool, hobby: list):
        self.name = name
        self.age = age
        self.health = health
        self.status = status
        self.hobby = hobby
        chels.chels_list.append(self)

    def chel_create(self):
        print(f'чел имени -> {self.name} возраста = {self.age} и жизнь в {self.health} статуса - {self.status} и списком хобби: {", ".join(self.hobby)} ')

    @classmethod
    def chel_list(cls):
        print(f'вот список челиков:')
        for index, chel in enumerate(chels.chels_list, 1):
            print(f'{index}) {chel.name}, {chel.health}, {chel.age} лет, хобби: {", ".join(chel.hobby)}')
    def chel_name_change(self, name):
        print(f'имя {self.name} смена на {name}')
        self.name = name

    def chel_health_damage(self,damage):
        self.health = self.health - damage
        print(f'{self.name} нанесен дмг = {damage} и хп стало = {self.health}')

ivan = chels('иван', 19, 80,True, ["машина", "дерево"])
petya = chels('петя', 37, 71, True, ["кофе", "вино"])

ivan.chel_create()
petya.chel_create()
chels.chel_list()

petya.chel_name_change("лол")

chels.chel_list()

petya.chel_health_damage(40)