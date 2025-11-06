class Animal:
    def __init__(self,name,age):
        self.__name = name
        self.__age = age

class Dog(Animal):
    def __init__(self,name,age):
        super().__init__("Dog",15)
        self.__name = name

class cat(Animal):
    def __init__(self,name,age):
        super().__init__("Cat",20)
        self.__name = name

class tiger(Animal):
    def __init__(self,name,age):
        super().__init__("tiger",30)
        self.__name = name

