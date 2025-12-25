import requests

url=input("Enter URL: ")

try:
    response = requests.get(url)
    response.raise_for_status()
    HTML_content = response.text
except requests.exceptions.RequestException as e:
    print(f"Error fetching the URL: {e}")


#Saving the HTML_content data as File
try:
  fName=input("Enter The File Name (without extension): ")+".html"
  path=f"/storage/emulated/0/@@A-CODE/{fName}"
  #path=f"{fName}"
  with open(path,"w") as f:
    f.write(HTML_content)
  print(f"File {path} saved Successfully")
except FileNotFoundError:
  print("Invalid File Name or Path")