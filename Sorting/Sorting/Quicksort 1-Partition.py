def quick_sort(l):
    left=[]
    right=[]
    equal=[]
    for i in range(0, len(l)):
        p=l[0]
        if(l[i]==p):
             equal.append(l[i])
        elif(l[i]<p):
             left.append(l[i])
        else:
             right.append(l[i])
    x=left+equal+right
    l[:]=x

        
        

m = int(input().strip())
ar = [int(i) for i in input().strip().split()]
quick_sort(ar)
print(" ".join(map(str,ar)))