def difference():
    i=0
    new_list=[]
    while i<len(list1):
        if list1[i]  not in list2:
            new_list.append(list1[i])
        i+=1
    return new_list
        

list1 = [1,2,3,4,5,6]
list2 = [2,3,1,0,6,7] 

print(difference())


