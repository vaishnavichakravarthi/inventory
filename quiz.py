import random
"""Random is imported"""

def getLines(fileIn):
    numLines = 0
    for i in enumerate(fileIn):
        numLines+=1
    return numLines

def random_line(fileIn,numLines):
    x = random.randint(0,numLines-1)
    for i,line in enumerate(fileIn):
        if(i == x):
            return line
    return "Nothing to display! Try adding some questions first into 'questions.txt' first."

class QuizMaker:
	"""Here we start the quiz"""

    def __init__(self):

        self.result = 0

    def show(self,flag):

        self.f = open("questions.txt")
        if(flag):

            numLines = getLines(self.f)

            self.f = open("questions.txt")
            """opens the text file where questions are stored"""
            questionLine = random_line(self.f,numLines)

            if(questionLine == "Nothing to display! Try adding some questions first into 'questions.txt' first."):
                print(questionLine)
                return
            
            question = questionLine.rpartition('?')

            print(question[0])

            x = input()
            if(x == 'quit'):

                    print("\n======================================")
                    print("You did a great job! You scored ",end='')
                    print(self.result,end='')
                    print(" points.")
                    print("\nEnter 1 to play again!")

                    x = int(input())

                    if(x == 1):
                        self.result = 0
                        self.show(True)
                    else:
                        print("\n======================================")
                        print("Hope you had fun! Until next time...")
                        return

            answer = question[2][1:].replace("\n",'')

            if(x == answer):
            	"""If answer is right it adds points to it"""
                print("\n======================================")
                print("Great! That was right! Here's the next question.[Enter 'quit' to exit quiz.] ")
                print("======================================")
                self.result += 1
                self.show(True)

            else:
            	"""else it comes out of the program and restarts the quiz"""
                print("\n======================================")
                print("Oops. You got it wrong. :(\n")
                print("The correct answer is: ",end='')
                print(answer,end='.\n')
                print("You did a great job! You scored ",end='')
                print(self.result,end='')
                print(" points.\n")
                print("Enter 1 to play again or anything else to quit!")

                x = int(input())
                print("\n======================================")

                if(x == 1):
                    self.result = 0
                    self.show(True)
                else:
                    print("Hope you had fun! Until next time...\n")
                    return

def main():

    myQuiz = QuizMaker()
    print("\n======================================")
    print("Welcome to QuizMaster Pro! Ready to play? Here it comes!")
    print("======================================")

    myQuiz.show(True)

if __name__ == "__main__":
    main()
