
#functions
def easy_hard(question_text):
    while True:
        Answer = input(question_text).lower()
        # if they say easy out put that
        if Answer == "easy" or Answer == "e":
            Answer = "Easy"
            return Answer

        #if they say hard output that
        elif Answer == "hard" or Answer == "h":
            Answer = "Hard"
            return Answer

        #otherwie show error
        else:
            print('please answer "easy" or "hard"')
        print(f"you entered {Answer}")


#mainroutine
diffuclty = easy_hard("do you want to play easy or hard mode :")
print(diffuclty)
print("countiunes")
