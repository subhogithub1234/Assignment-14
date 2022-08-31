n=int(input("Enter the size of list"))
l1=[]
print("insert the number:")
for i in range(n):
     x=int(input())
     l1.append(x)
print(l1) 
for i in range(n):
    if l1[i]==1:
        print(i)

