astring = "0123156789"
print(astring.index("6"))
print(astring.count("1"))
print(astring[::-1])

astring2 = "Hello world"
print(astring2.upper())
print(astring2.lower())
print(astring2.startswith("Hell"))
print(astring2.endswith("ld"))

spliced_string = astring2.split(" ")
print(spliced_string)
for x in astring2:
    print(x)

for x in spliced_string:
    print(x)


