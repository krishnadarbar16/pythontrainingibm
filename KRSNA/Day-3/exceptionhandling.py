try:
    a=int(input("enter a : "))
    b=int(input("enter b : "))
    c=a/b
    print(c)
except ZeroDivisionError:
    print("cannot divide by zero")
except ValueError:
    print("invalid input enter valid integer")
    
print("flow of the program")
