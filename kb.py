questions = [
    "Which is the largest planet in our solar system?",
    "Who painted the Mona Lisa?",
    "What is the capital city of Australia?",
    "What is the national animal of India?",
    "Which country won the FIFA World Cup in 2018?"
]

options = [
    ["A. Jupiter", "B. Saturn", "C. Mars", "D. Earth"],
    ["A. Leonardo da Vinci", "B. Vincent van Gogh", "C. Pablo Picasso", "D. Michelangelo"],
    ["A. Sydney", "B. Melbourne", "C. Canberra", "D. Brisbane"],
    ["A. Tiger", "B. Lion", "C. Elephant", "D. Peacock"],
    ["A. Germany", "B. Brazil", "C. France", "D. Argentina"]
]

answers = ["A", "A", "C", "A", "C"]

def k():
    s = 0
for i in range(len(questions)):
    print("\nquestion1" , i+1 ,questions[i])

    for option in options[i]:# in this in is the main thing that has caused problem
        print(option) # it is used for j in optioms[i] means options[i] in j and j is printed means
        # options of i have been printed

    h = input("enter any one of the follow A/B/C/D")

    if(h == answers[i]):
        print("correct option")
        s = s+1
    else:
        print("wrong answer")
        break

k()
