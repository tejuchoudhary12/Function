def show_number(limit):
    i=1
    while i<=10:
        if i%2==0:
            print(i,"even")
        else:
            print(i,"odd")
        i+=1
number=int(input("enter a number: "))
show_number(number)