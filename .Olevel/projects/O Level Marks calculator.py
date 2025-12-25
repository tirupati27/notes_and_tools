print("\t---O LEVEL Marks Calculator_\u00a9\u0054\u0069\u0072\u0075\u0070\u0061\u0074\u0069---")
while True:
    t=int(input("\nEnter Theory marks: "))
    p=int(input("Enter Practical marks: "))
    if t>100 or p>100: print("Invalid marks input !")
    else:
        n=(t*(60/100))+(p*(40/100))
        print(f"The Total marks is: {round(n,2)}",end=" =>")
        if t<33 or p<33: print("(Fail)")
        else:
            if n>=85: print("(S-grade)")
            elif n>=75: print("(A-grade)")
            elif n>=65: print("(B-grade)")
            elif n>=55: print("(C-grade)")
            elif n>=50: print("(D-grade)")
            else: print("(Fail)")
