#types of arguments

def greet(student,trainer):
    print(f'''good morning {trainer}
    welcome {student}''')

#1)positional arguments_ - - based on the  positions of parameters
greet("krishna","GOVINTHAN")

#2)KEYWORD ARGUMENT - - - DECLARE THE ARGUMENT WITH THEIR PARAMETERS
greet(trainer="GOVINTHAN",student="krishna")

# 3)VARIABLE length arguments - - - if we are not aware of the no.of arguments  ->args*  (any type of argumens can be given)
def printer(*args):
    for i in args:
        print(i)
    print(args)

printer(5,6,7,8,4)   #these will be stored in lists

# 4)kwargs argument - - - used when arguments are mentioned with their variables  ->**kwargs
def printerrrr(**kwargs):
    for i in kwargs.keys():
        print(i)
    for i in kwargs.values():
        print(i)
    for k,v in kwargs.items():
        print(f'''{k} = {v}''')
    print(kwargs)

printerrrr(baba1="big",name="babita",babba2="small")    #these will be stored in dictionary