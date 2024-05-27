n=input()
n=n.capitalize()

for i in range(len(n)):
  if n[i] == '_' and i+1<len(n):
      n= n[:i+1] + n[i+1].capitalize() + n[i+2:]
n=n.split('_')
print("".join(n))

