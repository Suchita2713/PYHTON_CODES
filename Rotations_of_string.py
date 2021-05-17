def rotations(s,s1):
  s=s+s
  if s1 in s:
    return "YES"
  else:
    return "NO"
s="abcde"
s1="abced"
print(rotations(s,s1))
