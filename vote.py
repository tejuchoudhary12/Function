def eligible_for_vote():
    if age>=18:
        return ("You are eligible")
    else:
        return("Not eligible")
age=int(input("enter your age"))
print(eligible_for_vote())