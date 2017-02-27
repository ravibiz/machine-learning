class Person:
    def __init__(self, name, gender):
        self.name = None
        self.gender = None

    def getName(self):
        self.name

    def getGender(self):
        self.gender


class Male(Person):
    def __init__(self, name):
        print("My name is Mr." + name)


class Female(Person):
    def __init__(self, name):
        print("My name is Mrs." + name)


class Factory:
    def getPerson(self, name, gender):
        if gender == 'M':
            return Male(name)
        elif gender == 'F':
            return Female(name)
        else:
            print("Unknown")


if __name__ == '__main__':
    factory = Factory()
    factory.getPerson("Ravi", "M")
    factory.getPerson("Rajini", "F")
    factory.getPerson("Rajini", "A")
