
def binarySearch(list1,key):
    low=0
    high=len(list1)-1
    found = False
    while low<=high and not found:
        mid = (low + high) // 2
        if key == list1[mid]:
            found = True
        elif key > list1[mid]:
            low = mid+1
        else:
            high=mid-1
    if found == True:
        print("key found")
    else:
        print("not found")

list1=[]
num=int(input("enter the number of elements to be added :"))
print("enter the input :")
for k in range(num):
    list1.append(int(input()))

list1.sort()
print(list1)
key = int(input("enter the key to be found : "))
binarySearch(list1,key)

# Output :
# enter the number of elements to be added :4
# enter the input :
# 1
# 2
# 5
# 2
# [1, 2, 2, 5]
# enter the key to be found : 1
# key found