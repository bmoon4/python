try:
    age = int(input("Age: "))
    xfactor = 10/age
except(ValueError, ZeroDivisionError):
    print("Something's wrong")
else:
    print("No exceptions were thrown.")
