
def add(*args):
    print(args)
    print(type(args))
    print(args[0])
    return sum(args)


print(add(2,3,4))
print(add(1,2,99,5))

def calculate(n,**kwargs):

    n += kwargs['add']
    print(n)
    n *= kwargs['mult']
    print(n)


calculate(2,add=3, mult=5)

class Car:

    def __init__(self, *args, **kw):
        self.make = kw["make"]
        self.model = kw.get("model")

my_car = Car(make="Robin", model="Reliant")
print(my_car.make)
my_car2 = Car(make="BMW")
print(my_car2.model)