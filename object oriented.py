class Person:
    def __init__(self, name):
        self.name = name
        self.__is_employee = False
        self.is_businessman = False
        self.__check_bug()

    def __str__(self):
        if self.__is_employee:
            return self.name + "is Employee."
        elif self.is_businessman:
            return self.name, "is businessman"
        else:
            return self.name + ' is not yet working'

    def __repr__(self):
        print('name:', self.name)
        print('Employee status:', self.__is_employee)
        print('businessman status:', self.is_businessman)

    def __check_bug(self):
        if self.__is_employee and self.is_businessman:
            try:
                raise IOError
            except IOError as mistake:
                print("error:", mistake)


class Employee(Person):
    def __init__(self, name):
        super().__init__(name)
        self.__is_employee = True

    @classmethod
    def employ(cls, person=Person(name="")):
        person.__is_employee = True

    @classmethod
    def fire(cls, person=Person(name="")):
        person.__is_employee = False

def main():
    me = Person("Saransh")
    print(me)
    Employee.employ(me)
    print(me)
    Employee.fire(me)
    print(me)
# fixme: a bug causing me to be unemployed on employ method
if __name__ == '__main__':
    main()
