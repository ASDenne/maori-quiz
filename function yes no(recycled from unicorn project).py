'''this is a previouse piece of code i will be using for the instruction checker and difficulty checher'''

#functions
def yes_no(question_text):
    while True:
        Answer = input(question_text).lower()
        # if they say output program countiues
        if Answer == "yes" or Answer == "y":
            Answer = "Yes"
            return Answer
    
        #if they say no output desplay instructions
        elif Answer == "no" or Answer == "n":
            Answer = "No"
            return Answer
    
        #otherwie show error
        else:
            print('please answer "yes" or "no"')
        print(f"you entered {Answer}")


#mainroutine
show_instructions = yes_no("have you played before? :")
print(f"you entered {show_instructions}")
fun = yes_no("Are you having Fun")
print(f"you entered {fun}")
