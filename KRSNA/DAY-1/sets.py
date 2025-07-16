#sets
# unordered
# partially mutabl  -> modified via methods
# does not allow duplicates
c={1,2,3,4,5,1,3,2,5}
print(c)
# print(c[3])    this will give error as set is unordered
c.add(10000) #will add element at a random position as it is unordered'
c.remove(1) #will remove if element exist or else error
print(c)
c.discard(1)#it will remove element if exists otherwise no change
print(c)
print(len(c))          
d={7,8,9,0,9,99,88,77,776}
c.update(d)     
print(c)

c.clear()
print(c)

empty =set() #way to declare empty set

#set operations
A = {1,2,3,4}
B = {3,4,5,6}

#will return set with all elements from set1 and set2 uniquely
print(A.union(B))
print(A|B)

#wil return set with elements common in both set1 and set2
print(A.intersection(B))
print(A&B)

#elements that are in A but not in B
print(A-B)
print(A.difference(B))

#symmetric difference will return elements that are not common in both sets
print(A.symmetric_difference(B))
print(A^B)

#froznset---completely immutable cannot even perform .remove,.add ,etc.......................................
e=frozenset([1,2,3,4])
print(e) 

