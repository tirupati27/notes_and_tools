def q1():
  string=input("Enter a string: ")
  lst=list(string[0])
  for i in string:
    if i!=lst[-1]:
      lst.append(i)
  
  print("".join(lst))
  
def q2():
  lst=list(range(1,21))
  while len(lst)>2:
    c=0
    for i in range(len(lst)):
      if i%3==2:
        print(lst.pop(i-c), end=", ")
        c+=1
    print()
  print(lst)
      

def q3():
  import datetime
  
  d=int(input("Enter day: "))
  m=int(input("Enter month: "))
  y=int(input("Enter year: "))
  date=datetime.date(y,m,d)
  a=datetime.date(2020,1,1)
  b=datetime.date(2020,12,31)
  
  if a<=date<=b:
    day={0:"Monday",1:"Tuesday",2:"Wednesday",3:"Thursday",4:"Friday",5:"Saturday",6:"Sunday"}
    print(f"The Day for date {d}/{m}/{y} is: {day[date.weekday()]}")
  
  else:
    print("Please Enter a date between 1/1/2020 and 31/12/2020")

def q4():
  L=[10,20,30,3,9,11]
  
  def isprime(n):
    if n<=1:
      return False
    for i in range(2,n):
      if n%i==0:
        return False
    return True
  
  for i in L:
    if isprime(i):
      print(i,"is the first prime number in the list.")
      break
  else:
    print("No prime number in the list.")

def q5():
  sum=0
  for i in range(1, 100+1):
    if i%2!=0:
      sum=sum+i
  print("The sum of odd no. between 1 and 100 is:",sum)
  
  c=1
  sum=0
  for i in range(5):
    n=int(input(f"Enter the no. {c}"))
    sum=sum+n
    c=c+1
  print("The sum of 5 no. is:",sum)


def q6():
  import math
  c=1
  sum=0
  for i in range(3):
    n=int(input(f"Enter the no. {c}"))
    sum=sum+math.sqrt(n)
    c=c+1
  print("The sum of square root of 3 no. is:",sum)

def q7():
  def isDisarium(n):
    c=1
    sum=0
    for i in str(n):
      sum=sum+(int(i)**c)
      c=c+1
    if sum==n:
      return True
    else:
      return False
  
  
  for i in range(1,200+1):
    if isDisarium(i):
      print(i)
      
q7()