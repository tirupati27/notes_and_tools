import json
import pathlib
import re
import subprocess



import readline
import atexit
historyFile=".NEW_CLI-HISTORY"
subprocess.run(f"touch {historyFile}",shell=True)
readline.read_history_file(historyFile)
atexit.register(readline.write_history_file, historyFile)
readline.set_history_length(100)




default_main_db={
"directory_db":[],
"setting_db":{
  "NAME":"Tirupati",
  "NAME-COL":"0;255;0",
  "PWD-COL":"200;100;100",
  "DIR-COL":"200;200;0",
  }
}

try:
  with open(".app_database.db","r") as file:
    main_db=json.load(file)
except FileNotFoundError:
  main_db=default_main_db

#Global Variables
dir_db=main_db["directory_db"]
set_db=main_db["setting_db"]
PWD=subprocess.run("pwd",shell = True, capture_output=True,text=True)
PWD=PWD.stdout[:-1]
success="\033[32mSuccess:\033[0m"
error="\033[31mError:\033[0m"
predefined_cmd={
  "add <directory>" : "To add a directory to the database",
  "add ." : "To add PWD to the database",
  "rem <directory_ref>": "To remove a directory from the database",
  "print" : "To print all your directories stored in the database",
  "set" : "To customise the App's settings",
  "exit" : "To exit from this python App",
  "copydb <fileName>" : "Copy the database of this app into another directory as specified file name"
}


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
  for key, value in predefined_cmd.items():
    print(f"==> {key}:- {value}\n")



def add_path_to_database(path):
  temp=subprocess.run(f'cd "{path}" && pwd',shell = True, capture_output=True,text=True)
  if temp.stdout!="":
    path=temp.stdout[:-1]
    path_parts=list(pathlib.Path(path).parts)
    if path_parts not in dir_db:
      dir_db.append(path_parts)
      save_updated_database()
      return f"{success} Added '{path}'"
    else:
      return f"Already Added '{path}'"
  else:
    return f"{error} '{path}' is NOT a Valid Directory"



def remove_path_from_database(x):
  #Searching 'dir.10' like text in x
  if re.search(r"^dir.[0-9]+$", x.lower()):
    i=int(x[x.find(".")+1:])-1
    if i in range(len(dir_db)):
      dir_db.pop(i)
      save_updated_database()
      return f"Successfully Removed {actual_command(x)}"
    else:
      return f"{error} '{x}' NOT Found In The Database"
  else:
    return f"{error} '{x}' NOT Found In The Database"


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
  while True:
    #Manipulating 'dir.10.1' like text in x
    if re.search(r"dir.[0-9]+.[0-9]+", x.lower()):
      #Here m is the exact match string like 'dir.10.1'
      m=re.search(r"dir.[0-9]+.[0-9]+", x.lower()).group()
      #dir.10.1 ==> dir.i.j
      i=int(m[m.find(".")+1:m.rfind(".")])-1
      j=int(m[m.rfind(".")+1:])-1
      try:
        path_parts=dir_db[i][:j+1]
      except IndexError:
        print(f"{error} Invalid Directory Reference '{m}'\n")
        return x
      actual_path=str(pathlib.Path(*path_parts))
      x=x.replace(m, f'"{actual_path}"')
    
    
    #Manipulating 'dir.10' like text in x
    elif re.search(r"dir.[0-9]+", x.lower()):
      #Here m is the exact match string like 'dir.10.1'
      m=re.search(r"dir.[0-9]+", x.lower()).group()
      #dir.10 ==> dir.i
      i=int(m[m.find(".")+1:])-1
      try:
        path_parts=dir_db[i]
      except IndexError:
        print(f"{error} Invalid Directory Reference '{m}'\n")
        return x
      actual_path=str(pathlib.Path(*path_parts))
      x=x.replace(m, f'"{actual_path}"')
    
    else:
      return x



def app_settings():
  global set_db
  def col(c):
    t=input("Enter RGB Color Code (like 255;255;255): ").strip()
    if re.search(r"[0-9]+;[0-9]+;[0-9]+", t):
      r=int(t[:t.find(';')])
      g=int(t[t.find(';')+1:t.rfind(';')])
      b=int(t[t.rfind(';')+1:])
      if r>255 or g>255 or b>255:
        print(f"{error} RGB Value Can't be greater than 255")
        col(c)
      else:
        if c==2: set_db['NAME-COL']=t
        elif c==3: set_db['PWD-COL']=t
        elif c==4: set_db['DIR-COL']=t
    else:
      print(f"{error} Color code must be in '255;255;255' format")
      col(c)
  
  
  print("1. User Name\n2. Color of User Name\n3. Color of PWD\n4. Color of Directory References\n5. Reset to Default")
  temp=input("\033[38;2;0;200;200mChoose Option/exit:\033[0m ").strip()
  if temp=="1":
    set_db["NAME"]=input("Enter New User Name: ").strip()
  elif temp=="2": col(2)
  elif temp=="3": col(3)
  elif temp=="4": col(4)
  elif temp=="5":
    main_db['setting_db']=default_main_db['setting_db']
    set_db=main_db["setting_db"]
  elif temp.lower()=="exit":
    return
  else:
    print(f"{error} Invalid Input !")
    app_settings()
  save_updated_database()





def copy_db(f):
  f=f.replace('"',"")
  try:
    with open(f,"w") as file:
      json.dump(main_db,file,indent=3)
      print(f"{success} file saved as {f}")
  except (FileNotFoundError, IsADirectoryError):
    print(f"{error} {f} is NOT a Valid Directory/fileName")
      




def bash_commandexecuter(cmd):
  global PWD
  if cmd[:3]=="cd " or cmd=="cd":
    temp=subprocess.run(f"{cmd} && pwd",shell = True, capture_output=True,text=True,cwd=PWD)
    if temp.stderr=="":
      PWD=temp.stdout[:-1]
    else:
      print(temp.stderr)
  else:
    subprocess.run(cmd,shell=True, cwd=PWD)





def main():
  subprocess.run("clear",shell = True)
  print(f"{'='*35}\n\033[1;93m\tWelcome To NEW_CLI\033[0m\n{'='*35}\n")
  print_directories()
  print("Type 'help' to get help")
  print("Enter any predefined/Bash command:")
  
  while True:
    user_cmd=input(f"\033[1;38;2;{set_db['NAME-COL']}m{set_db['NAME']}:\033[0m \033[38;2;{set_db['PWD-COL']}m{PWD}\033[0m \033[1;38;2;{set_db['NAME-COL']}m$\033[0m ").strip()
    
    if user_cmd.lower()=="help":
      show_help()
    
    elif user_cmd.lower()=="add .":
      print(add_path_to_database(PWD))
    
    elif user_cmd.lower()[:4]=="add ":
      path=actual_command(user_cmd[4:].strip())
      print(add_path_to_database(path))
    
    elif user_cmd.lower()[:4]=="rem ":
      path=user_cmd[4:].strip()
      print(remove_path_from_database(path))
    
    elif user_cmd.lower()[:7]=="copydb ":
      fileName=actual_command(user_cmd[7:].strip())
      copy_db(fileName)
      
    
    elif user_cmd.lower()=="print":
      print_directories()
    
    elif user_cmd.lower()=="set":
      app_settings()
    
    elif user_cmd.lower()=="exit":
      break
    
    else:
      user_cmd=actual_command(user_cmd,)
      bash_commandexecuter(user_cmd)

  
  
  
if __name__=="__main__":
  main()