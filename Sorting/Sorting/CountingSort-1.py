
        
m = int(input().strip())
a = [int(x) for x in input().split()]
listofcounting = [0] * 100
for i in range(0,100):
    x=a.count(i)
    listofcounting[i]+=x
    #sj
    
print(" ".join(map(str,listofcounting)))

