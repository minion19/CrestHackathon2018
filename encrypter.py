x=input("hi input pls. pls write 1 extra character")
for letter in x:
    letter = ord(letter) - 13
    print(chr(letter), end="")