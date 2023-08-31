# bubble-sort using python.

list1=[]
num=int(input("enter the numbers to be added :"))
for k in range(num):
    list1.append(int(input()))

for j in range(len(list1)-1):
    for i in range(len(list1)-1-j):
        if list1[i]>list1[i+1]:
            list1[i],list1[i+1]=list1[i+1],list1[i]

print("sorted list is :",list1)

# Output :
# enter the numbers to be added :5
# -1
# 4
# 88
# 0
# 333
# sorted list is : [-1, 0, 4, 88, 333]