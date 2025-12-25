def python_file_executor(file_path):
  try:
    with open(file_path,'r') as file:
      code=file.read()
      exec(code)
  except FileNotFoundError:
    print(f'FILE {file_path} NOT FOUND !')
    
python_file_executor("/storage/emulated/0/@@A-CODE/calc.py")
import os
print(os.getcwd())