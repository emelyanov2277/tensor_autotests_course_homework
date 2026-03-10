class chelovek:
    chelovek_spisok = []
    def __init__(self, name: str, age: int, hel: int, hobby: list):
        self.name = name
        self.age = age
        self.hel = hel
        self.hobby = hobby
        self.chelovek_spisok.append(self)
    def create_chelovek(self):
        print(f'чел {self.name} создан с возрастом {self.age} и жизнью {self.hel} и набором хобби: {", ".join(self.hobby)}')
    def spisok_chelovek_hobby(self):
        print(f'список хобби человека {self.name} = {", ".join(self.hobby)}')
    def bolezn_chelovek(self, bolezn):
        self.hel = self.hel - bolezn
        return self.hel
    @classmethod
    def spisok_chelovek(cls):
        for i in cls.chelovek_spisok:
            print(f'{i.name}, возраст: {i.age}, жизнь: {i.hel}')
vasya = chelovek('вася', 31, 80, ['спорт', 'готовка', 'кулинария'])
vasya.create_chelovek()
vasya.spisok_chelovek_hobby()
vasya.bolezn_chelovek(10)
chelovek.spisok_chelovek()
