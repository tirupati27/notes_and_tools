import json
import os
import pathlib
import re
import subprocess



try:
  with open(".app_database.db","r") as file:
    main_db=json.load(file)
except FileNotFoundError:
  main_db={
"dir_db":[],
"setting_db":{
  "NAME":"Tirupati",
  "NAME-COL":"0;255;0",
  "CWD-COL":"220;100;100",
  "DIR-COL":"200;200;0",
  }
}

dir_db=main_db["dir_db"]
set_db=main_db["setting_db"]



def save_updated_database():
  with open(".app_database.db","w") as file:
    json.dump(main_db,file,indent=3)



def show_help():
  sep=f"\n{'='*35}\n"
  print(sep+"\t\033[1;93mObjective Of This App\033[0m"+sep)
  print("The main objective of this application is to provide an over the top (OTT) command line interface,\n\t where you can execute all the bash commands without writing the full & long directory.\n\tInstead of this, you can only write a very short reference of the directory.")
  print(sep+"\t\033[1;93mExamples: How To Use Reference of Directory\033[0m"+sep)
  print("Let suppose we have a directory in the database i.e.\n\nDIR.1 == 'storage/emulated/Android/data'\n(notice that, DIR.1 have 4 parts, seperated with the Slash)\n\n\tNow, Read carefully the following Exaples command.\n\tIn each example the commands written in the left and right side of '==' will works absolutely same.")
  print('''
1. 'cd storage/emulated/Android/data' == '\033[36mcd dir.1\033[0m'

2. 'cd storage/emulated' == '\033[36mcd dir.1.2\033[0m'

3. 'mv a.png storage/NewFolder' == '\033[36mmv a.png dir.1.1/NewFolder\033[0m'

4. 'rm storage/emulated/Android/data/a.py' == '\033[36mrm dir.1/a.py\033[0m'

5. 'rm -r storage/emulated/Android' == '\033[36mrm -r dir.1.3\033[0m'

6. 'rm storage/emulated/file.jpg' == '\033[36mrm dir.1.2/file.jpg\033[0m'

''')
  print("\tSo, you don't have to write the full & long directory in your commands. Instead of this, you can only write a very short reference of the directory")
  print(sep+"\t\033[1;93mExplanation of Predefined Commands\033[0m"+sep)
  print("=> add :- To add a directory to the database\n\n=> addpwd:- To add PWD to the database\n\n=> rem :- To remove a directory from the database\n\n=> print :- To print all your directories stored in the database\n\n=> set:- To customise the App's settings\n\n=> exit :- To exit from this python App\n")



def add_path_to_database(path):
  if os.path.isdir(path):
    path_parts=list(pathlib.Path(path).parts)
    if path_parts not in dir_db:
      dir_db.append(path_parts)
      save_updated_database()
      return "Successfully Added!"
    else:
      return "Already Added!"
  else:
    return "It's Not a Valid Directory In Your Computer"



def remove_path_from_database(path):
  path_parts=list(pathlib.Path(path).parts)
  try:
    dir_db.remove(path_parts)
    save_updated_database()
    return "Successfully Removed!"
  except ValueError:
    return "No Directory Found to Remove!"



def print_directories():
  if len(dir_db)==0:
    print("You don't have any directory in the database!\n")
  else:
    count=1
    for i in dir_db:
      path=str(pathlib.Path(*i))
      print(f"\033[38;2;{set_db['DIR-COL']}mDIR.{count}\033[0m == '{path}'\n")
      count+=1



def actual_command(x):
  global cwd
  while True:
    #Manipulating 'dir.10.1' like text in x
    if re.search(r"dir.[0-9]+.[0-9]+", x.lower()):
      m=re.search(r"dir.[0-9]+.[0-9]+", x.lower()).group()
      i=int(m[m.find(".")+1:m.rfind(".")])-1
      j=int(m[m.rfind(".")+1:])-1
      try:
        temp=dir_db[i][:j+1]
        path=str(pathlib.Path(*temp))
        x=x.replace(m,f"'{path}'")
      except IndexError:
        print(f"Invalid Directory Reference '{m}'\n")
        return x
    
    #Manipulating 'dir.10' like text in x
    elif re.search(r"dir.[0-9]+", x.lower()):
      m=re.search(r"dir.[0-9]+", x.lower()).group()
      i=int(m[m.find(".")+1:])-1
      try:
        temp=dir_db[i]
        path=str(pathlib.Path(*temp))
        x=x.replace(m,f"'{path}'")
      except IndexError:
        print(f"Invalid Directory Reference '{m}'\n")
        return x
      
    else:
      break
  
  if x[:3]=="cd " or x=="cd":
    temp=subprocess.run(x+" && pwd",shell = True, capture_output=True,text=True,cwd=cwd)
    if temp.stdout!="":
      cwd=temp.stdout[:-1]
      return ""
  
  return x



def app_settings():
  global set_db
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
  
  print("1. User Name\n2. Color of User Name\n3. Color of PWD\n4. Color of Directory References\n5. Reset to Default")
  
  temp=input("\033[38;2;0;200;200mChoose Option:\033[0m ")
  if temp=="1":
    set_db["NAME"]=input("Enter New User Name: ")
  elif temp=="2": col(2)
  elif temp=="3": col(3)
  elif temp=="4": col(4)
  elif temp=="5":
    main_db['setting_db']={
    "NAME":"Tirupati",
    "NAME-COL":"0;255;0",
    "CWD-COL":"220;100;100",
    "DIR-COL":"200;200;0",
    }
    set_db=main_db["setting_db"]
  else:
    print("Invalid Input !")
  save_updated_database()


def main():
  global cwd
  cwd=subprocess.run("pwd",shell = True, capture_output=True,text=True)
  cwd=cwd.stdout[:-1]
  
  subprocess.run("clear",shell = True)
  
  print(f"{'='*35}\n\033[1;93m  Welcome To NEW_CLI   v-1.0\033[0m\n{'='*35}\n")
  print_directories()
  print("Predefined Commands Are:\n[help, add, addpwd, rem, print, set, exit]")
  print("Enter any predefined/Bash command:")
  
  while True:
    command=input(f"\033[1;38;2;{set_db['NAME-COL']}m{set_db['NAME']}:\033[0m \033[38;2;{set_db['CWD-COL']}m{cwd}\033[0m \033[1;38;2;{set_db['NAME-COL']}m$\033[0m ")
    
    if command.lower()=="help":
      show_help()
    
    elif command.lower()=="add":
      user=input("Enter the directory to add into database\n\033[1;91m:\033[0m ")
      user=actual_command(user)
      print(add_path_to_database(user))
    
    elif command.lower()=="addpwd":
      print(add_path_to_database(cwd))
    
    elif command.lower()=="rem":
      user=input("Enter the directory to remove from database\n\033[1;91m:\033[0m ")
      user=actual_command(user)
      print(remove_path_from_database(user))
    
    elif command.lower()=="print":
      print_directories()
    
    elif command.lower()=="set":
      app_settings()
    
    elif command.lower()=="exit":
      break
    
    else:
      command=actual_command(command)
      subprocess.run(command,shell=True, cwd=cwd)
  
  
  
if __name__=="__main__":
  main()