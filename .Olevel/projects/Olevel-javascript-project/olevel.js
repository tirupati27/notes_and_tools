/*---------------------------------------TIRUPATI_01------------------*/
function fun1(){
var a, b, c, d, e, f, g, h;
a=document.getElementById("anum1").value;
b=document.getElementById("anum2").value;
c=parseFloat(a)+parseFloat(b);
document.getElementById("anum3").value=c;
d=parseFloat(a)-parseFloat(b);
document.getElementById("anum4").value=d;
e=parseFloat(a)*parseFloat(b);
document.getElementById("anum5").value=e;
f=parseFloat(a)/parseFloat(b);
document.getElementById("anum6").value=f;
g=parseFloat(a)%parseFloat(b);
document.getElementById("anum7").value=g;
h=parseFloat(a)**parseFloat(b);
document.getElementById("anum8").value=h;
}

/*---------------------------------------TIRUPATI_02------------------*/
function fun2(){
var a, b, c, d, e;
a=document.getElementById("bnum1").value;
b=document.getElementById("bnum2").value;
c=3.144*parseFloat(a)*parseFloat(a);
document.getElementById("bnum3").value=c;
d=parseFloat(a)**2;
document.getElementById("bnum4").value=d;
e=a*b;
document.getElementById("bnum5").value=e;
}

/*---------------------------------------TIRUPATI_03------------------*/
function fun3(){
var a, b, c, d, e;
a=document.getElementById("cnum1").value;
b=document.getElementById("cnum2").value;
c=document.getElementById("cnum3").value;
d=(parseFloat(a)*parseFloat(b)*parseFloat(c))/100;
document.getElementById("cnum4").value="₹ "+d.toFixed(2);
e=parseFloat(a)+parseFloat(d);
document.getElementById("cnum5").value="₹ "+e.toFixed(2);
}

/*---------------------------------------TIRUPATI_04------------------*/
function fun4(){
var x, y, z;
x=document.getElementById("dnum1").value;
y=document.getElementById("dnum2").value;
z=document.getElementById("dnum3").value;
if(x==0){x=0;}
if(y==0){y=0;}
if(z==0){z=0;}
x=parseFloat(x);
y=parseFloat(y);
z=parseFloat(z);

if(x>y)
{
    if(x>z)
     {
       dnum4.value="x is Greater.";
     }
    if(x<z)
     {
       dnum4.value="z is Greater.";
     }
    if(x==z)
     {
       dnum4.value="x & z are Equally Greater.";
     }
}
if(y>x)
{
    if(y>z)
     {
       dnum4.value="y is Greater.";
     }
    if(y<z)
     {
       dnum4.value="z is Greater.";
     }
    if(y==z)
     {
       dnum4.value="y & z are Equally Greater.";
     }
}
if(x==y)
{
    if(x>z)
     {
       dnum4.value="x & y are Equally Greater.";
     }
    if(x<z)
     {
       dnum4.value="z is Greater.";
     }
    if(x==z)
     {
       dnum4.value="ALL are Equal.";
     }
}
}

/*---------------------------------------TIRUPATI_05------------------*/
function fun5(){
var leapy;
leapy=parseInt(document.getElementById("enum1").value);
if((leapy%4==0 && leapy%100!=0)||(leapy%400==0))
{
   enum2.value="It's a Leap Year.";
}
else
{
   enum2.value="It's NOT a Leap Year.";
}
}

/*---------------------------------------TIRUPATI_06------------------*/
function fun6(){
var a, b;
a=parseFloat(document.getElementById("fnum1").value);
b=parseFloat(document.getElementById("fnum2").value);
a=a+b;
b=a-b;
a=a-b;
fnum3.value=a;
fnum4.value=b;
}

