class Person:
    name = ""
    age = 1
    weight = 1
    gender = True

    def medical(self):
        return "med care"


class Worker(Person):

    def education(self):
        return "edu"

    def department(self):
        return 'dep'


class Student(Person):
    pass


class Children(Person):
    pass


class Homeless(Person):
    pass

a=Worker()