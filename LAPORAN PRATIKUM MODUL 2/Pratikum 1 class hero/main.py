class Hero:
    jumlah = 0
    __privateJumlah = 0  # atribut private class

    def __init__(self, name, health):
        self.name = name
        self.health = health
        self.__private = 'private'    
        self._protected = 'protected' 

hero_1 = Hero('Atsu', 100)

print(hero_1.__dict__)              # menampilkan atribut instance
print(Hero.__dict__)                # menampilkan atribut class
print(Hero.Hero__privateJumlah)    # akses atribut private class
