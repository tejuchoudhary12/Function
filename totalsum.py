def total_sum():
    
    number=30
    i=0
    a=[]
    while i <len(n):
        j=0
        while n[i]>n[j]:
            if n[i]+n[j] == 30 :
                a.append([n[j],n[i]])
            j=j+1
        i+=1
    return (a)

n = [10, 11, 12, 13, 14, 17, 18, 19]

print(total_sum())