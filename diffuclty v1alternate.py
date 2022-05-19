def yes_no(question_text):
    while True:
        Answer = input(question_text).lower()
        # if they say output program countiues
        if Answer == "yes" or Answer == "y":
            return "Yes"




        #if they say no output desplay instructions
        elif Answer == "no" or Answer == "n":
            return "No"



        #otherwise show error
        else:
            print('please answer "yes" or "no"')
        print(f"you entered {Answer}")


#mainroutine
easy_mode = yes_no("do you want to play the easy mode? :")
print(easy_mode)
