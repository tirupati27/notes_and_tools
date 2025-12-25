import random
for i in range (0,10):
  a = random.randint(0,100)
  b = random.randint(0,100)
  c = random.randint(0,100)
  
  print("A=",a)
  print("B=",b)
  print("C=",c)
  
  arr=[a,b,c]
  arr.sort(reverse=True)
  print(arr[0],"is Greatest")
  
  
  #Seperator
  print("------------------------------")