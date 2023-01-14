from survey import AnonymousSurvey

# Define una pregunta y haz una encuesta.
question = "¿Cual fue el primer idioma que aprendiste a hablar?"
my_survey = AnonymousSurvey(question)

# Muestra la pregunta y almacena las respuestas a la pregunta
my_survey.show_question()
print("Introduce 'q' en cualquier momento para terminar.\n")
while True:
    response = input("Language: ")
    if response == 'q':
        break
    my_survey.store_response(response)

# Muestra los resultados de la encuesta.
print("\nGracias a todos por participar en la encuesta!")
my_survey.show_results()