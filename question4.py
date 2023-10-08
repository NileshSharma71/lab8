m=int(input("Enter: "))
n=int(input("Enter: "))
a=[]
for i in range(n):
    for j in range(m):
        n=int(input("Enter the value: "))
        a.append(n)
for i in a:
    if m==n:
        b=[a[m*(i)]]
