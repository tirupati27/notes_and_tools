d={"rahul":20,"aman":100,"ramu":20,"Sachin":50}

# 1. sorting by key
L=[]
for i in sorted(d.keys()):
  L.append([i,d[i]])

d=dict(L)
print("Sorted by key:", d)




# 2. sorting by value
L=[]
for i in sorted(d.values()):
  for j in d.keys():
    if d[j]==i:
      L.append([j,i])

d=dict(L)
print("Sorted by value:", d)
