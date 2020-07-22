
#declaring the class Question
class Question:
    def __init__(self, mcq, answer):
        self.mcq = mcq
        self.answer = answer
#introduction note
print("Welcome to the Intellectual Game! You will see 10 questions that will test your general knowledge and intelligence.Each question will have 1 point. At the end of the game, the program will show your result.\n\n Good luck!")

print()
#list of the questions that user will see
questions_mcqs = [

"Which of these is a type of hat?\n (a)Sausage roll\n (b)Pork pie\n (c)Scotch egg\n (d)Potato crisp\n\n",

"Which of these have to pass a test on ‘The Knowledge’ to get a licence?\n (a) Taxi drivers\n (b) Bus drivers\n (c) Police officers\n (d) Ambulance drivers\n\n",

"Which of these phrases refers to a brief success?\n (a)Blaze in the pot\n (b)Spark in the tub\n (c)Flare in the jug\n (d)Flash in the pan\n\n",

"The young of which creature is known as a squab?\n (a)Salmon\n (b)Horse\n (c)Pigeon\n (d)Octopus\n\n",

"Which of these US presidents appeared on the television series 'Laugh-In'?\n (a)Lyndon Johnson\n (b)Richard Nixon\n (c)Jimmy Carter\n (d)Gerald Ford\n\n",

"Which of the following landlocked countries is entirely contained within another country?\n (a)Lesotho\n (b)Mongolia\n (c)Burkina Faso\n (d)Luxemburg\n\n",

"In the children’s book series, where is Paddington Bear originally from?\n (a)India\n (b)Peru\n (c)Canada\n (d)Iceland\n\n",

"During World War II, US soldiers used the first commercial aerosol cans to hold what?\n (a)Cleaning fluid\n (b)Antiseptic\n (c)Insecticide\n (d)Shaving cream\n\n",

"The US icon Uncle Sam was based on Samuel Wilson who worked during the War of 1812 as a what?\n (a)Meat Inspector\n (b)Mail deliverer\n (c)Historian\n (d)Weapons mechanic\n\n",

"Now used to refer to a cat, the word 'tabby' is derived from the name of a district of what world capital?\n (a)Baghdad\n (b)Cairo\n (c)New Delhi\n (b)Moscow\n\n"]

#list of the right answers for questions
questions = [
    Question(questions_mcqs[0],"b"),
    Question(questions_mcqs[1],"a"),
    Question(questions_mcqs[2],"d"),
    Question(questions_mcqs[3],"c"),
    Question(questions_mcqs[4],"b"),
    Question(questions_mcqs[5],"a"),
    Question(questions_mcqs[6],"b"),
    Question(questions_mcqs[7],"c"),
    Question(questions_mcqs[8],"a"),
    Question(questions_mcqs[9],"a")]

#function that sets the grading system of our quiz: the right answer adds a point to it, the wrong answer keeps it the same
def start_quiz(questions):
    point = 0
    for question in questions:
        answer = input(question.mcq +"Enter your answer = ")
        if answer == question.answer:
            point += 1
#the program shows the grade of a user (number of answers he got right)
    print("Your totals points are " +str(point)+"/10")
#the quiz starts when we call this function
start_quiz(questions)

