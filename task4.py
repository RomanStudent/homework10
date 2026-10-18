"""This script looks for str objects."""

list1 = ["beers",
        "doctor_pepper??,
        "greek salad",
        "chicken nuggets/",
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
