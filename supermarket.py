customer=[]
items=[]
while True:
     a= input("Is there is any customer available y/n:   ")
     name=input("Enter the Name: ")
     if a=='y':
       while True:
        items=input("Enter the items purchased: ")
        if items=='stop':
           break
     print(name,items)
        