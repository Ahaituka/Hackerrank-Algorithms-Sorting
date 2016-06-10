
#def insertionSort(a):
#	for i in range(1,len(a)):
#		base=a[i]
#		pos=i


#		while pos>0 and base<a[pos-1]:
#			a[pos]=a[pos-1]
#			pos=pos-1


#		a[pos]=base

#a = [54,26,93,17,77,31,44,55,20]
#insertionSort(a)
#print(a)

n=int(input())		
a = [int(x) for x in input().split()]
for i in range(1,len(a)):
		base=a[i]
		pos=i


		while pos>0 and base<a[pos-1]:
			a[pos]=a[pos-1]
			pos=pos-1
		a[pos]=base
		print(' '.join(map(str,a)
