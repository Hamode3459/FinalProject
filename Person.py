class Person:
    def __init__(self, name, age, address, gender):
        self.name = name
        self.age = age
        self.address = address
        self.__height = 183
        self.gender = gender
    def printPerson(self):
        print(self.name)
        print(self.age)
        print(self.address)
        print(f"height = " {self.__height}")
        print(self.gender)