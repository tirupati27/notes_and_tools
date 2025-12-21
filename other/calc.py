def ci():
  while True:
    print("\n-Compound Interest Calculator_\u00a9\u0054\u0069\u0072\u0075\u0070\u0061\u0074\u0069-")
    p=float(input("\nEnter Pricipal Amount: "))
    r=float(input("Enter the Rate (without % symbol): "))
    t=float(input("Enter Time (in Years): "))
    n=float(input("Enter compounding frequency in one year: "))
    a=round(p*((1+(r/(n*100)))**(n*t)),4)
    EAR=round(((1+(r/(n*100)))**n)-1,4)
    print("-------------------------")
    print("=>The Interest for",t,"Years @",r,"% is:",a-p)
    print("=>Total amount is :",a)
    print("=>The EAR is :",EAR*100,"%",)
    print("-------------------------")
    if input("Do you want to exit (y/n): ")=='y':
      print("\t---Thank_You---")
      break
    
def roi():
  while True:
    print("\n-FD's EAR Calculation_\u00a9\u0054\u0069\u0072\u0075\u0070\u0061\u0074\u0069-")
    r=float(input("\nEnter The Annual Nominal Rate: "))
    EAR=((1+(r/(4*100)))**4)-1
    print("-------------------------")
    print("=>The EAR is :",round(EAR*100,4),"%",)
    print("-------------------------")
    if input("Do you want to exit (y/n): ")=='y':
      print("\t---Thank_You---")
      break
    
def recharge():
  while True:
    print("\n-Recharge Plan Comparison_\u00a9\u0054\u0069\u0072\u0075\u0070\u0061\u0074\u0069-")
    p=float(input("\nPlan 1-\nEnter recharge Amount: "))
    v=int(input("Enter Validity (in days): "))
    p1=round(p/v,3)
    p=float(input("Plan 2-\nEnter recharge Amount: "))
    v=int(input("Enter Validity (in days): "))
    p2=round(p/v,3)
    print("-------------------------")
    if p1<p2: print("Plan 1 is better, Because-\nPlan 1 per day cost is: ₹",p1,"\nPlan 2 per day cost is: ₹",p2)
    elif p2<p1: print("Plan 2 is better, Because-\nPlan 1 per day cost is: ₹",p1,"\nPlan 2 per day cost is: ₹",p2)
    else: print("Both Plans are same at the cost of ₹",p1,"per day.")
    print("-------------------------")
    if input("Do you want to exit (y/n): ")=='y':
      print("\t---Thank_You---")
      break
    
while True:
  print("\n-Welcome to Daily Routine Calculator_\u00a9\u0054\u0069\u0072\u0075\u0070\u0061\u0074\u0069-\n1. Recharge Plan Comparison\n2. Compound Interest Calculator\n3. FD's EAR Calculation\n4. Exit The App.")
  opt=input("Enter the option Number: ")
  if opt=='1': recharge()
  elif opt=='2': ci()
  elif opt=='3': roi()
  elif opt=='4': break
  else: print("\t---Invalid Input---")
