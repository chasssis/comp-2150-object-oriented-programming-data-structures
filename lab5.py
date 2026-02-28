import math

# -------------------------
# problem 1: Circle Class
# -------------------------
class Circle:
    def __init__(self, radius):
        self.radius = radius

    def diameter(self):
        return self.radius * 2

    def area(self):
        return math.pi * self.radius ** 2

    def perimeter(self):
        return 2 * math.pi * self.radius

#test 1
circle = Circle(5)
print("Diameter:", circle.diameter())
print("Area:", circle.area())
print("Perimeter:", circle.perimeter())

# -------------------------
# problem 2: Date Class
# -------------------------
class Date:
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day

    def format_date(self):
        return f"{str(self.month).zfill(2)}-{str(self.day).zfill(2)}-{self.year}"

#test 2
date = Date(2026, 2, 27)
print(date.format_date())

# -------------------------
# problem 3: Pet
# -------------------------
class Pet:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return f"{self.name} says: greetings."

class Dog(Pet):
    def speak(self):
        return f"{self.name} barks!"


class Cat(Pet):
    def speak(self):
        return f"{self.name} meows!"

#test 3
pet = Pet("Spot")
dog = Dog("Rex")
cat = Cat("Whiskers")

print(pet.speak())
print(dog.speak())
print(cat.speak())

# -------------------------
# problem 4: Animal Hierarchy
# -------------------------
class Animal:
    def __init__(self, name, species, age):
        self.name = name
        self.species = species
        self.age = age

    def make_sound(self):
        raise NotImplementedError("Subclasses must implement make_sound")

    def __str__(self):
        return f"{self.name} ({self.species}), Age: {self.age} years"


class Mammal(Animal):
    def __init__(self, name, species, age, fur_color):
        super().__init__(name, species, age)
        self.fur_color = fur_color

    def make_sound(self):
        print("Mammal sound")

    def __str__(self):
        return f"{super().__str__()}, Fur Color: {self.fur_color}"


class Bird(Animal):
    def __init__(self, name, species, age, wing_span):
        super().__init__(name, species, age)
        self.wing_span = wing_span

    def make_sound(self):
        print("Bird sound")

    def __str__(self):
        return f"{super().__str__()}, Wing Span: {self.wing_span} inches"

#test 4
simba = Mammal("Simba", "African Lion", 5, "Golden")
print(simba)
simba.make_sound()

eddie = Bird("Eddie", "Bald Eagle", 10, 72.5)
print(eddie)
eddie.make_sound()

# -------------------------
# problem 5: Further Specialization
# -------------------------
class Feline(Mammal):
    def __init__(self, name, species, age, fur_color, claw_length):
        super().__init__(name, species, age, fur_color)
        self.claw_length = claw_length

    def make_sound(self):
        print("Feline sound!")

    def __str__(self):
        return f"{super().__str__()}, Claw Length: {self.claw_length} inches"


class BigCat(Feline):
    def make_sound(self):
        print("Roar!")


class HouseCat(Feline):
    def make_sound(self):
        print("Meow!")


class Parrot(Bird):
    def __init__(self, name, species, age, wing_span, colorful_feathers):
        super().__init__(name, species, age, wing_span)
        self.colorful_feathers = colorful_feathers

    def make_sound(self):
        print("Squawk!")

    def __str__(self):
        return f"{super().__str__()}, Colorful Feathers: {self.colorful_feathers}"

#test 5
rajah = BigCat("Rajah", "Bengal Tiger", 7, "Orange", 4.5)
print(rajah)
rajah.make_sound()

felix = HouseCat("Felix", "Shorthair Cat", 4, "Grey Stripes", 0.75)
print(felix)
felix.make_sound()

tom = Feline("Tom", "Feline", 67, "Grey", 0)
print(tom)
tom.make_sound()

polly = Parrot("Polly", "Ara Macaw", 15, 36.2, True)
print(polly)
polly.make_sound()

dumbo = Mammal("Dumbo", "African Elephant", 12, "Gray")
print(dumbo)
dumbo.make_sound()

pidgey = Bird("Pidgey", "Rock Pigeon", 3, 20.0)
print(pidgey)
pidgey.make_sound()

##I know i just used all the examples that were given, i am lazy. hope that is ok