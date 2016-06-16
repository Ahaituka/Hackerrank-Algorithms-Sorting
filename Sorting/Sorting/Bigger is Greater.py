"""Algo:1.Take letter
        2.Permutate and store in a list say perms
        3.Then sort  into a list
        4.Compare list with the inut string and get the matched index say x
        5.Print perms[x+1] """


from itertools import permutations
n=int(input())
for i in range(n):
      a=input()
      perms = [''.join(p) for p in permutations(a)]
      perms.sort()
      x=perms.index(a)
      if(perms[x+1]==a):
          print("no answer")
      else:
        print(perms[x+1])
#sj      