m=int(input("Enter: "))
n=int(input("Enter: "))
a=[]
c=0
while True:
    c+=1
    a.append((input("enter the value: ")).split())
    if c==m:
        break
    
print("First matrix: ",a)
b=[]
c1=0
while True:
    c1+=1
    b.append((input("enter the value: ")).split())
    if c1==m:
        break
print("second matrix: ",b)
for i in a:
    for j in b:
        pass