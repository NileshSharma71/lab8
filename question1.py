print("Enter -1 to stop!")
k=[]
t1=0
t2=1
while True:
    n=int(input("Enter: "))
    if n==-1:
        break
    k.append(n)
#1st one
for i in k:
    t1+=i
print("The sum is: ",t1)
#2nd one
for i in k:
    t2*=(i)
print("the product is : ",t2)
#3rd one
print("Largest element is: ",max(k))