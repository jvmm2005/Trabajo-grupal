from PreguntasCiencia import science_questions


for index, question in enumerate(science_questions, start=1):
    print(f"Question {index}: {question.pregunta}")
    options = question.getOpciones()
    for i, option in enumerate(options, start=1):
        print(f"{i}. {option}")
    while True:
        user_answer = input("Enter your answer (1, 2, 3, or 4): ")
        if user_answer.isdigit() and 1 <= int(user_answer) <= 4:
            break
        else:
            print("Invalid input. Please enter a number between 1 and 4.")

    user_answer_index = int(user_answer) - 1
    is_correct = question.validateAnswer(options[user_answer_index])
    
    if is_correct:
        print("Correct!")
    else:
        print(f"Wrong! Correct answer is: {question.respuesta_correcta}")
        
        

        

