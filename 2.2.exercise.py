x = object()
y = object()

x = "A"*10
y = "B"*10

# Here goes my code
x_list = [x] * 10
y_list = [y] * 10
big_list = x_list+y_list

print("x_list contains %d objects" % len(x_list))
print("y_list contains %d objects" % len(y_list))
print("big_list contains %d objects" % len(big_list))

print(x_list.count(x))
print(x)
print(y_list.count(y))
print(y)

# Testing code
if x_list.count(x) == 10 and y_list.count(y) == 10:
    print("Almost there")
else:
    print("Keep trying")

if big_list.count(x) == 10 and big_list.count(y) == 10:
    print("Great")
else:
    print("Keep trying")
