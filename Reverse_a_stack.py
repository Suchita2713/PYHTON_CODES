#Reverse a stack that refrences to the same stack
def rev(s1,s2):                      #using Recursion Stack
  print(s1)
  while len(s1)!=1:
      ele=s1.pop()
      s2.append(ele)
  last=s1.pop()
  while len(s2)!=0:
      ele=s2.pop()
      s1.append(ele)
  rev(s1,s2)
  s1.append(last)
  
n=int(input())
s1=[]
s2=[]
for i in range(n):
  s1.append(int(input()))
rev(s1,s2)
while len(s1)!=0:
    print(s1.pop(),end=" ")
