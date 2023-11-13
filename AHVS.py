class Worker:

    def __init__(self, name, surname, work_pls):
        self.name = name
        self.surname = surname
        self.work_pls = work_pls

    def sellory_type(self):
        pass

    def holiday_count(self):
        pass


staff = Worker("Armen", "Gevorgyan", "Google")
print(staff.name)
ani = Worker("Ani", "Avagyan", "Oracle")

print(ani.name)


class Transport:
    def __init__(self, power):
        self.power = power

    def break_system(self):
        pass


class Car(Transport):
    gas_type = ""
    transsmision = ""
    abs = True

    def __init__(self, color, door, power):
        super().__init__(power)
        self.color = color
        self.door = door

    def drive(self, direction="d"):
        for i in range(10):
            print(i)
        return direction

    def break_system(self):
        return "stop"

    class Engine:
        pass


class Bus(Car):
    def __init__(self, passenger_count, color, door, power):
        super().__init__(color, door, power)
        self.__passenger_count = passenger_count

    def passenger_count_set(self, passenger_count):
        self.__passenger_count = passenger_count

    def passenger_count_get(self):
        if input("input password") == "1111":
            return self.__passenger_count
        else:
            return "incorrect input"

    def break_system(self):
        return "air break system."


class Jeep(Car):

    def break_system(self):
        return "liquid break system."


class Train(Transport):
    __passenger_count = 0

    def break_system(self):
        return "air break system."


class Ship(Transport):
    def break_system(self):
        return "reverse break system."


class Plan(Transport):
    def break_system(self):
        return "turbine break system."


# volvo = Bus(12, "silver", 5, 350)
# print(volvo.break_system())
# volvo.passenger_count_set(32)
# print(volvo.passenger_count_get())
# yachta = Ship(120)
# print(yachta.break_system())
# train = Train(1000)
# print(train.passenger_count)
# train.passenger_count = 100


def test_func(num, count=1):
    print(num - count)


test_func(num=9)


def var_parameters(*args):
    # print(arg)
    print(args)
    print(type(args))
    # print(kwargs)


var_parameters(12, 45, 56, 78, 89)


class Area:
    def __init__(self, *args):
        self.args = args

    def area(self):
        if len(self.args) == 1:
            return 3.14 * pow(self.args[0], 2)
        elif len(self.args) == 2:
            return self.args[0] * self.args[1]
        elif len(self.args) == 3:
            p = (self.args[0] + self.args[1] + self.args[2]) / 2
            if (p - self.args[0]) * (p - self.args[1]) * (p - self.args[2]) > 0:
                return pow(p * (p - self.args[0]) * (p - self.args[1]) * (p - self.args[2]), 1 / 2)
            else:
                return -1

    def perimeter(self):
        if len(self.args) == 1:
            return 2 * 3.14 * self.args[0]
        elif len(self.args) == 2:
            return 2 * (self.args[0] + self.args[1])
        elif len(self.args) == 3:
            p = (self.args[0] + self.args[1] + self.args[2]) / 2
            if (p - self.args[0]) * (p - self.args[1]) * (p - self.args[2]) > 0:
                return self.args[0] + self.args[1] + self.args[2]
            else:
                return -1


cycle = Area(7.4)
rectangle = Area(7.4, 4.9)
triangle = Area(62, 40, 25)
print(" -------  area of --------")
print("Area of cycle is {}".format(cycle.area()))
print("Area of rectangle is {}".format(rectangle.area()))
print("Area of triangle is {}".format(triangle.area()))
print(" -------  perimeter of --------")
print("Perimetr of cycle is {}".format(cycle.perimeter()))
print("Perimetr of rectangle is {}".format(rectangle.perimeter()))
print("Perimetr of triangle is {}".format(triangle.perimeter()))

print(" -------  function paradigma --------")


def plus(a, b):
    return a + b


def minus(a, b):
    return a - b


def sum_of(start, end):
    sum_num = 0
    for i in range(start, end):
        sum_num += i
    return sum_num


def math_operation(number_a, number_b, operation):
    result = operation(number_a, number_b)
    if result > 0:
        return result
    else:
        return -1 * result


print(math_operation(12, 45, plus))
print(math_operation(12, 45, minus))
print(math_operation(12, 45, sum_of))


def func_return(func_list):
    if len(func_list) > 0:
        return func_list[0]
    else:
        return -1


list_func = [plus, minus, sum_of]

temp = func_return(list_func)(12, 12)
print(temp)

print(" -------  decoreator --------")


def decor(func):
    def inner(a, b):
        return func(a, b) * 10

    return inner


@decor
def multiply(a, b):
    return a * b


print(multiply(5, 6))

import time


def delta_time(func):
    def inner(*args):
        start = time.time()
        func(*args)
        return time.time() - start

    return inner


@delta_time
def test_func(*args):
    sum_ = 0
    for i in range(args[0]):
        sum_ += pow(int(str(i)), 1 / 2)


# print(test_func(10000000))


@delta_time
def decor_function(*args):
    sum_ = 0
    for i in range(args[0], args[1]):
        sum_ += pow(int(str(i)), 1 / 2) + pow(int(str(i)), 2)


# print(decor_function(100, 10000000))

print(" -------  generator --------")


def i_range(start, end, step):
    result = start
    while True:
        result += step
        if result < end:
            yield result
        else:
            break


# i_range = iter(i_range(1, 8, 1.5))

# print(next(i_range))
# print(next(i_range))
# print(next(i_range))

for i in i_range(1.1, 5.6, 0.5):
    print(i)
