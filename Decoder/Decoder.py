# -*- coding: utf-8 -*-
import random

def get_pad():
    with open("/Users/acolby/Documents/Testing/Vernam + transfomation/Encoder/encoder_side_pad","r") as padfile:
        pad = padfile.read()
    return(pad)

def set_pad(pad):
    with open("/Users/acolby/Documents/Testing/Vernam + transfomation/Encoder/encoder_side_pad","w") as padfile:
        padfile.write(pad)

def get_message():
    with open("/Users/acolby/Documents/Testing/Vernam + transfomation/Transmission_file","r") as messagefile:
        message = messagefile.read()
    return(message)

# all random methods should really be fully random but I can't be bothered
def generateRandomList(length,padRange,seed):
    Start,End = padRange
    length = len(pad)
    if(seed):
        random.seed(seed)
    return([random.randint(Start,End) for _ in range(length)])

def changePad(padRange,seed = None):
    pad = get_pad()
    padLength = len(pad)
    offset = generateRandomList(padLength,padRange,seed)
    newPad = ""
    for i in range(padLength):
        newPad += chr((ord(pad[i]) + offset[i]) % padRange[1])
    return(newPad)

def decode(message,padRange):
    pad = get_pad()
    newMessage = ""
    for i in range(len(message)):
        newMessage += chr(ord(message[i])^ord(pad[i]))
    # experimental, uses a function applied to the message to get the next seed
    # this is based on the fact that the message itself will be pseudo-random
    useMessage = False
    if(useMessage):
        total = 0
        position = 1
        for i in message:
            total += ord(i)*position
            position += 1
        random.seed(total)
        seed = random.randint(1,10000)
        # I assume the random module has a good way of convuluting the number inputted
    else:
        seed = int(newMessage[0:6])
        newMessage = newMessage[6:]
    newPad = changePad(padRange,seed)
    return(newMessage,newPad)

pad = get_pad()
padLength = len(pad)
padRange = (50,200)
message = get_message()
message,pad = decode(message,padRange)
print("it is done!")
print("the message is:\n {}\n\nthe new pad is:\n".format(message))
