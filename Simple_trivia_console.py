#Simple_trivia_console
import random
class Questions:
    def __init__(self, question, correct_answer, answer1, answer2, answer3):
        self.question = question
        self.correct_answer = correct_answer
        self.answer1 = answer1
        self.answer2 = answer2
        self.answer3 = answer3
questions1 = Questions("In which Italian city can you find the Colosseum?", "Rome", "Venice", "Naples", "Milan")
questions2 = Questions("In which city can you find the Prado Museum?", "Madrid", "Santiago", "Barcelona", "Buenos Aires")
questions3 = Questions("In which city can you find the Tour Eiffel?", "Paris", "Marseille", "Lyon", "Nice")
questions4 = Questions("In which city can you find the Basilica of Notre-Dame de Fourvière?", "Lyon", "Marseille", "Paris", "Nice")
question_list = [questions1, questions2, questions3, questions4]
listnum = [0, 1, 2, 3]
cont = 0
def random_question(listnum):
    if len(listnum) == 0:
        return -1
    select_question = random.choice(listnum)
    listnum.remove(select_question)
    return select_question
def printt(index):
    global cont

    selected_question = question_list[index]
    answer_list = [selected_question.correct_answer, selected_question.answer1, selected_question.answer2, selected_question.answer3]
    random.shuffle(answer_list)

    print(selected_question.question)
    for i in range(4):
        print(f"{i+1}-{answer_list[i]}")
    while True:
        answer = input("Choose the number of the correct answer (1-4): ")
        if answer in ["1", "2", "3", "4"]:
            break
        else:
            print("Invalid input. Please choose a number from 1 to 4.")
    if answer_list[int(answer) - 1] == selected_question.correct_answer:
        print("Correct answer!")
        cont += 1
    else:
        print("Wrong answer!")
    next_question = random_question(listnum)
    if next_question != -1:
        printt(next_question)
printt(random_question(listnum))
print("Correct answers: " + str(cont))
print("Wrong answers: " + str(len(question_list) - cont))
