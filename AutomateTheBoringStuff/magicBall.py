
import random

def getAnswer(answerName):
    if answerName == 1:
        return "It is certain."
    
    elif answerName == 2:
        return "It is decidedly."
    
    elif answerName == 3:
        return "Yes"
    
    elif answerName == 4:
        return "Reply hazy try again."
    
    elif answerName == 5:
        return "Ask again later"
    
    elif answerName == 6:
        return "Concentrate and ask again."
    
    elif answerName == 7:
        return "My reply is on."
    
    elif answerName == 8:
        return "Outlook not so good."
    
    elif answerName == 9:
        return "Very doudtfull."
    
#i = random.randint(1, 9)
#fortune = getAnswer(i)
#print(fortune)

print(getAnswer(random.randint(1, 9)))