# "Automate the Boring Stuff" Book
# CH8: randomQuizGenerator.py - Creates quizzes with questions and answers in
# random order, along with the answer key

import random

#the quiz data. Keys are states and vaues are their capitals.
capitals = {'Alabama': 'Montgomery', 'Alaska': 'Juneau', 'Arizona': 'Phoenix',
   'Arkansas': 'Little Rock', 'California': 'Sacramento', 'Colorado': 'Denver',
   'Connecticut': 'Hartford', 'Delaware': 'Dover', 'Florida': 'Tallahassee',
   'Georgia': 'Atlanta', 'Hawaii': 'Honolulu', 'Idaho': 'Boise', 'Illinois':
   'Springfield', 'Indiana': 'Indianapolis', 'Iowa': 'Des Moines', 'Kansas':
   'Topeka', 'Kentucky': 'Frankfort', 'Louisiana': 'Baton Rouge', 'Maine':
   'Augusta', 'Maryland': 'Annapolis', 'Massachusetts': 'Boston', 'Michigan':
   'Lansing', 'Minnesota': 'Saint Paul', 'Mississippi': 'Jackson', 'Missouri':
   'Jefferson City', 'Montana': 'Helena', 'Nebraska': 'Lincoln', 'Nevada':
   'Carson City', 'New Hampshire': 'Concord', 'New Jersey': 'Trenton', 'New Mexico':
    'Santa Fe', 'New York': 'Albany', 'North Carolina': 'Raleigh',
   'North Dakota': 'Bismarck', 'Ohio': 'Columbus', 'Oklahoma': 'Oklahoma City',
   'Oregon': 'Salem', 'Pennsylvania': 'Harrisburg', 'Rhode Island': 'Providence',
   'South Carolina': 'Columbia', 'South Dakota': 'Pierre', 'Tennessee':
   'Nashville', 'Texas': 'Austin', 'Utah': 'Salt Lake City', 'Vermont':
   'Montpelier', 'Virginia': 'Richmond', 'Washington': 'Olympia', 'West Virginia':
    'Charleston', 'Wisconsin': 'Madison', 'Wyoming': 'Cheyenne'}

# Generate 35 quiz files.
for quizNum in range(35):
    # Create the quiz and answer key files.
    quizFile= open('C:\\Users\\PATTY\\Desktop\\loops\\python_command\\capitalsquiz%s.txt' % (quizNum + 1), 'w')
    answerKeyFile= open('C:\\Users\\PATTY\\Desktop\\loops\\python_command\\capitalsquiz_answers%s.txt' % (quizNum + 1),'w')

    #Write out the header for the quiz.
    quizFile.write('Name:\n\nDate:\n\nPeriod:\n\n')
    quizFile.write((' ' * 20) + 'State Capitals Quiz (Form %s)' % (quizNum +1))
    quizFile.write('\n\n')

    #Shuffle the order of the states.
    states= list(capitals.keys())
    random.shuffle(states)


#Loop through all 50 states, making a question for each.
    for questionNum in range(50):

        #Get right and wrong answers.
        correctAnswer= capitals[states[questionNum]]        #capital[keys], this gets the right capital(value) from input key 
        wrongAnswers= list(capitals.values())               #gets the shuffled list of all values(capitals)
        del wrongAnswers[wrongAnswers.index(correctAnswer)]        #delete the right capital from the list
        wrongAnswers = random.sample(wrongAnswers,3)        #gets 3 capitals from the list and stored them in a list 'wrongAnswers'
        answerOptions = wrongAnswers + [correctAnswer]      #Add the correct answer to the list, now it has 4 members
        random.shuffle(answerOptions)
    

        #Write the question and the answer options to the quiz file.
        quizFile.write('%s. What is the capital of %s?\n' % (questionNum+1, states[questionNum]))

        for i in range(4):
            quizFile.write(' %s. %s\n' %('ABCD'[i], answerOptions[i]))
            quizFile.write('\n')

        #Write the answer key to a fike.
        answerKeyFile.write('%s. %s\n' %(questionNum + 1, 'ABCD' [answerOptions.index(correctAnswer)]))

quizFile.close()
answerKeyFile.close()

    
