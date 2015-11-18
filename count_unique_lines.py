with open('anwserid.txt') as f:
  content = f.readlines()

s = set(content)
c = len(s)
print(c)
