# def array():
user_array=int(input("enter only 2, 3 or 0 : "))
user_element =int(input("enter no within 10 : "))
i=0
j=[]
while i < user_array :
    sublist=[]
    a=0
    while a< user_element:
        sublist.append(a+1)
        a+=1
    j.append(sublist)
    i+=1
print(j)