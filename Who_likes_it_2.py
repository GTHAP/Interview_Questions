def likes(names):

    count = 0

    list_length = len(names)

    if list_length == 0:
        print("No one likes this")
    if list_length == 1:
        print(names[0], " likes this")
    if list_length == 2:
        print(names[0], names[1], " like this")
    if list_length == 3:
        print(names[0], names[1], names[2], " like this")
    if list_length == 4:
        count = list_length - 2
        print(names[0], names[1], " and ", count, " others like this")
    if list_length > 4:
        count = list_length - 2
        print(names[0], names[1], " and ", count, " others like this")

names = ["GTX","RTX","ETX","HTX","ATX"]

likes(names)

