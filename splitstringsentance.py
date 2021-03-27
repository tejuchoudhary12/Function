def line():

    a=[]
    i=" "
    for c in sentance:
        if c==" ":
            a.append(i)
            i=""
        else:
            i+=c
    if i:
        a.append(i)
    return(a)

sentance="NvGurukul is an Alternative to higher education reducing the barries of current formal education system"
print(line())