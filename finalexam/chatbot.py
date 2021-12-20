
import random 
from log import Log

def createKnownResponses():
    questions = {
        "what do you have?": "We have chocolates, lollipops, and gummy bears.",
        "chocolate?": "We do have chocolate!",
        "chocolate price?": "$3",
        "lollipops?": "We do have lollipops!",
        "lollipop price?": "$0.50",
        "gummy bears?": "We do have gummy bears!",
        "gummy bears price?": "$4"
    }
    return questions

def createUnknownResponses():
    unknowns = [
        "We will have those in stock soon, sorry!", 
        "Jolly Jack's Candy is the place to be!", 
        "We use only the best ingredients!", 
        "Jack would be happy to talk to you more in person!",
        "Try asking, \"what do you have?\""
    ]
    return unknowns

def runReport(logHistory):
    for log in logHistory:
        print(log.__repr__()) # not sure why I had to explicitly call the repr here, but I was running into huge issues without it

def questionsToLearn(unansweredQuestionList):
    try:
        with open("questionsToLearn.txt", "w") as outfile:
            for question in unansweredQuestionList:
                outfile.write(question)
    except Exception as e:
        print("Something went wrong: " + e)

def process(d, l):
    
    unansweredQuestions = []
    logHistory = []
    chatNumber = 1

    print("Welcome to Jolly Jack's Candy Store website!")
    print("Let me help you find what is in stock or how much an item is!")        
    while True:
        print("If you would like to quit, select \"q\"")
        request = str(input())
        
        if request == "q":
            runReport(logHistory)
            questionsToLearn(unansweredQuestions)
            quit()

        response = d.get(request)
        if response == None:
            unansweredQuestions.append(request)
            response = random.choice(l)
        print(response)
        
        currentLog = Log(chatNumber, request, response)
        logHistory.append(currentLog)
        chatNumber += 1

def main():
    d = createKnownResponses()
    l = createUnknownResponses()
    process(d, l)

if __name__ == "__main__":
    main()
