import random
f=open('new.json','w')
f.write('[\n')
def con2json(name):
    data={}
    for i in name:
      data['id']=random.randint(1,100)
      data['Name']=i
      f.write("\t"+str(data)+"\n")
    f.write("]")
    f.close()

a=["aman","rajan","ram","sunny"]
con2json(a)
f=open("new.json",'r')
print(f.read(),"\nThe JSON file saved as 'new.json'")
f.close()
