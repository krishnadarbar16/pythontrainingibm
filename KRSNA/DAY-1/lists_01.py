#lists
a=[1,2,3,"string",True,[1,23,4,5]]
print(a)
print(type(a))
print(a[3])
print(a[5][1]) #element from list inside the list
a[3]=1254  #directly modify the list
print(a)

#slicing a list
b=["apple","ball","cat","dog","elephANT"]
print(b[1:4])
print(b[2:])

#negative indexing
print(b[-3])
print(b[-3:])

#.remove
b.remove("dog")
print(b)

#.append
b.append("deathhh") #will add element at the end of list
print(b)

#.pop()
b.pop()  #will remove the last element by default
print(b)

#.index
print(b.index("cat")) #will return index number of given element
#if the selected element is not present it shows error

#sort
t=[4,2,6,5,9,1,12,0,94]
t.sort()  #arrange in ascending order
print(t)
t.sort(reverse=True)  #arrange in descending order
print(t)

#.reverse
x=[1,2,"sfgrtgv",True,False]
x.reverse()
print(x)  #reverse the order of elements
#clear
x.clear()    #deletes all the elements in the list
print(x)


#reassigning of lists
list1 = ['a','b','c','d','e']
list2 = list1
print(list1)    #the elements of list Are reassigned to list 2
print(list2)    #if any changes in one anathor will also be change
list2.remove('c')
print(list1)    

#copying the lists
l1 = [1,2,3,4,5,6,7]
l2 = l1.copy()
print(l1)
print(l2)
l1.remove(1)
print(l1)
print(l2)




