from PreguntasCiencia import science_questions

def pregunta(tema):
    for index, question in enumerate(tema, start=1):
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
        
temas = [science_questions, history_questions, film_questions, art_questions]

while any(temas):
    temas_disponibles = [i for i, tema in enumerate(temas) if tema]  # Obtener índices de temas con preguntas
    if not temas_disponibles:
        break  # Salir del bucle si no quedan temas con preguntas
    
    tema_actual = choice(temas_disponibles)  # Elegir un tema aleatorio con preguntas restantes
    preguntas_del_tema = temas[tema_actual]  # Obtener las preguntas del tema actual

    pregunta(preguntas_del_tema[0])  # Presentar la primera pregunta del tema seleccionado

    # Eliminar la pregunta para evitar repetirla
    preguntas_del_tema.pop(0)
    temas[tema_actual] = preguntas_del_tema  # Actualizar la lista de preguntas del tema
