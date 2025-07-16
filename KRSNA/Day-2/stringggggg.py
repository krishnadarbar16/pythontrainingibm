s = ' aaaabcde fghij klmn opqr stuvw xyz  '
print(s)
print(len(s))   #returns length of string
print(s[25])    #returns charachter at index umber 25
print(s.upper())    #converts every char in upper case
print(s.lower())    #converts every char in lower case
print(s.title())    #capitalizes every words in first letter
print(s.capitalize())   #capitalizes only first words first letter
print(s.strip())    #removes the space at end and start of string
print(s.replace("abcde","gupabaslaudya"))
a=s.split() #converts atring into a list by taking each word as a different element
print(a)
b=" _ ".join(a)   #converts the list into a string by seperating each element by given charachters in the " "
print(b)
print(s[4:15])      #string slicing
print(s.count("a"))     #returns the no.of times the charachter occured
print(s.find("fghi"))
print(s.startswith(" aaa"))  #if correct then returns boolean value
print(s.endswith("qwertyu"))

name="vedant"
height=4.1
print(f"the height of {name} is {height} cuz he is dumnaaaa")

