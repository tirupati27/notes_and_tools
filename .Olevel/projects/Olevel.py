while True:
  print("-"*40)
  print("Que 1. Checking Krishnamurthy Number")
  print("Que 2. Greatest digit of a Number")
  print("Que 3. Addition & subtraction of 2 Numbers")
  print("Que 4. Swap of two variables using function")
  print("Que 5. Odd/Even using function")
  print("Que 6. 10 natural number using function")
  print("Que 7. Printing Table of a number")
  print("Que 8. Checking factorial/Palindrome/Prime number")
  print("Que 9. factorial of a number using Recursion")
  print("Enter 'exit' to exit the program")
  print("-"*40)
  
  
  user=input("Enter the question number: ")
  
  
  if user=="1":
    n=int(input("Enter a number: "))
    backup=n
    sum=0
    while n!=0:
      d=n%10
      fact=1
      for i in range(1,d+1):
        fact=fact*i
      sum=sum+fact
      n=n//10
    if sum==backup:
      print(backup,"is a Krishnamurthy number !")
    else:
      print(backup,"is NOT a Krishnamurthy number !")
  
  
  elif user=="2":
    n=int(input("Enter a number: "))
    greatest=0
    while n!=0:
      d=n%10
      if d>greatest:
        greatest=d
      n=n//10
    print(greatest,"is the Greatest digit in the number !")
    
    
  elif user=="3":
    a=int(input("Enter number A: "))
    b=int(input("Enter number B: "))
    def calc(num1,num2):
      print("A+B =",a+b)
      print("A-B =",a-b)
    calc(a,b)
    
  
  elif user=="4":
    a=int(input("Enter value A: "))
    b=int(input("Enter value B: "))
    def calc(num1,num2):
      global a,b
      c=a
      a=b
      b=c
      print("A =",a)
      print("B =",b)
    calc(a,b)
    
    
  elif user=="5":
    n=int(input("Enter a number to check Odd/Even: "))
    def check(n):
      if n%2==0: return "Number is Even"
      return "Number is Odd"
    print(check(n))
    
    
  elif user=="6":
    n=int(input("Enter a number to print next 10 natural numbers: "))
    def natural(n):
      for i in range(n,n+11):
        print(i,end=", ")
      print()
    natural(n)
    
    
  elif user=="7":
    n=int(input("Enter a number to print it's table: "))
    def table(n):
      print("Table of",n,"is: ")
      for i in range(1,11):
        print(i*n, end=", ")
      print()
    table(n)
    
    
  elif user=="8":
    n=int(input("Enter a number: "))
    def multiTask(n):
      fact=1
      for i in range(1,n+1):
        fact=fact*i
      print("Factorial of",n,"is:",fact)
      
      backup=n
      rev=0
      while n!=0:
        d=n%10
        rev=rev*10+d
        n=n//10
      if backup==rev:
        print(backup,"is a palindrome number!")
      else:
        print(backup,"is Not a palindrome number!")
      
      n=backup
      count=0
      for i in range(1,n+1):
        if n%i==0:
          count=count+1
      if count==2:
        print(n,"is a prime number")
      else:
        print(n,"is NOT a prime number")
    multiTask(n)
    
    
  elif user=="9":
    n=int(input("Enter a number: "))
    def factorial(n):
      if n==1:
        return 1
      return n*factorial(n-1)
    print("Factorial of",n,"is",factorial(n))
    
    
  elif user.lower()=="exit":
    break
  else:
    print("Invalid Input!")