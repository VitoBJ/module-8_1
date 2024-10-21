def add_everything_up(a, b):
    try:

        if isinstance(a, (int, float)) and isinstance(b, (int, float)):
            return a + b


        elif isinstance(a, str) and isinstance(b, str):
            return a + b


        else:
            return str(a) + str(b)

    except TypeError as e:

        return str(a) + str(b)



print(add_everything_up(5, 10))
print(add_everything_up(5.5, 4.5))
print(add_everything_up("Hello, ", "world!"))
print(add_everything_up(5, " apples"))
print(add_everything_up("Count: ", 100))