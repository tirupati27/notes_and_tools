import random
for i in range (0,10):
  a = random.randint(0,100)
  b = random.randint(0,100)
  c = random.randint(0,100)
  
  print("A=",a)
  print("B=",b)
  print("C=",c)
  
  #Condition 1
  if a == b == c:
      print("All numbers are equal!")
  #Condition 2
  elif a >= b and a >= c:
      if a == b:
          print("A and B are greatest!")
      elif a == c:
          print("A and C are greatest!")
      else:
          print("A is greatest!")
  #Condition 3
  elif b >= a and b >= c:
      if b == c:
          print("B and C are greatest!")
      else:
          print("B is greatest!")
  #Condition 4
  else:
      print("C is greatest!")
  #Seperator
  print("------------------------------")