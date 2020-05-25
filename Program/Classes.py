# t = int(input())
# for i in range(t):
#     n = int(input())
#     i = 1
#     while True:
#         if i * i >= n:
#             break
#         i = +1
#     print(i)
# Capitiliize the single word pascl
# class Point:
#     def __init__(self,x,y):
#         self.x=x
#         self.y=y
#     def move(self):
#         print("move")
#     def draw(self):
#         print("draw")
# point1=Point(10,20)
# print(point1.x+1)
# point1.draw()
# point1.x=10
# point1.y=20
# point2=Point()
# print(point1.x)
# print(point1.y)
# class Person:
#     def __init__(self,name):
#         self.name=name
#     def talk(self):
#         print(f"Hi  this is {self.name}")
# person1=Person('Surya')
# person1.talk()
'''Inheritance'''

# To avoid the reputation of this code we use Inheriatnce
class Animal:
    def walk(self):
        print('Walk')
class Dog(Animal):
    def bark(self):
        print("Bho Bho")

class Cat(Animal):
    def meo(self):
        print("Meoowww")

dog1=Dog()
dog1.walk()
dog1.bark()
cat1=Cat()
cat1.meo()



'''Modules in Python'''



