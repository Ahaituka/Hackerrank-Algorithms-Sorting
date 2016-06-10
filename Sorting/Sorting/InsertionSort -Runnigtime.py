
def insertion_sort(l):
    c=0
    for i in range(1, len(l)):
        j = i
        key = l[i]
        while (j > 0) and (l[j-1] > key):
           l[j] = l[j-1]
           j -= 1
           c+=1
        l[j] = key
    return c 


m = int(input().strip())
ar = [int(i) for i in input().strip().split()]
c=insertion_sort(ar)
print(c)