lst = []
for x in range(1000):
  if (x % 3 == 0) or (x % 5 == 0):
    lst.append(x)
print(sum(lst))