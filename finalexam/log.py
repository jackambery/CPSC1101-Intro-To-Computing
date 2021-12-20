
class Log:
    
    def __init__(self, chatNumber, question, response):
        self.chatNumber = chatNumber
        self.question = question
        self.response = response
        
    def __repr__(self):
        s = "chat #" + str(self.chatNumber) + ":\nuser: " + str(self.question) + "\nchatbot: " + str(self.response) + "\n"
        print(s)   