import subprocess
print()
print(">>0. /data/data/com.termux/files/home")
print(">>1. @@A-CODE")
print(">>2. @@A-CODE/Template")
print(">>3. @@A-CODE/TERMUX")
print(">>4. Shared")
print(">>5. Shared/Download")
print(">>6. Shared/Android")
print()
print(">>7. /data/data/com.termux")
print(">>8. com.termux/files/usr/lib/python3.12/")
print(">>111. Copy any file to all the directories")
print(">>112. Remove any file from all the directories")

user=int(input("\nChoose Option: "))
#subprocess.run("clear",shell=True)
base='"/data/data/com.termux/'
arr=[
  base+'files/home/"',
  base+'files/home/storage/shared/@@A-CODE/"',
  base+'files/home/storage/shared/@@A-CODE/Template/"',
  base+'files/home/storage/shared/@@A-CODE/TERMUX/"',
  base+'files/home/storage/shared/"',
  base+'files/home/storage/shared/Download/"',
  base+'files/home/storage/shared/Android/"',
  base+'"',
  base+'files/usr/lib/python3.12/"',
]

if user in range(len(arr)):
  subprocess.run("cd "+arr[user],shell=True)
elif user==111:
  f=input("Enter the file Name: ")
  for i in arr:
    subprocess.run("cp "+f+" "+i,shell=True, capture_output=True)
  print("Successfully Copied!")
elif user==112:
  f=input("Enter the file Name: ")
  for i in arr:
    subprocess.run("rm "+i+f,shell=True, capture_output=True)
  print("Successfully Removed!")
else: print("\tINVALID INPUT!")