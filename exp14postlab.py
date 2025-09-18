
# import math

# class Circle:
#     def __init__(self, radius):
#         self.radius = radius

#     def area(self):
#         return math.pi * self.radius ** 2

#     def perimeter(self):
#         return 2 * math.pi * self.radius

# # Example use
# c = Circle(5)
# print("Radius:", c.radius)
# print("Area:", c.area())
# print("Perimeter:", c.perimeter())




class Book:
    def __init__(self, title, author, price):
        self.title = title
        self.author = author
        self.price = price
    def display(self):
        print(f"Title: {self.title}, Author: {self.author}, Price: {self.price}")

    def apply_discount(self, percent):
        self.price = self.price - (self.price * percent / 100)
# Example use
book1 = Book("Python Basics", "John Smith", 500)
book2 = Book("AI Intro", "Jane Doe", 700)
print("Before discount:")
book1.display()
book2.display()
book2.apply_discount(10)
print("\nAfter 10% discount on book2:")
book1.display()
book2.display()
