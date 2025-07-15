a=[2,6,4,12,32,1,78,456,345,23,]
print(a)
temp=0
b=len(a)
for i in range(b):
    for j in range(i+1,b):
        if a[i]>a[j]:
            temp=a[i]
            a[i]=a[j]
            a[j]=temp
print(a)
