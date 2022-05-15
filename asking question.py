import random
diffuclty = input(">>")
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
    guess = input(">>")
    

