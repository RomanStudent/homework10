"""This script looks for str objects."""

list1 = [23,
        23.213,
        "penguin 1",
        "penguin",
        True,
        26,
        False,
        [23, 32],
        (65, 643.23),
        "barbecue bacon burger"]
count = 0

for i in list1:
    if type(i) == str:
        count += 1

print(count)
