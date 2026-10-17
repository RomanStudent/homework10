"""This script looks for str objects."""

list1 = [23,
        23.213,
        "asdasd",
        "a",
        True,
        26,
        False,
        [23, 32],
        (65, 643.23),
        "asd"]
count = 0

for i in list1:
    if type(i) == str:
        count += 1

print(count)
