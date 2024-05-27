from cs50 import get_string

before = get_string("Before : ")
print("After: ", end="")
#for c in 'string'
for c in before:
    #here its uppercasing this specific character
    print(c.upper(), end="")
print()

