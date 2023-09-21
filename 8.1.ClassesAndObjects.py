class MyClass:
    variable = "blah"

    def some_function(self):
        print("This is a message inside the class.")

    def __init__(self, number):
        self.number = number


myobjectx = MyClass("B")
myobjecty = MyClass("C")

myobjectx.variable = "X"

print(myobjectx.variable)
print(myobjecty.variable)

myobjectx.some_function()

print(myobjectx.number)
