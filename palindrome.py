    #reverse of a string or number


a="hello world"
rev=""
for i in a:
    rev=i+rev
print(rev)
    
#reverse of a splitted string

a="hello world"
rev=""
arr=a.split()
for i in arr:
    arr1=" "
    for j in i:
        arr1=j+arr1

    rev+=arr1
print(rev)
    

