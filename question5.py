# n=input("Enter: ").split()
# ss=input("Enter the sample string: ")
# c=0
# #1st one
# for i in n:
#     if ss==i:
#         c+=1
# print("No. of strings that contain the sample string: ",c)
#2nd one
# kk=[]
# j=[]
# while True:
#     k=int(input("Enter the value: "))
    
#     if k==0:
#         break
#     kk.append(k)
# for i in (kk):
#     if i>=0:
#         i=i**2
#         j.append(i)
#     elif i<0:
#         j.append(0)
# print(j)
#3rd one
# kj=[]
# jj=[]
# while True:
#     k=int(input("Enter the value: "))
    
#     if k==0:
#         break
#     kj.append(k)
# for i in kj:
#     if i<=20 and i>=10:
#         i=i**2
#         jj.append(i)
#     else:
#         jj.append(i)
# print("resultant list: ",jj)
#4th one
ni=input("Enter: ").split()
jk=[]
for i in ni:
    if (i.islower()) or (i.istitle==False):
        jk.append(i)
        continue
    k=i.upper()
    jk.append(k)
print(" ".join(jk))
    