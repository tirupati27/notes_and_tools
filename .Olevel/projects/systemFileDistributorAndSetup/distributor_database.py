file_data={
  
  "git config system level" : "/data/data/com.termux/files/usr/etc/gitconfig",
  
  "git config global level" : "/data/data/com.termux/files/home/.gitconfig",
  
  "Termux bashrc with PS1" : "/data/data/com.termux/files/home/.bashrc",
  
  "Ubuntu bashrc with PS1" : "/root/.bashrc",
  
  "NEW_CLI.py" : "/data/data/com.termux/files/home/a",
  
  "NEW_CLI's database" : "/data/data/com.termux/files/home/.app_database.db",
  
  "Termux bash history" : "/data/data/com.termux/files/home/.bash_history",
  
  "Termux default mirror set" : "/data/data/com.termux/files/usr/etc/apt/sources.list",
  
  
}




#database testing function
def testing():
  error=False
  
  for i in file_data.keys():
    try:
      with open(i,'r') as f:
        pass
    except FileNotFoundError:
      error=True
      print(f"\033[31mError:\033[0m File '{i}' Not Found")
      
  
  for i in file_data.values():
    try:
      with open(i,'r') as f:
        pass
    except FileNotFoundError:
      error=True
      print(f"\033[31mError:\033[0m Either directory error or file '{i}' Not Found")
      
  if not error:
    print("Everything is okay")




if __name__=="__main__":
  testing()