/*---------------------------------------TIRUPATI_07------------------*/
function fun7(){
var n;
n=parseInt(document.getElementById("gnum1").value);
    if(n>0)
   {
    gnum2.value="Positive";
    }
    if(n<0)
   {
    gnum2.value="Negetive";
    }
    if(n==0)
   {
    gnum2.value="Zero";
    }
   
    if(n%7==0 && n%10==7)
    {
       gnum3.value="Yes";
    }
    else
    {
       gnum3.value="No";
    }

    if(n%2==0)
    {
       gnum4.value="Even";
    }
    else
    {
       gnum4.value="Odd";
    }
}

/*---------------------------------------TIRUPATI_08------------------*/
function fun8(){
var x, y, z;
x=document.getElementById("hnum1").value;
y=document.getElementById("hnum2").value;
z=document.getElementById("hnum3").value;
if(x==0){x=0;}
if(y==0){y=0;}
if(z==0){z=0;}
x=parseFloat(x);
y=parseFloat(y);
z=parseFloat(z);
if((x+y+z)==180)
{
    hnum4.value="Yes, It Makes a valid Triangle";
}
else
{
    hnum4.value="No, It doesn't Make a Triangle";
}
}

/*---------------------------------------TIRUPATI_09------------------*/
function fun9(){
let x=document.getElementById("inum1").value;
if(x>='0' && x<='9')
{
    inum2.value="It's a Digit";
}
else if(x>='A' && x<='Z')
{
    inum2.value="It's a Uppercase Alphabet";
}
else if(x>='a' && x<='z')
{
    inum2.value="It's a Lowercase Alphabet";
}
else
{
    inum2.value="It's a Special Character";
}
}
/*---------------------------------------TIRUPATI_10------------------*/
function fun10(){
var a, b, c, d, e, f;
a=parseFloat(document.getElementById("jnum1").value);
b=parseFloat(document.getElementById("jnum2").value);
c=parseFloat(document.getElementById("jnum3").value);
d=parseFloat(document.getElementById("jnum4").value);
e=a*(1+b/(d*100))**(d*c);
f=(((1+b/(d*100))**d)-1)*100;
document.getElementById("jnum5").value="₹ "+e.toFixed(2);
document.getElementById("jnum6").value=f.toFixed(2)+" %";
}
/*---------------------------------------TIRUPATI_11------------------*/
function fun11(){
var a, b;
a=parseFloat(document.getElementById("knum1").value);
b=document.getElementById("knum2");
if (a==2||a==3||a==5||a==7){
b.value=a+" is a Prime Number";
}
else if (a<=1||a%2==0){
b.value=a+" is NOT a Prime Number";
}
else{
for (let i=3; i<=Math.sqrt(a); i=i+2){
if(a%i==0){b.value=a+" is NOT a Prime Number"; break;}
else{b.value=a+" is a Prime Number";}
}
}
}
/*---------------------------------------TIRUPATI_12------------------*/
function fun12(){
var n, i, fact=1;
n=parseFloat(document.getElementById("lnum1").value);
for(i=1; i<=n; i++){fact=fact*i;}
document.getElementById("lnum2").value=fact;
}
/*---------------------------------------TIRUPATI_13-THEME----------------*/
let allcol, buttonall, headall, boxall, gradientvalue, lgradient, rgradient, gradInput;
gradInput=document.getElementById("selectgrad");
allcol=document.querySelectorAll(".themecol");
buttonall=document.getElementsByTagName("button");
headall=document.getElementsByTagName("h2");
boxall=document.getElementsByTagName("div");

