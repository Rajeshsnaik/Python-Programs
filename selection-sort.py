# selection sort using min method(ascending order)
list1=[20,23,44,5,1,22,3]

for i in range(len(list1)-1):
    min_val=min(list1[i:])
    min_index=list1.index(min_val)
    list1[i],list1[min_index]=list1[min_index],list1[i]
print(list1)


# selection sort using max method(descending order)
'''list1=[20,23,44,5,1,22,3]

for i in range(len(list1)-1):
    min_val=max(list1[i:])
    min_index=list1.index(min_val)
    list1[i],list1[min_index]=list1[min_index],list1[i]
print(list1)'''

# in the proper manner
'''list1=[20,23,44,5,1,22,3]

for i in range(len(list1)-1):
    min_val=min(list1[i:])
    min_index=list1.index(min_val)
    if list1[i] != list1[min_index]:
        list1[i],list1[min_index]=list1[min_index],list1[i]
    print(list1)'''


# sorting without using built-in functions

num = int(input("enter the numbers you want to enter : "))
list1=[int(input("enter number : ")) for x in range(num)] #list compriation method
print("list is",list1)

for i in range(len(list1)-1):
    m_val=list1[i]
    for j in range(i+1,len(list1)):
        if list1[j] < m_val: #if we want to find in the descending value then change the sign.
            m_val=list1[j]
    
    m_ind = list1.index(m_val,i)
    if list1[i] != list1[m_ind]:
        list1[i],list1[m_ind]=list1[m_ind],list1[i]
print(list1)
