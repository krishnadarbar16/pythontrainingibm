# Bill Splitter
# Ask for the total bill and number of people.
# Divide the bill and show how much each person should pay.
bill_amount = float(input("Enter bill amount : "))
total_persons = float(input("enter no.of persons : "))
per_person=bill_amount/total_persons
print(f"each person should pay {per_person} rupees")