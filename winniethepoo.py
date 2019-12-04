# un vieux clebard

class Dog:

    def __init__(self, race="none", age=0, color="none"):
        self.race = race
        self.age = age
        self.color = color

    def display(self):
        print("{} : race={}, age={}, color={}.".format(self, self.race, self.age, self.color))

    def bark(self):
        print("{}: waf waf waf !".format(self))
    
    def sleep(self):
        print("{}: zzzZZZZZZZZ !".format(self))

    def eat(self):
        print("{}: oh NomNomNomNom !!".format(self))

def main():
    dog1 = Dog("petit batard", 15, "blue")
    dog2 = Dog("gros batard", 3, "orange")

    dog1.display()
    dog2.display()

    dog1.eat()
    dog2.sleep()
    dog2.bark()

if __name__ == "__main__":
    main()