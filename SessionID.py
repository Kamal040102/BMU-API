import random
import string

def createSessionID():
    lower = string.ascii_lowercase
    upper = string.ascii_uppercase
    num = string.digits

    var = lower + upper + num

    sessionId = ''.join(random.sample(var, 50))
    return sessionId

print(createSessionID())