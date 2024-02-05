print("Hello world")
print(1, 2, 3, 4, 5, 6, sep="~")
print(1, 2, 3, 4, 5, 6, sep="_")
print(1, 2, 3, 4, 5, 6, sep=":")
print(1, 2, 3, 4, 5, 6)#Default sep=' '
"""Escapes Sequences

- characters whose presence is felt, but they were not printed
    \t - tab space
    \n - new line
    \b - overwrites previous character

r'' - raw string"""
print("hello \tworld \npython")
# To ignore the escape sequences
print("hello \tworld \\npython")
# \b - overwrites previous character
print("Hei")
print("He\bi")
print("He\b")
print(r"hello \tworld \npython")