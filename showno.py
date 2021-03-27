def showNumbers(list):
    i=1
    while i<=number:
        if i%2==0:
            print(i, "even no.")
        else:
            print(i, "odd no.")
        i+=1
number=int(input("enter no"))
showNumbers(number)