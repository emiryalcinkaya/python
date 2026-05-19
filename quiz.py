questions = {'What is the capital of Turkey?': 'ankara',
            'What is 2 + 2?': '4',
            'What color is the sky?': 'blue'
             }

score = 0

for question in questions:

    entered_answer = input(question + " ").lower()

    if entered_answer == questions[question]:
        print("Correct!!")
        score += 1

    else: 
        print("Wrong!!")

print("Score:", score)
