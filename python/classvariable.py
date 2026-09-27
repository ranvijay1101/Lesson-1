# Activity 1
class Student:
    grade = 10
    def __init__(self):
        print("Hi I am a student in grade", self.grade)
ob = Student()

# Activity 2
class Student:
    grade = 10
    name = "Banana"
    def introduction(self):
        print("Hi I am a student")
    def details(self):
            print("My name is", self.name)
            print("I study in Grade", self.grade)
ob = Student()
ob.introduction()
ob.details()


# Actvity 3
class Parrot:
     species = "bird"
     def __init__(self, name, age):
          self.name = name
          self.age = age
blu = Parrot("Blu", 10)
woo = Parrot("Woo", 15)
print(blu.species)
print(woo.species)
print(blu.name, blu.age)
print(woo.name, woo.age)


# Activity 4
class Parrot:
     def __init__(self, name, age):
          self.name = name
          self.age = age
     def sing(self, song):
          return self.name, song
     def dance(self):
         return self.name
blu = Parrot("Blue", 10)
print(blu.sing("'Happy'"))
print(blue.dance())
          