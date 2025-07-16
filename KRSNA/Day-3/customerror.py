age =int(input("enter age: "))
if age < 18 :
    raise ValueError("Age must be 18 or older")
else:
    print("access granted")
