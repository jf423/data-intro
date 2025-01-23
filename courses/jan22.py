def HelloWorld(x, y):
    if x < 10:
        print("Hello World, x was < 10")
    elif x < 20:
        print("Hello World, x was >= 10 but < 20")
    else:
        print("Hello World, x was >= 20")
    return x + y

for i in range (8, 25, 7):
    print(i)

for i in range (10, 0, -1):
    print(i)

for i in ['test', 1]:
    print(i)
