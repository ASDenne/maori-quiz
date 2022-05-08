def instructions():
    print("this will later be filled with in")
def yes_no(question_text):
    while True:
        Answer = input(question_text).lower()
        # if they say output program countiues
        if Answer == "yes" or Answer == "y":
            Answer = "Yes"

            break


        #if they say no output desplay instructions
        elif Answer == "no" or Answer == "n":
            Answer = "No"
            break


        #otherwise show error
        else:
            print('please answer "yes" or "no"')
        print(f"you entered {Answer}")


#mainroutine
instructions = yes_no("have you played before? :")
if instructions == "No":
    instructions()
print("next step")
