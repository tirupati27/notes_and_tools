while True:
    z=int(input("\nHow many Armstrong Number do you want to print: "))
    num=10
    printCount=0
    while True:
        num=str(num)
        arm=0
        for item in num:
            arm = arm+int(item)**len(num)
        if arm==int(num):
            printCount+=1
            print(printCount,"=>", arm)
        if printCount==z: break
        num=int(num)+1
    print("Note:- 0,1,2,3,4,5,6,7,8,9 are also Armstrong Numbers !")




