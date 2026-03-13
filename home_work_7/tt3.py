class chel:
    chel_list = []
    def __init__(self, name:str, age: int, status: bool, hobby: list):
        self.name = name
        self.age = age
        self.status = status
        self.hobby = hobby
        chel.chel_list.append(self)
    def chel_crete(self):

        print(f'человек с именеем {self.name} , возрастом {self.age}, статусом {self.status} и списком хобби: {", ".join(self.hobby)} ПО создался')
    def chel_lives(self, lives):
        print(f'человек {self.name} прожил {lives} лет и стал возрастом {self.age + lives}')
    @classmethod
    def chel_spisok(cls):
        print(f'вот список людей: ')
        for chel in cls.chel_list:
            print(chel.name)

ivan = chel('иван', 19, сTrue, ["машины", "квартиры"])
ivan.chel_crete()
ivan.chel_lives(10)
chel.chel_spisok()
chel.chel_spisok()