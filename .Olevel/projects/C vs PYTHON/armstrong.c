#include<stdio.h>
#include<conio.h>
#include<math.h>
int checkArm(int x){
int backup=x;
//COUNTING THE DIGIT
int length=0;
while(x>0){
length++;
x=x/10;
}

x=backup;
int sum=0;
while(x>0){
int d=x%10;
sum=sum+pow(d,length);
x=x/10;
}

if (backup==sum) return 1;
return 0;
}

int main(){
printf("--WELCOME TO ARMSTRONG NUMBER PRINTING INTERFACE--@tirupati\n");
printf("\t\t--C language--\n");
int user;
printf("How many Armstrong number do you want to print: ");
scanf("%d", &user);
int printCount=0,num=10;
while(1){
if (checkArm(num)){
printCount++;
printf("%d=> %d\n",printCount,num);
}
if (user==printCount) break;
num++;
}


printf("\n             ------THANK_YOU-----");
getch();
}