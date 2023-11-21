import random
class preguntas():
    def __init__ (self, pregunta, respuesta_correcta, respuesta1, respuesta2, respuesta3):
        self.pregunta= pregunta
        self.respuesta_correcta = respuesta_correcta
        self.respuesta1 = respuesta1
        self.respuesta2 = respuesta2
        self.respuesta3 = respuesta3
        self.respuestas = [self.respuesta_correcta, self.respuesta1, self.respuesta2, self.respuesta3]
    
    
    def getOpciones(self):
        random.shuffle(self.respuestas)
        return self.respuestas
    
    def validateAnswer(self,answer):
        if answer == self.respuesta_correcta:
            return True
        else:
            return False
        

    