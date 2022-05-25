import random


def instructions():
    print("the aim of the game is to guess what the maori number is in english")
    print("their is an easy mode and a hard mode")
    print("the easy mode is numbers 1 through 9")
    print("the hard mode is numbers 1 through 99")
    print("when the  game ends you while be told how many you got right ")
    print("and how many you got wrong")
    print("and what ones you got wrong")


def yes_no(question_text):
    while True:
        print(question_text)
        guess_ = input(">>").lower()
        # if they say output program continues
        if guess_ == "yes" or guess_ == "y" or guess_ == "":
            return "Yes"

        # if they say no output display instructions
        elif guess_ == "no" or guess_ == "n":
            return "No"

        # otherwise, show error
        else:
            print('please answer "yes" or "no"')
        print(f"you entered {guess_}")


def easy_hard(question_text):
    while True:
        print(question_text)
        answer_ = input(">>").lower()
        # if they say easy out put that
        if answer_ == "easy" or answer_ == "e":
            answer_ = "Easy"
            return answer_

        # if they say hard output that
        elif answer_ == "hard" or answer_ == "h":
            answer_ = "Hard"
            return answer_

        # otherwise, show error
        else:
            print('please answer "easy" or "hard"')
        print(f"you entered {answer_}")


# main routine
rounds = 0
mistakes = 0
words = []
instruction = yes_no("have you played before? :")  # finding if they have played
if instruction == "No":
    instructions()  # prints instructions
difficulty = easy_hard("do you want to play easy or hard mode :")  # finding out what difficulty
while True:
    Numbers = ["Tahi", "rua", "toru", "whā", "rima", "ono", "whitu", "waru", "iwa"]

    if difficulty == "Easy":
        answer: int = random.randint(1, 9)
    else:
        answer: int = random.randint(1, 99)
    if answer < 10:
        question = Numbers[answer - 1]  # 1-9
    elif answer == 10:  # 10
        question = "Tekau"
    elif answer < 20:  # 11-19
        question = "tekau mā " + Numbers[answer % 10 - 1]
    elif answer % 10 == 0:  # ends in 0
        question = Numbers[answer // 10 - 1] + " tekau"
    else:  # everything else
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
    stop = yes_no("do you want to continue?")
    if stop == "No":
        break
print(F"you got {rounds - mistakes} questions right")
print(F"you got {mistakes} questions wrong")
print(F"your score is {rounds - mistakes} out of {rounds} or {((rounds - mistakes) / rounds) * 100}%")
print(F"you need to work on {words}")
