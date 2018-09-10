import unittest

class Survey():
    def __init__(self, question):
        self.question = question
        self.responses = []
    def show_question(self):
        print (self.question)
    def store_response(self, new_response):
        self.responses.append(new_response)
    def show_result(self):
        print("Survey result:")
        for response in self.responses:
            print (response)

def main():
    question = "what language do you speak?"
    my_survey = Survey(question)
    my_survey.show_question()
    print("Press q to quit")
    while(True):
        answer = input("Enter the language you speak: ")
        if answer == 'q':
            break
        my_survey.store_response(answer)
    print("Thank you for being a part of the survey")
    my_survey.show_result()

# testing the class
class TestSurvey(unittest.TestCase):

    def test_store_single_response(self):
        question = "what lang do you speak?"
        test_survey = Survey(question)
        test_survey.store_response("English")
        self.assertIn("English", test_survey.responses)

    def test_store_multiple_responses(self):
        question = "whang lang you speak?"
        test_survey = Survey(question)
        test_survey.responses = ["English","Chinese","French"] # put in the possible re
        for response in test_survey.responses:
            self.assertIn(response,test_survey.responses)

    # now a demo of the setup method, this method allows user to setup values that will be used in the test
    def setUp(self):
        question = "What lang you speak?"
        self.my_survey = Survey(question)
        self.responses = ["English","Chinese","French"]
    
    def test_case_2_use_setUp(self): # single input testing USING setUp()
        self.my_survey.store_response(self.responses[0])
        self.assertIn(self.responses[0], self.my_survey.responses)
    def test_case_3_use_setUp(self): # multi input testing USING setUp()
        for response in self.responses:
            self.my_survey.store_response(response)
        for response in self.responses:
            self.assertIn(response, self.my_survey.responses)



unittest.main()