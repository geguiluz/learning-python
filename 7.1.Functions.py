def my_function():
    print("Hello from my function!")


def my_function_with_args(username, greeting):
    print("Hello, %s , From My Function!, I wish you %s" %
          (username, greeting))


def sum_two_numbers(a, b):
    x = a+b
    return x


# Then we'll call our functions
my_function()
my_function_with_args("Juan", "die soon")
print(sum_two_numbers(1, 5))
