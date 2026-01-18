"""
Plan is to write a script that takes any string and reverses it no matter the length

The shorter, the better.

"""
from operator import index

string_input = input("Enter a string: ")

characters = list(string_input)
length = len(string_input) - 1

for i in range(len(characters) // 2):
    mirror = length - i
    characters[i], characters[mirror] = characters[mirror], characters[i]

print("".join(characters))
