tup1=(1,2,3,"abc")
print(tup1)
print(tup1[3])
print(tup1*2)
tup2=(4,5,6,'def')
print(tup1+tup2)
#tuple will always return a tuple by creating a new tuple

#tuple methods

#.count()
t1 =(1,2,3,3,4,4,5,5,5,5)
print(t1.count(5))  #returns no.of selected element in the tuple
print(t1.index(3))  #returns index number of the selected numbers first occurance

#tuple unpackingggggggg
# name="alice"
# age = 24
# profession = "teacher"
#above three lines can be written by below tupple
t11 = ("alice",24,"teacher")
name,age,profession=t11
print(name)
print(age)
print(profession)










