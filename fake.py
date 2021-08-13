from collections import Counter

a = Counter([1,2,3,1,2,5,3])
b={1:1,2:2,4:1}
a.subtract(b)
print (a)
for (x,y) in a.items():
    print (x,y)
