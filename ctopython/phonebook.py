from cs50 import get_string

#Its a hash table of people
people = {
    "Clarice": "+55-21-996067410",
    "Andre": "+55-21-983545734"
}
#Thats a powerful way of associating one thing with another by using the ':'

name = get_string("Name: ")
if name in people:
    print(f"Number: {people[name]}")

#Alternatively we can do that:
#name = get_string("Name: ")
#if name in people:
#   number = people[name]
#    print(f"Number: {number]}")