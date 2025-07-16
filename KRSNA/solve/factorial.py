def fact(n):
    ans=1
    while True:
        if(n==0):
            print(ans)
            break
        ans=ans*n
        n=n-1
fact(6)

import math
def area(radius):
    area=math.pi*(math.pow(radius,2))
    print(area)    
area(10)

