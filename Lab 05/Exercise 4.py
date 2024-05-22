def compute(a, b, c, d):
    if a > 10 or b > 10 or c > 10 or d > 10:
        return "Error: All numbers must be less than 10."
    else:
        return "Result is " + str(a + (b * c) + d)

try:
    a = float(input("Enter number a: "))
    b = float(input("Enter number b: "))
    c = float(input("Enter number c: "))
    d = float(input("Enter number d: "))
except ValueError:
    print("Error, please enter numeric input")
    exit()
print(compute(a, b, c, d))
