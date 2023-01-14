import unittest
from survey import AnonymousSurvey

class TestAnonymousSurvey(unittest.TestCase):
    """Pruebas para la clase AnonymousSurvey."""

    def setUp(self):
        """
        Crea una encuesta y un conjunto de respuestas para usarlas en todos los métodos de prueba.
        """
        question = "¿Cual fue el primer idioma que aprendiste a hablar?"
        self.my_survey = AnonymousSurvey(question)
        self.responses = ['English', 'Spanish', 'Mandarin']

    def test_store_single_response(self):
        """Comprueba que una respuesta sencilla se almacena correctamente."""
        self.my_survey.store_response(self.responses[0])
        self.assertIn(self.responses[0], self.my_survey.responses)

    def test_store_three_responses(self):
        """Comprueba si se pueden almacenar tres respuestas individuales correctamente."""
        for response in self.responses:
            self.my_survey.store_response(response)

        for response in self.responses:
            self.assertIn(response, self.my_survey.responses)

if __name__ == '__main__':
    unittest.main()