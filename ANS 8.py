""" print("Enter the size of list:")
n=int(input()) """
l1=["A","A","B","C","C"]
a=0;b=0;c=0
for i in range(5):
    if l1[i]=="A":
        a+=1
    if l1[i]=="B":
        b+=1
    if l1[i] =="C":
        c+=1
print("A:{},B:{},C:{}".format(a,b,c))           
