def product(list):
    value = 1
    for e in list:
        value *= int(e)
    return value

print product([4, 5, 5])