def perfect_numbers(num):
    b=number
    a=1
    sum=0
    while a<num:
        if num%a==0:
            sum+=a
        a+=1
    if sum==b:
        return (b, "is perfect number")
    else:
        return(b, "it is not a perfect number")
number=int(input("enter no."))
print(perfect_numbers(number))