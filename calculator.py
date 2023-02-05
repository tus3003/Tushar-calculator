
a = float(input("enter first no."))
b = float(input("entwe second no."))
add = a + b
subtract = a-b
divide = a/b
multiplication = a*b
value = a//b
power = a**b

z = input("choose what operation you want to perfome 'add', 'subtract', 'divide', 'multiplication', 'value', 'power'")

if z == "add":
    print("sum is",add)
elif z == "subtract":
    print("difference is",subtract)
elif z == "divide":
    print("difference is", divide)
elif z == "multiplication":
    print("difference is", multiplication)
elif z == "value":
    print("difference is", value)
elif z == "power":
    print("difference is", power)
else:
    print('please enter correct value')

