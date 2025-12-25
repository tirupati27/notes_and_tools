def checkArm(n):
        backup=n
        #finding length of the number
        length=0
        while n>0:
            length+=1
            n=n//10
        n=backup
        arm=0
        while n>0:
            d=n%10
            arm=arm+d**length
            n=n//10
        if backup==arm: return True
        return False
        

print("--WELCOME TO ARMSTRONG NUMBER PRINTING INTERFACE--@tirupati")
print("\t\t--PYTHON--\n")

user=int(input("How many Armstrong number do you want to print: "))
printCount=0
num=10
while True:
    if checkArm(num):
        printCount+=1
        print(printCount,"=>",num)
    if user==printCount: break
    num+=1
    
print("\n             ------THANK_YOU-----")




