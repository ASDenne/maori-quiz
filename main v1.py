import random


def instructions():
    print("the aim of the game is to guess what the maori number is in english")
    print("thier is an easy mode and a hard mode")
    print("the easy mode is numbers 1 through 9")
    print("the hard mode is numbers 1 through 99")
    print("when the  game ends you while be told how many you got right ")
    print("and how many you got wrong")
    print("and what ones you got wrong")


def yes_no(question_text):
    while True:
        print(question_text)
        Answer = input(">>").lower()
        # if they say output program countiues
        if Answer == "yes" or Answer == "y" or Answer == "":
            return "Yes"

        #if they say no output desplay instructions
        elif Answer == "no" or Answer == "n":
            return "No"



        #otherwise show error
        else:
            print('please answer "yes" or "no"')
        print(f"you entered {Answer}")


def easy_hard(question_text):
    while True:
        print(question_text)
        Answer = input(">>").lower()
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
rounds = 0
mistakes = 0
words= []
instruction = yes_no("have you played before? :")
if instruction == "No":
    instructions()
diffuclty = easy_hard("do you want to play easy or hard mode :")
while True:
    Numbers = ["Tahi", "rua", "toru", "whā", "rima", "ono", "whitu", "waru", "iwa"]

    if diffuclty == "Easy":
        answer: int = random.randint(1, 9)
    else:
        answer: int = random.randint(1, 99)
    if answer < 10:
        question = Numbers[answer - 1]
    elif answer == 10:
        question = "Tekau"
    elif answer < 20:
        question = "tekau mā " + Numbers[answer % 10 - 1]
    elif answer % 10 == 0:
        question = Numbers[answer // 10 - 1] + " tekau"
    else:
        question = Numbers[answer // 10 - 1] + " tekau mā " + Numbers[answer % 10 - 1]
    print(f"what is {question} In english")
    while True:
        try:
            Guess = int(input(">>"))
            break
        except ValueError:
            print("please enter guess in number format")
    if answer == Guess:
        print("congrats you guessed correctly")
    else:
        print("oh sorry you got it wrong")
        mistakes = mistakes + 1
        words.append(question)
    rounds = rounds + 1
    stop = yes_no("do you want to countinue?")
    if stop == "No":
        break
print(F"you got {rounds-mistakes} questions right")
print(F"you got {mistakes} questions wrong")
print(F"your score is {rounds - mistakes} out of {rounds} or {((rounds-mistakes)/rounds)*100}%")
print(F"you need to work on {words}")
