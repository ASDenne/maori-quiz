while True:
    question = ""
    numbers = ["Tahi","rua","toru","whā","rima","ono","whitu","waru","iwa"]
    Answer = int(input(">>"))
    if len(str(Answer)) == 1:
        question = numbers[Answer-1].upper()
    elif Answer == 10:
        question = "Tekau"
    elif Answer % 10 == 0:
        question = numbers[(Answer//10)-1].upper() + " tekau"
    print(question)
    else:
