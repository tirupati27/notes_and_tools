import subprocess
import tkinter
from tkinter import filedialog
import os

root=tkinter.Tk()
root.withdraw()

cright=u"\u00a9\u0054\u0069\u0072\u0075\u0070\u0061\u0074\u0069"
print(" "*20,cright)
print("\t--WELCOME TO C/C++ COMPILER INTERFACE--")

'''
print("\n>>> Press Enter to choose a file:",end="")
input()
'''

#Defining a function to compile and run the user file
stdErr=""
def output(cm):
    #print(cm)
    comp=subprocess.run(cm,shell=True,capture_output=True,text=True)
    global stdErr
    stdErr=comp.stderr
    if stdErr=="":
        print("\n>>> SUCCESSFULLY Compiled...Output is showing below.\n\n")
        subprocess.run(".\\"+exeFileName,shell=True,cwd=".\\bin")
    else:
        print("\n>>> You have following Errors in Your Program-")
        print("\n"+("-"*50)+"\n"+stdErr+("-"*50)+"\n")
        print(">>> Fix the above error and compile again...")

#Argument variables for "filedialog.askopenfilename()" function
desktop=os.path.join(os.path.expanduser("~"),"Desktop")
fileTypes=[("C language Files","*.c *.cpp"),("All Files","*.*")]    
#User file selection through "filedialog.askopenfilename()" function
userFilePath=filedialog.askopenfilename(title=cright,initialdir=desktop,filetypes=fileTypes)
root.destroy()
invalidFileMessage='\n\n>>> INVALID File Selection !...Please Select a valid ".c" or ".cpp" file.'
if userFilePath=="":
    print(invalidFileMessage)
else:
    #Extraction of fileName,extension,etc. for further use
    userFileName=os.path.basename(userFilePath)
    tempArr=userFileName.split(".")
    exeFileName=tempArr[0]+"_"+cright+".exe"
    userFileExt="."+tempArr[1].upper()
    if userFileExt==".C":
        output('.\\bin\\clang.exe "'+userFilePath+'" -o "'+exeFileName+'"')
    elif userFileExt==".CPP":
        output('.\\bin\\clang++.exe "'+userFilePath+'" -o "'+exeFileName+'"')
    else:
        print(invalidFileMessage)

'''
#Getting the compilation error message into .txt file
ff=open("####errorMessage.txt","w")
ff.write("stderr:"+"\n"+("-"*50)+"\n"+stdErr+("-"*50)+"\n")
ff.close
'''

print("\n\n>>> Press Enter to Exit...["+cright+"]",end="")
input()

