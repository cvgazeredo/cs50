from cs50 import get_int

n = get_int("n: ")

if n % 2 == 0: #The % operator gives us the remainder of n after we divide it by 2
    print("Even")
else:
    print("Odd")

