def add_everything_up(a, b):
    try:
        type(a) == type(b)
        print(a + b)
    except:
        print(str(a) + str(b))

print(add_everything_up(123.456, 'строка'))
print(add_everything_up('яблоко', 4215))
print(add_everything_up(123.456, 7))
