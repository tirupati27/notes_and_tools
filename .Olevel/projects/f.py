n=int(input("Enter The Value of n: "))
def fibonacci(x, a=0, b=1):
  if x>0:
    print(a, end=", ")
    return fibonacci(x-1, b, a+b)

fibonacci(n)