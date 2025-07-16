#create a contact book,
#where each contact contains name,number,email
#add functions to add contacts , remove and view all contacts

#dictionary to save contacts
contact_book = {
    1:["krishna",9959670833,"krishnadarbar@gamil.com"],
    2:["vedant",9988776655,"vedantmali@gmail.com"],
    3:["aadi",2233445566,"aadibho@gmail.com"]
}

#function to view a single contact using seriaL number
def view_contact(*args):
    contact_no = int(input("enter the serial number : "))
    print(contact_book[contact_no])

#function to view all contacts in dictionary
def view_all_contacts():
    for i in contact_book:
        for j in contact_book[i]:
            print(j)
        print("---------------------")

#function to add contact in dictionary
def add_contact(*args):
    new_key = len(contact_book.keys()) + 1
    print("--->enter the following details to add contact")
    name = input("enter name : ")
    phone = int(input("enter phone number : "))
    email = input("enter email : ")
    serial = [name,phone,email]
    contact_book[new_key] = serial

# function to remove contact
def remove_contact(*args):
    key = int(input("--->enter the serial number of to be delete : "))
    contact_book.pop(key)
    
print("....welcome to contact book....")
print(f"Queries::::")
print('''   1)View all contacts
    2)View a contact
    3)Add contact
    4)Remove contact
    5)Close''')
while True:
    query = input("Enter query : ")
    if(query == "1"):
        view_all_contacts()
    elif(query == "2"):
        view_contact()
    elif(query == "3"):
        add_contact()
    elif(query == "4"):
        remove_contact()
    elif(query == "5"):
        print("contact book close:: THANK YOU!!")
        break
    else:
        print("wrong input ...")