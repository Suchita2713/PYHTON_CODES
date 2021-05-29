# Missing no. in a array

def func(n,arr):
  return n*(n+1)//2-sum(arr)

n=int(input())
a=[]
for i in range(n):
  a.append(int(input()))
print(func(n,a))
  
