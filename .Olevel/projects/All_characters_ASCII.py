def export_to_html(main_data,file_path,x,y):
  html_text=r"""<!---©Tirupati--->
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-16" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0"/>
  <title>Student details</title>
  <style>
    body {
      background: linear-gradient(to right, #83a4d4, #b6fbff);
      font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
      margin: 0;
      padding: 0;
    }

    .container {
      max-width: 600px;
      margin: 50px auto;
      background: white;
      padding: 20px;
      border-radius: 15px;
      box-shadow: 0 0 20px rgba(0, 0, 0, 0.2);
    }

    h1 {
      margin-bottom: 50px;
      margin-top: 0px;
      color: #333;
      font-size: 2.2em;
      text-shadow: 1px 1px 2px #aaa;
    }
    
    h1>span{
      color: red;
    }

    table {
      width: 100%;
      border-collapse: collapse;
    }

    th, td {
      padding: 10px 2px;
      border-bottom: 1px solid #ccc;
      font-size: 0.7em;
    }

    th {
      background-color: #4CAF50;
      color: white;
    }

    tr:nth-child(even) {
      background-color: #f2f2f2;
    }

    tr:hover {
      background-color: #e0f7fa;
    }
    div.print{
      text-align: center;
      margin-bottom: 300px;
    }
    div.print>button {
      padding: 15px;
      font-size: 18px;
      font-weight: bold;
      color: white;
      background: linear-gradient(45deg, #4CAF50, #2E7D32);
      border: none;
      border-radius: 12px;
      cursor: pointer;
      box-shadow: 0 5px 15px rgba(0,0,0,0.2);
      transition: 0.3s ease;
    }
    
    div.print>button:hover {
      background: linear-gradient(45deg, #66BB6A, #388E3C);
      transform: scale(1.05);
    }
    
    @media print {
      div.print>button {
        display: none;
      }
      body {
        -webkit-print-color-adjust: exact !important;
        color-adjust: exact !important;
        print-color-adjust: exact !important;
      }
    }
    
    div.watermark {
      position: fixed;
      top: 50%;
      left: 50%;
      transform: translate(-50%, -50%) rotate(-30deg);
      font-size: 65px;
      color: rgba(0, 0, 0, 0.07);
      z-index: 1;
      pointer-events: none;
      user-select: none;
      white-space: nowrap;
    }
  </style>
</head>
<body>
  <div class="container">
    <div class="watermark">©Tirupati</div>
    <h1>All Characters With Their ASCII Values b/w"""+f""" {x} and {y}"""+r"""</h1>
    <table>
      <thead>
        <tr>
          <th>Dec. Value</th>
          <th>Character</th>
          <th>Dec. Value</th>
          <th>Character</th>
          <th>Dec. Value</th>
          <th>Character</th>
        </tr>
      </thead>
      <tbody>



"""+main_data+r"""


      </tbody>
    </table>
  </div>
  <div class="print">
    <button onclick="window.print()">🖨️ Print This Page</button>
  </div>
</body>
</html>
"""
  with open(file_path,"w") as file:
    file.write(html_text)
  
  return f'\nFile "{file_path}" Saved Successfully !\n'






def open_through_termux(path, file_name):
  import subprocess
  subprocess.run(f"am start -a android.intent.action.VIEW -d http://127.0.0.1:9000/{file_name}", shell=True, capture_output=True)
  cmd=f"cd {path} && python -m http.server 9000"
  subprocess.run(cmd,shell=True, capture_output=True, text=True)







def main_data_generator(x,y):
  #import os
  #path=os.getcwd()
  path="/storage/emulated/0/Android"
  file_name=f"/All_Characters_{x}-{y}.html"
  file_path=path+file_name
  
  main_data=r""
  temp=r""
  srn=x
  row=1
  printCount=1
  
  for i in range(x, y+1):
    #Skipping lone surrogate characters
    if i in range(55296,57343+1):
      continue
    temp=temp+f"  <td>{srn}.</td><td>{chr(i)}</td>\n"
    srn+=1
    if printCount%3==0 or i==y:
      main_data=main_data+f'<tr row="{row}">\n{temp}</tr>\n'
      temp=r""
      row+=1
    printCount+=1
  
  print(export_to_html(main_data,file_path,x,y))
  
  u=input("Do you want to open ? (y/n): ").lower().strip()
  if u=='y':
    open_through_termux(path, file_name)








def main():
  print(f"\n{'*'*40}\nExport All Characters with their ASCII values in a HTML File\n{'*'*40}\n")
  u=input("Enter Range (like 0-256): ").lower().strip()
  if '-' not in u:
    print("Invalid input !")
    return
  try:
    x=int(u[:u.find('-')].strip())
    y=int(u[u.find('-')+1:].strip())
  except ValueError:
    print("Invalid input !")
  
  if x>=0 and x<=y and y<=1114111:
    main_data_generator(x,y)
    
  else:
    print("Range must be 0-1114111")


if __name__=="__main__":
  main()