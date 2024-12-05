with open("data.txt") as f:
    lines = f.readlines()

a1 = []
a2 = []
for line in lines:
    e1, e2 = ([int(x.strip()) for x in (line.split("   "))])
    a1.append(e1)
    a2.append(e2)
    
a1.sort()
a2.sort()

dist = 0
for index, item in enumerate(a1):
    dist += abs(item-a2[index])

print(dist)
