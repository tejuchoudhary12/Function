def Split(element): 
    i=0
    even = [] 
    odd = [] 
    while i <len(element): 
        if (i % 2 == 0): 
            even.append(element[i]) 
        else: 
            odd.append(element[i])
        i+=1
    print("Even lists:", even) 
    print("Odd lists:", odd) 
  
element = [23, 14, 56, 12, 19, 9, 15, 25, 31, 42, 43]
Split(element)         
