# def f1():
#    s = "I Love Navgurukul"
#    def f2():
#        print(s)
#    f2()
# f1() 

# def first_function():
#     s = 'I love India'
#     def second_function():
#         print(s)     
#     second_function()
# first_function() 

def first_function():
    s = 'I love India'
    def second_function():
        s = "MY NAME IS JACK"
        print(s)     
    second_function()
    print(s)    

first_function()