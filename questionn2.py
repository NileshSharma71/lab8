print("Enter -1 to stop!")
k=[]
j=[]
while True:
    
    n=int(input("Enter: "))
    
    if n==-1:
        break
    k.append(n)
print(k)
x=len(k)
for i in range(x):
    o=min(k)
    k.remove(o)
    j.append(o)
print(j)