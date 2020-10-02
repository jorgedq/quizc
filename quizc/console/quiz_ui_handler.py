from quizc.console.quiz_input_handler import QuestionInputHandler
from quizc.console.quiz_ui_menu import QuizUIMenu
from quizc.model.quiz import Quiz
from quizc.model.quiz_answers import QuizAnswer, Answer


class QuizUIHandler(object):

    @staticmethod
    def create_quiz() -> Quiz:
        menu = QuizUIMenu()
        return menu.handle_create_quiz()

    @staticmethod
    def fill_quiz(quiz) -> QuizAnswer:
        quiz_answer = QuizAnswer(quiz)
        question_handler = QuestionInputHandler()
        print("\tQuiz: " + quiz.title)

        for question in quiz.questions:
            answers = question_handler.ask_question_value(question)
            answer = Answer(answers, question)
            quiz_answer.add_answer(answer)

        return quiz_answer

    @staticmethod
    def show_quiz(quiz_answer):
        print("\tQuiz: "+ quiz_answer.quiz.title)
        print("=============================================")
        print("\n")
        count = 1
        for answer in quiz_answer.answers:
            print("# Question "+str(count)+":"+ answer.question.title)
            print("\tAnswer.- "+ answer.answers[0])
            print("\n")
            count += 1

        return quiz_answer
