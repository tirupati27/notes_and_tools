n=int(input("Enter the number of rows: "))
print("----------Pattern_1------------")
for i in range(1,n+1):
  for j in range(1,i+1):
    print("*",end="")
  print()


print("----------Pattern_2------------")
for i in range(n,0,-1):
  for j in range(1, i+1):
    print("*", end="")
  print()


print("----------Pattern_3------------")
for i in range(1,n+1):
  print(" "*(n-i),end="")
  for j in range(1, i+1):
    print("*", end="")
  print()


print("----------Pattern_4------------")
for i in range(n,0,-1):
  print(" "*(n-i), end="")
  for j in range(1, i+1):
    print("*", end="")
  print()
  
  
print("----------Pattern_5------------")
z=2*n-1 #no. of stars in the last line
for i in range(1,n+1):
  a=2*i-1 #no. of stars in current line
  print(" "*int((z-a)/2),end="")
  print("*"*a,end="")
  print(" "*int((z-a)/2))


print("----------Pattern_6------------")
z=2*n-1 #no. of stars in the last line
for i in range(n,0,-1):
  a=2*i-1 #no. of stars in current line
  print(" "*int((z-a)/2),end="")
  print("*"*a,end="")
  print(" "*int((z-a)/2))
  
