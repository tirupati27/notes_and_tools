from distributor_database import file_data


def distributor(f):
  try:
    with open(f,'r') as f1:
      with open(file_data[f],'w') as f2:
        f2.write(f1.read())
    print(f"\033[32mSuccess:\033[0m file '{f}' distributed as '{file_data[f]}'\n")
    
  except FileNotFoundError:
    print(f"\033[31mError:\033[0m Either File '{f}' or Directory '{file_data[f]}' Not found\n")




def print_options():
  print("\n0. Distribute ALL the files showing below.")
  for sr_no, i in enumerate(file_data,start=1):
    print(f"{sr_no}. {i}")




def main():
  print(f"\n{'-'*35}\n\033[1;38;2;0;200;200m  System File Distributor\033[0m\n{'-'*35}\n")
  
  while True:
    print_options()
    user=input("\033[38;2;0;200;200mChoose Option/exit:\033[0m ").strip()
    if user.lower()=="exit":
      return
    try:
      user=int(user)
    except ValueError:
      pass
    
    if user==0:
      for f in file_data:
        distributor(f)
    
    elif user in range(1,len(file_data)+1):
      f=list(file_data.keys())[user-1]
      distributor(f)
    
    else:
      print("\033[31mError:\033[0m Invalid Input")
  

if __name__=="__main__":
  main()
