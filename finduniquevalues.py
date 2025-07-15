list1=[1,2,3,4,5,6,7,8]
list2=[2,3,6,7,8,9,10]
print(list1)
print(list2)
list3=list1+list2
join=[]

for i in list3:
    if i not in join:
        join.append(i)
print(set(join))