print("hello liv")
print("hallo Tätzli")

x = 1
if x == 1:
    # indented four spaces
    print("x is 1.")

    myint = 7
    print(myint)

    myfloat = 7.0
    print(myfloat)
    myfloat = float(7)
    print(myfloat)
    print(float(7))

    mystring = "Don't worry about apostrophes"
    print(mystring)

    one = 1
    two = 2
    three = one + two
    print(three)

    three = 3
    five = three + two
    print(five)

    hello = "hello"
    world = "world"
    helloworld = hello + " " + "liv" + " " + world
    print(helloworld)

    oki = "oki"
    doki = "doki"
    okidoki = oki + doki
    print(okidoki)

    Na = "Na"
    Logo = "Logo"
    Kumpi = Na + " " + Logo
    print(Kumpi + " " + okidoki)

    a, b = 2, 4
    print(a + b)

    a, b = Na, Logo
    print(a, b)

    mystring = "hello"
    myfloat = 10.0
    myint = 20
    if mystring == "hello":
        print("String: %s" % mystring)
    if isinstance(myfloat, float) and myfloat == 10.0:
        print("Float: %f" % myfloat)
    if isinstance(myint, int) and myint == 20:
        print("Integer: %d" % myint)

mystring = "'hallo Liv'"
print(mystring)
print("papa" + " " + "sagt:" + " " + mystring)

mylist = []
mylist.append(1)
mylist.append(2)
mylist.append(3)
print(mylist[0])
print(mylist[1])
print(mylist[2])

for x in mylist:
    print(x)


mylist = [1]
mylist.append(3)
mylist.append(6)
mylist.append(9)
print(mylist[0])
print(mylist[1])
print(mylist[2])
print(mylist[3])

for x in mylist:
    print(x)

numbers = []
strings = []
names = ["John", "Eric", "Jessica"]

numbers.append(1)
numbers.append(2)
numbers.append(3)

strings.append("hello")
strings.append("world")

second_name = names[1]

print(numbers)
print(strings)
print("The second name on the names list is %s" % second_name)


print("Liv" + "Zoé")
print("Kumpi"*5)

Liv = 42
Zoé = 2
print(Liv + Zoé)

Papa = Liv + 5
print(Papa)

Kumpi = "uncool"
print(Kumpi)
Kumpi = "cool!"
print(Kumpi)

myAge = input(19)
print('You will be ' + str(int(myAge) + 1) + ' in a year.')
print("Liv")
print("hello")
print("hello")

myName = input("Zoé")
print(myName)

print("It is good to meet you, " +myName)
print(len(myName))

input("liv")