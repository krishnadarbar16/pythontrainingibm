#dictionaries
#unordered
# key cannot have duplicate
#mutable
D = {
    "name":"krishna",
    "age":19,
    "profession":"teacher"
}

#print methods of dictionary , keys and  values
print(D)
print(D["name"])
print(D.keys())
print(D.values())

#modification of values in dict using 
D["name"]="classmate vedant"
print(D)

#a dictionary can contain list,sets,tuples and dict itself
d = {
    "name":["vedant","krishna","aaditya","niraj","jatin"],
    "friends":False,
    "batchmates":True,
    "laptop":{#dict inside a dict
        "brand":"ASUS",
        "cpu":"ryzen7",
        "gpu":"rtx3040"
    }
}

#accessing list and dict inside a dict
print(d["name"][3])
print(d["laptop"]["gpu"])

#updating a dictionary
d2={
    "name":"govinthan",
    "laptop":"gaming is best",
    "profession":"cheif"
}
d.update(d2)
print(d.items())  #this will print key value pairs grouped with each other

for i in d2.keys():
    print(i)
for i in d2.values():
    print(i)
for key,value in d2.items():
    print(key)
    print(value) 

print(d2.pop("name")) #pop removes and returns the value
