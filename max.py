# def maximum():
#     index=0
#     max=num[0]
#     while index<len(num):
#         m=num[index]
#         if m>max:
#             max=m
#         index+=1
#     print("max no. is:", max)

# num=[10, 20, 30, 40, 50, 60, 70]
# maximum()

 
def isEven(number  = 12):
    if(number % 2 == 0):
        return True
    else:
        return False

print(isEven(10))