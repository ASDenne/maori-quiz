import random
def generate_Question(diffuclty):
    numbers = ["Tahi","rua","toru","whā","rima","ono","whitu","waru","iwa"]
    if diffuclty == "Easy":
        Answer = random.randint(1,9)
        question = numbers[Answer]



    else:
        Answer = random.randint(1,99)
        if len(str(Answer)) == 1:
            question = numbers[Answer-1]
        elif Answer == 10:
            question = "Tekau"
        elif Answer % 10 == 0:
            question = numbers[Answer//10-1] + " tekau"
        else:
            question = numbers[Answer//10-1] + " tekau mā " + numbers[Answer % 10-1]
    return question




#main
while True:
    print(generate_Question("H"))