function defaultTheme(){
allcol[0].value="#ffffff";
allcol[1].value="#ffffff";
allcol[2].value="#ffffff";
allcol[3].value="#ffff00";
allcol[4].value="#000000";
allcol[5].value="#ffffff";
dynamictheme();
}
function themeDataInput(){
let n=(Math.random()*10).toFixed(0);
console.log(n+"th set of value stored");
if(n==0){
allcol[0].value="#c6d6e6";
allcol[1].value="#c6d6e6";
allcol[2].value="#0000ff";
allcol[3].value="#ffffff";
allcol[4].value="#000000";
allcol[5].value="#ffff00";
}
else if(n==1){
allcol[0].value="#00ffff";
allcol[1].value="#85e77e";
allcol[2].value="#dffb09";
allcol[3].value="#a59ff4";
allcol[4].value="#000000";
allcol[5].value="#e2e255";
}
else if(n==2){
allcol[0].value="#e2e255";
allcol[1].value="#f09b24";
allcol[2].value="#ffffff";
allcol[3].value="#ffffff";
allcol[4].value="#000000";
allcol[5].value="#f5a8c3";
}
else if(n==3){
allcol[0].value="#ffffff";
allcol[1].value="#ffff00";
allcol[2].value="#ffffff";
allcol[3].value="#fb0450";
allcol[4].value="#ffffff";
allcol[5].value="#38ffb3";
}
else if(n==4){
allcol[0].value="#f457ff";
allcol[1].value="#ffdd57";
allcol[2].value="#0fc6eb";
allcol[3].value="#015a3c";
allcol[4].value="#ffffff";
allcol[5].value="#96ff64";
}
else if(n==5){
allcol[0].value="#ffffff";
allcol[1].value="#ffffff";
allcol[2].value="#ffffff";
allcol[3].value="#0000ff";
allcol[4].value="#ffffff";
allcol[5].value="#e2b555";
}
else if(n==6){
allcol[0].value="#ffffff";
allcol[1].value="#ffffff";
allcol[2].value="#ffff00";
allcol[3].value="#ff0000";
allcol[4].value="#ffffff";
allcol[5].value="#908514";
}
else{
allcol[0].value="#ffffff";
allcol[1].value="#ff00ff";
allcol[2].value="#ffffff";
allcol[3].value="#ffffff";
allcol[4].value="#000000";
allcol[5].value="#999999";
}
if((Math.random()*10).toFixed(0)<5){gradInput.value="linear-gradient";}
else{gradInput.value="radial-gradient";}
console.log(gradInput.value);
dynamictheme();
}
themeDataInput();
/*-----------------EventListener start----------------*/
for(let i=0; i<allcol.length; i++){
allcol[i].addEventListener("input", dynamictheme);
}
gradInput.addEventListener("change", dynamictheme);
for(let i=0; i<buttonall.length; i++){buttonall[i].addEventListener("mouseout", dynamictheme);}
for(let i=0; i<buttonall.length; i++){
buttonall[i].addEventListener("mouseover", ()=>buttonhover(i));}
/*-----------------EventListener End----------------*/
function buttonhover(i){
buttonall[i].style.background="linear-gradient(to bottom right, red, #ff7070, red)";
buttonall[i].style.color="white";
buttonall[i].style.border="2px solid white";
}
function dynamictheme(){
/*----GradientStart----*/
lgradient=gradInput.value +"(to bottom right, " + allcol[0].value + ", " + allcol[1].value + ", " + allcol[2].value + 

")";
rgradient=gradInput.value + "(" + allcol[0].value + ", " + allcol[1].value + ", " + allcol[2].value + 

")";
gradInput.value=="linear-gradient"?gradientvalue=lgradient: gradientvalue=rgradient;
for(let i=0; i<boxall.length; i++){
boxall[i].style.background=gradientvalue;
boxall[i].style.border="2px solid";
boxall[i].style.borderColor=allcol[3].value;
}
/*----GradientEnd----*/
for(let i=0; i<headall.length; i++){
headall[i].style.background=allcol[3].value;
headall[i].style.color=allcol[4].value;
}
for(let i=0; i<buttonall.length; i++){
buttonall[i].style.background=allcol[3].value;
buttonall[i].style.color=allcol[4].value;
buttonall[i].style.border="1px solid black";
}
document.body.style.background=allcol[5].value;
}
/*---------------------------------------The_End--------------------------------------*/

