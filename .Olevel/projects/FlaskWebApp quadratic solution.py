'''----Main Code starts Here----'''
import math
def rajneesh(a,b,c):
  '''
  a = float(input("Enter coeff of a: "))
  b = float(input("Enter coeff of b: "))
  c = float(input("Enter coeff of c: "))
  '''
  global printCollection
  printCollection=[]
  
  if a == 0:
      printCollection.append("Linear Equation")
      if b == 0:
          if c == 0:
              printCollection.append("Infinetely Many Sol")
          else:
              printCollection.append("No Sol")
      else:
          root = (-c/b)
          printCollection.append(f"X = {root}")
  else:
      printCollection.append("Quadratic Equation.")
      discriminant = (b*b-4*a*c)
      if discriminant > 0:
          printCollection.append("Equation has Two Real and distinct Roots.")
          root1 = ((-b) + math.sqrt(discriminant))/2*a
          root2 = ((-b) -  math.sqrt(discriminant))/2*a
          printCollection.append(f"X1 = {root1} and X2 = {root2}")
      elif discriminant == 0:
          printCollection.append("Equation has Two Real and Same Roots")
          root = (-b)/2*a
          printCollection.append(f"X1 = X2 = {root}")
      else:
          printCollection.append("Equation has Imaginary Roots.")
          realpart = (-b)/2*a
          imaginarypart = math.sqrt(-discriminant)/2*a
          printCollection.append(f"X1 = {realpart} + {imaginarypart}i and X2 = {realpart} - {imaginarypart}i")
'''----Main Code ends Here----'''


'''
  -------------------------------
---Flask-App's Coding Starts Here---
  -------------------------------
'''
from flask import Flask, request
from datetime import datetime
import matplotlib.pyplot as pl
import numpy as np
import subprocess

subprocess.run("mkdir static", shell=True, capture_output=True)

app = Flask(__name__)
#Function to be called when user visit home page 
@app.route('/')
def home():
  return '''
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta http-equiv="X-UA-Compatible" content="ie=edge">
  <title>Tirupati</title>
  <style type="text/css">
   *{
      padding:0;
      margin:0;
      text-align: center;
    }
   body{
      margin:5px;
      background: linear-gradient(to bottom right, #efccaa,#bbb, #efccaa);
      border: 4px outset;
      padding-bottom:200px;
   }
   input{
     margin:10px;
     width:70px;
     height:25px;
   }
   button{
     color:white;
     border-radius:10px;
     padding:10px;
     background:#efccaa;
     margin-top: 30px;
   }
   h2{
     border: solid;
     padding: 5px;
   }
   div.t{
     margin-top: 10px;
   }
   div.interface{
     padding: 30px;
   }
   form{
     padding:10px;
     border:solid;
     box-shadow: 2px 2px 5px white;
   }
  </style>
</head>
<body>

  <h2>Root Calculator for Quadratic Equations</h2>
  <br>
  <div class="stdform">
    <b>Standard form</b>:<br>
    ax<sup>2</sup> + bx + c
  </div>
  <div class="interface">
  <form action="/calculate" method="POST">
  Enter the value of coefficient a:
  <input required pattern="^[0-9]+|[0-9]*\\.[0-9]+|-([0-9]+|[0-9]*\\.[0-9]+)$" name="a"><br>
  Enter the value of coefficient b:
  <input required pattern="^[0-9]+|[0-9]*\\.[0-9]+|-([0-9]+|[0-9]*\\.[0-9]+)$" name="b"><br>
  Enter the value of coefficient c:
  <input required pattern="^[0-9]+|[0-9]*\\.[0-9]+|-([0-9]+|[0-9]*\\.[0-9]+)$" name="c"><br>
  <button type="submit" onclick="validate();">Calculate</button>
  </form>
  </div>
  <div class="t"></div>

<script type="text/javascript">
function validate(){
let input=document.querySelectorAll("form>input");
for(i=0; i<input.length; i++){
  if(input[i].validity.patternMismatch) input[i].setCustomValidity("Please! Enter a valid Number");
  else input[i].setCustomValidity("");}
}
//Watermark function Start here
function $tfun(){
//make a div tag having class name 't'
let $tele,$t,$div;
$div=document.querySelector("div.t");
$div.style.fontFamily="Monospace";
$div.style.color="white";
$div.style.fontSize="50px";
$div.style.textAlign="center";
$t="RAJNEESH".split('');
$tele=document.createElement('span');
$tele.innerHTML=$t[$tcount];
$div.appendChild($tele);
$tcount++;
if($tcount==$t.length){
$tcount=50;
setTimeout($tshrink,1200);
return;}
setTimeout($tfun,250);
function $tshrink(){
  $div.style.textAlign="left";
  $div.style.color="#aaa";
  $div.style.fontSize=$tcount+'px';
  $tcount--;
  if($tcount==14){
   return;}
  setTimeout($tshrink,20);}}
let $tcount=0;
$tfun();
//$tfun();Closed
</script>
</body>
</htmt>
'''

#Function to be called when user click calculate button
@app.route('/calculate', methods=['GET','POST'])
def calc():
  a=float(request.form.get('a'))
  b=float(request.form.get('b'))
  c=float(request.form.get('c'))
  rajneesh(a,b,c)
  
  #Graph plotting starts here
  x=np.linspace(-20,20,400)
  y=a*x**2+b*x+c
  pl.plot(x,y,color="green")
  pl.xlabel("X-Axis-->")
  pl.ylabel("Y-Axis-->")
  graphTitle="("+str(a)+")x² + ("+str(b)+")x + ("+str(c)+")"
  pl.title(graphTitle)
  pl.grid(True)
  #pl.legend()
  graphName="./static/"+datetime.now().strftime("%d-%m-%Y_%I-%M-%S_%p")+".png"
  pl.savefig(graphName)
  pl.close()
  #Graph plotting Ends here

  result=""
  div="<div style='border:solid;margin:15px;padding:10px'>>>> "
  for i in printCollection:
    result=result+div+i+"</div>"

  return '''
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta http-equiv="X-UA-Compatible" content="ie=edge">
  <title>Result</title>
  <style>
    section{
      background:gray;
      color:white;
      padding:2px;
    }
    [type="button"]{
      color:white;
      border-radius:10px;
      padding:10px;
      background:salmon;
      display:block;
      margin:0 auto;
    }
  </style>
</head>
<body>
  <section >'''+result+'''</section>
  <img src="'''+graphName+'''" width="100%" alt="Image Not Found">
  <br><br><br>
  <input type="button" value="Go Back" onclick="history.back();" ">
</body>
</html>
'''

subprocess.run("am start -a android.intent.action.VIEW -d http://127.0.0.1:9000/", shell=True, capture_output=True)
#To Run the flask app
if __name__ == '__main__':
  app.run(debug=True, host='0.0.0.0', port=9000)