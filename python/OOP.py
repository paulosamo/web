#object-oriented programing
# class Person:
#     def __init__(self):
#         self.name = "joy"
#         self.gender = "female"
#         self.age = 19
#         self.school = "emobilis"
#         self.location = "kikuyu"
# person = Person()
#
# person.name = "John"
# print(person.name)
#
# person.gender = "Male"
# print(person.gender)
#
# person.age = 21
# print(person.age)
# print(person.school)
# print(person.location)
class People:
    def __init__(self, name, age, sex):
        self.name = name
        self.age = age
        self.sex = sex
person1 = People(name="jane", age=18, sex="female")

person2 = People(name="joyce", age=20, sex="female")

person3 = People(name="chris", age=18, sex="male")

print(person1.name)
print(f'my name is {person1.name} and am {person1.age} years old and i am a {person1.sex}')
class Fruit:
    def __init__(self):