def addQuestions(question_list):
    return question_list

def addOptions(options):
    return options

def correctAnswer(answer):
    return answer

def lifeline1(choices):
    return choices
    

question_list=[
    "How many continents are there?",
    "What is the capital of India?", 
    "NG mei kaun se course padhaya jaata hai?"
    ]
questions = addQuestions(question_list)

options_list = [
    ["1)Four", "2)Nine", "3)Seven", "4)Eight"],
    ["1)Chandigarh", "2)Bhopal", "3)Chennai", "4)Delhi"],
    ["1)Software Engineering", "2)Counseling", "3)Tourism", "4)Agriculture"]]
options = addOptions(options_list)

answer=[3,4,1]
correct = correctAnswer(answer)

choices=["2)Nine","3)Seven","1)Chandighar", "4)Delhi","1)Software Engineering", "2)Counseling"]
choice = lifeline1(choices)

i = 0
r = 1
y = 0
count=0
while(i < len(questions)):
    print(i+1, questions[i])
    j = 0
    while(j < len(options[i])):
        print(options[i][j])
        j = j + 1
    lifeline=input("do you want lifeline, yes or no")
    if lifeline=="yes":
        if count==0:
            print(choices[y+i])
            print(choices[y+r])
            n=int(input("Enter your anwser now "))
            if n==answer[i]:
                print("Sahi Jawab")
            else:
                print("aap ye game har chuke ho")
                break
            count+=1
        else:
            print("You have used your 50-50 lifeline before")
            m=int(input("Enter your answer"))
            if m==answer[i]:
                print("App jeet gaye ho") 
            else:
                print("sorry! Galat Jawab") 
                break
    elif lifeline=="no":   
        choice = int(input("Sahi Jawab chuneyee...."))
        if choice==correct[i]:
            print("sahi jawab")
            print("bade te hai agli prashn ki aor....")
        else:
            print("shema chahate hai.. aap har chuke ho")  
            break 
    r+=1
    y+=1         

    i = i + 1







    



