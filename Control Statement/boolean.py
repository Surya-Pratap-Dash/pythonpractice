class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __bool__(self):
        if self.age< 18 or self.age > 65:
            return False
        return True

if __name__ == '__main__':
    person = Person('Jane', 16)
    print(bool(person))
