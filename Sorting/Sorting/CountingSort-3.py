n = int(input())
a = []
for i in range(0,n):
    data=input().strip().split(' ')
    a.append(int(data[0]))


listofcounting = [0] * 100 #initializing a list of size 100 with zeroes
for i in range(0,100):
    x=a.count(i) #finding how many times the number apperas in the list
    listofcounting[i]+=x
    #sj

a=[]
sum=0
for i in range(0,100):
    if (listofcounting[i]):
        sum+=listofcounting[i]
        a.append(sum)
    if sum==a[i]:
        a.append(sum)
print(" ".join(map(str,a[1:])))



    
