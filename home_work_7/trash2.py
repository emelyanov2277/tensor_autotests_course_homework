class chelovek:
    chelovek_list = []
    def __init__(self, name:str, age:int, health:int, city: str, hobby:list):
        self.name = name
        self.age = age
        self.health = health
        self.hobby = hobby
        self.city = city
        chelovek.chelovek_list.append(self)
    def chelovek_create(self):
        print(f'человек : {self.name} рождается возраста равного {self.age}, жизнью в {self.health} из города {self.city} и списком хоббои: {", ".join(self.hobby)}')
    def chelovek_check_age(self):
        if self.age >=18:
            print(f'человек {self.name} взрослый')
        else:
            print(f'человек {self.name} не взрослый')

    @classmethod
    def chelovek_list_all(cls):
        print(f'вот список всех людей у нас: ')
        for chel in cls.chelovek_list:
            print(f"{chel.name}, {chel.age} лет, {chel.city}, здоровье {chel.health}")
    def chelovek_health_damage(self, bolezn):
        print(f'{self.name} получает болезнь {bolezn } и его здоровье становится {self.health - bolezn} вместо {self.health}')

vasya = chelovek('вася', 31, 85, 'псков', ['айти', 'коффе'])
vasya.chelovek_create()
misha = chelovek('миша', 21, 95,'спб', ['машины', 'пиво'])
misha.chelovek_create()
misha.chelovek_check_age()
misha.chelovek_health_damage(10)
chelovek.chelovek_list_all()
