def num(limit):
    i=0
    sum=0
    while i<=number:
        if i*3==0:
            sum+=1
            return(sum)
        if i*5==0:
            sum+=1
            return(sum)

        
        i+=1
number=int(input("Enter no."))
print(num(number))    