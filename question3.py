print("Enter -1 to stop!")
l1=[]
j=[]
while True:
    
    n=int(input("Enter: "))
    
    if n==-1:
        break
    l1.append(n)
print("Original List:", l1)
for i in range(0, len(l1)):
	for j in range(i+1, len(l1)):
		if l1[i] >= l1[j]:
			l1[i], l1[j] = l1[j],l1[i]
print("Sorted List", l1)
