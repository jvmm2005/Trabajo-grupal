from random import choice
from PreguntasCiencia import science_questions
from HistoryCuestions import history_cuestions
from PreguntasDeporte import sports_question
from PreguntasArte import art_question

def pregunta(tema):
    index = 1
    while tema:  # Mientras haya preguntas en el tema
        selected_question = choice(tema)  # Seleccionar una pregunta aleatoria
        print(f"Question {index}: {selected_question.pregunta}")
        options = selected_question.getOpciones()
        for i, option in enumerate(options, start=1):
            print(f"{i}. {option}")     
        while True:
            user_answer = input("Enter your answer (1, 2, 3, or 4): ")
            if user_answer.isdigit() and 1 <= int(user_answer) <= 4:
                break
            else:
                print("Invalid input. Please enter a number between 1 and 4.")

        user_answer_index = int(user_answer) - 1
        is_correct = selected_question.validateAnswer(options[user_answer_index])

        if is_correct:
            print("Correct!")
        else:
            print(f"Wrong! Correct answer is: {selected_question.respuesta_correcta}")
        
        tema.remove(selected_question)  # Eliminar la pregunta del tema
        index += 1  # Incrementar el índice de la pregunta

# Agrupar las preguntas por tema en una lista
temas = [science_questions, history_cuestions, sports_question, art_question]

while any(temas):
    tema_actual = choice([i for i, tema in enumerate(temas) if tema])  # Elegir un tema aleatorio con preguntas restantes
    preguntas_del_tema = temas[tema_actual]  # Obtener las preguntas del tema actual

    if preguntas_del_tema:  # Verificar si hay preguntas en el tema seleccionado
        pregunta(preguntas_del_tema)  # Presentar todas las preguntas del tema seleccionado
        temas[tema_actual] = []  # Vaciar la lista de preguntas del tema seleccionado
