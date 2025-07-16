#constructor -> it is a function which is immediately called when object is created
#it is used to initialize the variable for object
#__init__  it iws the constructur function

class student : 
    def __init__(self,student_name,rool_no,age):
        self.student_name = student_name
        self.rool_no = rool_no
        self.age = age
    def print_details(self):
        print(f'''student name : {self.student_name}
        rool no : {self.rool_no}
        age : {self.rool_no}''')

object1 = student("krishna",60,19)
object2 = student("vedant",46,19)
object3 = student("kushal",73,25)
object4 = student("aadi",41,20)
object5 = student("nirya",70,19)

object1.print_details()
object2.print_details()
object3.print_details()
object4.print_details()
object5.print_details()