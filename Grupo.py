import random
class preguntas():
    def __init__ (self, pregunta, respuesta_correcta, respuesta1, respuesta2, respuesta3):
        self.pregunta= pregunta
        self.respuesta_correcta = respuesta_correcta
        self.respuesta_correcta
        self.respuesta1 = respuesta1
        self.respuesta2 = respuesta2
        self.respuesta3 = respuesta3
        self.respuestas = [self.respuesta_correcta, self.respuesta1, self.respuesta2, self.respuesta3]
    
    
    def getOpciones (self):
        random.shuffle(self.respuestas)
        return self.respuestas
    
    def validateAnswer(self,awnser):
        if awnser == self.respuesta_correcta:
            return True
        else:
            return False
        


science_questions = [
    preguntas("What is the powerhouse of the cell?", "Mitochondria", "Ribosome", "Nucleus", "Endoplasmic reticulum"),
    preguntas("Which planet is known as the Red Planet?", "Mars", "Venus", "Jupiter", "Mercury"),
    preguntas("What is the chemical symbol for water?", "H2O", "CO2", "NaCl", "O2"),
    preguntas("What is the name of the man made thing that is further away?", "Voyager 1", "Hubble telescope", "Voyager 2", "ISS"),
    preguntas("What is the name of the spaceship that brought man to the moon?", "Saturn 5", "Falcon 9", "Starship", "Artemis 1"),
    preguntas("What is not a original Nobel prize?", "Economy", "Phisics", "Chemistry", "Literature"),
    preguntas("In what era the dinosaurs became extinct?", "Cretaceous", "Jurasic", "Triassic", "Paleocene"),
    preguntas("In what year the Higgs bosson was discoverd?", "2012", "2014","2008" , "2010"),
    preguntas("What space shuttles exploded?", "Columbia", "Atlantis", "Discovery", "Enterprise"),
    preguntas("WHat (a+b)(e2) equals to?", "a(e2) + 2ab +b(e2)", "a(e2) + b(e2)", "a(e2) + b(e2) + ab", "(ab)(e2)"),
]
    
    
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
        
        
        