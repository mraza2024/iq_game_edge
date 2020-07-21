#how smart are you?

print("Welcome to the Intellectual Game! You will see 10 questions that will test your general knowledge and intelligence. Your goal is to answer all the questions correctly, otherwise the game will stop. At the end of the game, the program will show your result. Good luck!")

questions=["Which of these is a type of hat? (a)Sausage roll, b)Pork pie, c)Scotch egg, d)Potato crisp",
                 "Which of these have to pass a test on ‘The Knowledge’ to get a licence? a) Taxi drivers, b) Bus drivers, c) Police officers, d) Ambulance drivers",
                 "Which of these phrases refers to a brief success? a)Blaze in the pot, b)Spark in the tub, c)Flare in the jug, d)Flash in the pan",
                 "The young of which creature is known as a squab?  a)Salmon, b)Horse, c)Pigeon, d)Octopus,
                 "Which of these US presidents appeared on the television series 'Laugh-In?'  a)Lyndon Johnson  b)Richard Nixon  c)Jimmy Carter d)Gerald Ford"
          "Which insect shorted out an early supercomputer and inspired the term 'computer bug'? a)Moth  b)Roach  c)Fly  d)Japanese beetle"
          "Which of the following men does not have a chemical element named for him? a)Albert Einstein  b)Niels Bohr  c)Isaac Newton  d)Enrico Fermi]
answers=["b", 
              "a",
              "d", 
              "c",
         "b"
         "a"
        "c"
        ]
recomends=[]
import random 
x=random.randint(0,4)
print ("Question 1:" + questions[x])
answer_right=answers[x]
answer_user=input("What is your answer?")
  
if answer_right==answer_user:
  print("Wow! Your answer is right!")
  #while answer_right==answer_user:
    
else:
  print("Unfortunately, your answer is wrong. However, you can i,prove your knowledge by reading or watching the next: "+recomends[x])
  print("You have answered "+str(NUMBER OF RIGHT QUESTIONS)+" questions right.")
 #also we need to show the user his level somehow, like 1-3 questions - average level, 4-6 - above average, 7-10 - extraordinarily smart)
  break

print("Thank you for taking part in our quiz!")

