try:
    age = int(input("Age: "))
except ValueError as ex:
    print("You didn't enter a valid age.")
    print(ex)
    print(type(ex))
else:
    ''' this will be executed only if there's no exception'''
    print("No exceptions were thrown")
print("Execution continues.")
