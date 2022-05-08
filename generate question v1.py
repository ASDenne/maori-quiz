import random
def generate_Question(diffuclty):
    numbers = ["Tahi","rua","toru","whā","rima","ono","whitu","waru","iwa"]
    if diffuclty == "Easy":
        Answer = random.randint(1,9)
        question = numbers[Answer].upper()



    else:
        Answer = random.randint(1,99)
        if len(str(Answer)) == 1:
            question = numbers[Answer].upper()
        elif Answer == 10:
            question = "Tekau"
        elif Answer == 0:
            question = numbers[Answer].upper() + "tekau"



#main
generate_Question("H")
