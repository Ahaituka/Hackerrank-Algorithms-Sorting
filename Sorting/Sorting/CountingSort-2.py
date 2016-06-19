
        
m = int(input().strip())
a = [int(x) for x in input().split()] #to input list
listofcounting = [0] * 100 #initializing a list of size 100 with zeroes
for i in range(0,100):
    x=a.count(i) #finding how many times the number apperas in the list
    listofcounting[i]+=x
    #sj

a=[]
for i in range(0,100):
    for j in range(0,listofcounting[i]):
        a.append(i)
print(" ".join(map(str,a)))

