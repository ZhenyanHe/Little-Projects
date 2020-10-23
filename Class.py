class Washer():
    def wash(self):
        print('can wash clothes')
    # get the feature
    def print_info(self):
        print(self.width)


haier = Washer()
print(haier)
haier.wash()

# Self指的是调用该函数的对象
haier.width = 500
haier.height = 800

haier.print_info()

# _init_()
class Washer():
    def _init_(self):
        self.width = 500
        self.height = 800
    def print_info(self):
        print(f'width is {self.width}, height is {self.height}')

haier = Washer()
haier.print_info()

class Washer():
    def __init__(self, a, b):
        self.width = a
        self.height = b
    def print_info(self):
        print(f'width is {self.width}, height is {self.height}')

haier = Washer(10, 20)
haier.print_info()

class Washer():
    def __init__(self, a, b):
        self.width = a
        self.height = b
    def __str__(self):
        print(f'This is the Haier instructions ')

haier = Washer(10, 20)
print(haier)

class Washer():
    def __init__(self, width, height):
        self.width = width
        self.height = height
    def __del__(self):
        print(f'{self} has been deleted from Haier')

haier = Washer(10, 20)
print(haier)

class SweetPotato(object):
    def __init__(self):
        self.cook_time = 0
        self.cook_status = 'raw'
        self.condiments = []

    def cook(self, time):
        self.cook_time += time
        if 0 <= self.cook_time < 3:
            self.cook_status = 'raw'
        elif 3 <= self.cook_time <5:
            self.cook_status = 'half-raw'
        elif 5 <= self.cook_time < 8:
            self.cook_status = 'done'
        elif self.cook_time >= 8:
            self.cook_status = 'over cooked'

    def __str__(self):
        return f'This potato has been cooked for {self.cook_time}, and is {self.cook_status}, condiments are {self.condiments}'

    def add_condiments(self, condiment):
        self.condiments.append(condiment)
digua1 = SweetPotato()
print(digua1)
digua1.cook(2)
digua1.add_condiments('pepper')
print(digua1)
digua1.cook(2)
print(digua1)
digua1.cook(1)
digua1.add_condiments('salt')
print(digua1)



class furniture(object):
    def __init__(self, name, size):
        self.name = name
        self.size = size
class house(object):
    def __init__(self, address, area):
        self.address = address
        self.area = area
        self.free_area = area
        self.furniture = []
    def __str__(self):
        return f'house is at {self.address} with size {self.area} sqft, the available room is {self.free_area} and already has {self.furniture} inside.'
    def add_furniture(self, item):
        if self.free_area >= item.size:
            self.furniture.append(item.name)
            self.free_area -= item.size
        else:
            print('furniture over sized')

bed = furniture('bed', 6)
sofa = furniture('sofa', 8)

lisa =house('LA', 1000)
print(lisa)

lisa.add_furniture(bed)
lisa.add_furniture(sofa)
print(lisa)

class A(object):
    def __init__(self):
        self.num = 1
    def info_print(self):
        print(self.num)

class B(A):
    pass

result = B()
result.info_print()


class Master(object):
    def __init__(self):
        self.kongfu = 'kongfu 1'
        self.__money = 2000000

    def make_cake(self):
        print(f'make cake with {self.kongfu}')

class School(object):
    def __init__(self):
        self.kongfu = 'kongfu 2'

    def make_cake(self):
        print(f'make cake with {self.kongfu}')

        # Super 2.1
        # super(School, self).__init__()
        # super(School, self).make_cake()

class Student(School, Master):
    def __init__(self):
        self.kongfu = 'kongfu 3'

    def make_cake(self):
        self.__init__()
        print(f'make cake with {self.kongfu}')
    def make_master_cake(self):
        Master.__init__(self)
        Master.make_cake(self)

    def make_school_cake(self):
         School.__init__(self)
         School.make_cake(self)
    def make_old_cake(self):
        # Master.__init__(self)
        # Master.make_cake(self)
        # School.__init__(self)
        # School.make_cake(self)
        # Super 2.1
        # super(Student, self).__init__()
        # super(Student, self).make_cake()
        super().__init__()
        super().make_cake()


alice = Student()
alice.make_cake()
alice.make_master_cake()
alice.make_school_cake()

class Student2(Student):
    pass
ray = Student2()
ray.make_master_cake()

















