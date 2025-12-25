import subprocess
def executer(sys, opt):
  pass







def Customizer(os):
  t=subprocess.run("cd /root",shell = True, capture_output=True,text=True)
  if os=='UBUNTU' and t.stdout=='':
    print("Please login and run this program inside the ubuntu environment to make changes for Ubuntu.")
    return
  def col(c):
    t=input("Enter RGB Color Code (like 255;255;255): ")
    if re.search(r"[0-9]+;[0-9]+;[0-9]+", t):
      r=int(t[:t.find(';')])
      g=int(t[t.find(';')+1:t.rfind(';')])
      b=int(t[t.rfind(';')+1:])
      if r>255 or g>255 or b>255:
        print("RGB Value Can't be greater than 255")
      else:
        if c==2: set_db['NAME-COL']=t
        elif c==3: set_db['CWD-COL']=t
        elif c==4: set_db['DIR-COL']=t
    else:
      print("Color code must be in '255;255;255' format")
  
    #------
    print("\n1. UserName\n2. Color of UserName\n3. Color of PWD\n4. Go to the Main Menu")
    user=input(f"\033[38;2;0;200;200mChoose Option, What you want to Customize for {os}\033[0m\n\033[1;91m:\033[0m ").strip()
    if user=="1":
      NAME=input("Enter the New UseName: ")
      executer(os,NAME)
    
    elif user=="2":
      executer(os,NAME_COL)
    
    elif user=="3":
      executer(os,PWD_COL)
    
    elif user=="4":
      break
    
    else:
      print("\033[31mError:\033[0m Invalid input !")
    





def main():
  print(f"\n{'-'*35}\n\033[1;38;2;0;200;200m  CLI Customizer\033[0m\n{'-'*35}\n")
  while True:
    print("\n\033[31mCutomize The Interface:\033[0m\n1. For Termux\n2. For Ubuntu\n3. Exit The App")
    user=input("\033[38;2;0;200;200mChoose Option:\033[0m ").strip()
    if user=="1":
      Customizer("TERMUX")
    
    elif user=="2":
      Customizer("UBUNTU")
    
    elif user=="3":
      break
    
    else:
      print("\033[31mError:\033[0m Invalid input !")


if __name__=="__main__":
  main()