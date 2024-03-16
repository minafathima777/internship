# a=10
# b=20
# print("Addition of 2 numbers:",a+b)

# str1="Hello"
# str2="Python"
# print("Cncatination of 2 strings:",str1+str2)

# list1=[1,2,3]
# list2=['a','b']
# print("Concatination of two lists",list1+list2)

# class shape:
#     def area(self):
#         return=0
# class Circle(shape):
#     def __init__(self,radius):
#         self.radius=radius
#     def area(self):
#         return 3.14* self.radius**2


class shape:
    def area(self):
        return 0
class Square(shape):
    def __init__(self,side):
        self.side=side
    def area(self):
        return self.side**2
square=Square(side=8)
print(square.area())