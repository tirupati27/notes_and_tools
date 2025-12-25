def formatted_text(obj):
  max_len=0
  for sr_no, method in enumerate(dir(obj), start=1):
    method=len(method)+7
    if method>max_len and sr_no%2!=0:
      max_len=method
  
  text=""
  for sr_no, method in enumerate(dir(obj), start=1):
    if sr_no%2==0:
      text=text+f"{sr_no}. {method}()\n"
    else:
      x=f"{sr_no}. {method}()"
      space=" "*(max_len-len(x))
      text=text+x+space
  
  return text



def export_to_html(obj,file_name):
  main_data=""
  for sr_no, method in enumerate(dir(obj), start=1):
    main_data=main_data+f"<tr>\n\t<td>{sr_no}.</td>\n\t<td>{method}()</td>\n</tr>\n"
  
  html_text=r"""<!---©Tirupati--->
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
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
      padding: 12px 10px;
      border-bottom: 1px solid #ccc;
    }

    th {
      background-color: #4CAF50;
      color: white;
      font-size: 1.1em;
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
    <h1>Methods Of Python's <span>"""+file_name+r"""</span> Object</h1>
    <table>
      <thead>
        <tr>
          <th>Sr.No</th>
          <th>Methods</th>
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
  
  #file_path=f"/Users/user/Desktop/Python's {file_name} Attributes.html"
  file_path=f"/storage/emulated/0/Android/Python's {file_name} Attributes.html"
  with open(file_path,"w") as file:
    file.write(html_text)
  
  return f'File "{file_path}" Saved Successfully !'



def main():
  python_objects = {
    "int": 42,
    "float": 3.14,
    "complex": 2 + 3j,
    "bool": True,
    "str": "Hello",
    "bytes": b"data",
    "bytearray": bytearray(b"data"),
    "list": [1, 2, 3],
    "tuple": (1, 2, 3),
    "set": {1, 2, 3},
    "frozenset": frozenset({1, 2, 3}),
    "dict": {"a": 1, "b": 2},
    "range": range(5),
    "NoneType": None,
    "function": lambda x: x,
    "builtin_function_or_method": len,
    "module": __import__("math"),
    "type": int,
    "ellipsis": ...,
    "NotImplementedType": NotImplemented,
    "memoryview": memoryview(b"abc"),
    "classmethod": classmethod(lambda cls: None),
    "staticmethod": staticmethod(lambda: None),
    "property": property(),
    "generator": (x for x in range(3)),
    "map": map(int, ['1', '2']),
    "filter": filter(bool, [0, 1, 2]),
    "zip": zip([1, 2], [3, 4]),
    "enumerate": enumerate([1, 2, 3]),
    "re.Match": __import__("re").match(r"\d+", "42"),
    "re.Pattern": __import__("re").compile(r"\d+"),
    "dict_keys": {"a": 1}.keys(),
    "dict_values": {"a": 1}.values(),
    "dict_items": {"a": 1}.items(),
    "set_iterator": iter({1, 2, 3}),
    "list_iterator": iter([1, 2, 3]),
    "tuple_iterator": iter((1, 2, 3)),
    "str_ascii_iterator": iter("abc"),
    "range_iterator": iter(range(3)),
    "dict_keyiterator": iter({"a": 1}.keys()),
    "dict_valueiterator": iter({"a": 1}.values()),
    "dict_itemiterator": iter({"a": 1}.items()),
    "bytes_iterator": iter(b"abc"),
    "bytearray_iterator": iter(bytearray(b"abc"))
  }
  
  print("\n",list(python_objects),sep="")
  choice=input("\nEnter Any Python's Object Name:\n>>>").lower()
  
  if choice not in python_objects:
    print("Object Not Found !")
      
  else:
    message=export_to_html(python_objects[choice],choice)
    print(f"\n{message}\n")
    consent=input("Would you like to print the methods here? (y/n): ").lower()
    
    if consent=="y":
      x=formatted_text(python_objects[choice])
      print(x)


if __name__=="__main__":
  main()