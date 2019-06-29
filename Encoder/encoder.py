# -*- coding: utf-8 -*-
'''
The concept:
A vernam cipher is mathematically a perfect way of transmitting a message, but
it requires a pre-transmission decided pad, which has to be the length of the
message encoded.

If a transformation to perform on the key is encoded along with the message,
then the initial pad can be changed but still be known by both sides, and can be
re-used.
'''

import random
import os

filePrefix = os.getcwd() + "/"

def get_pad():
    with open(filePrefix + "encoder_side_pad","r") as padfile:
        pad = padfile.read()
    return(pad)

def set_pad(pad):
    with open(filePrefix + "encoder_side_pad","w") as padfile:
        padfile.write(pad)

def set_message(message):
    with open("/Users/acolby/Documents/Testing/Vernam + transfomation/Transmission_file","w") as messagefile:
        messagefile.write("")
        messagefile.write(message)

# all random methods should really be fully random but I can't be bothered
# the python random module is only pseudo-random
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

def encode(message,padRange):
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
        # I assume the random module has a good way of convuluting the number inputted
    seed = random.randint(1,10000)
    newPad = changePad(padRange,seed)
    pad = get_pad()
    if(not(useMessage)):
        message = str(seed).zfill(6) + message
    newMessage = ""
    for i in range(len(message)):
        newMessage += chr(ord(message[i])^ord(pad[i]))
    return(newMessage,newPad)

pad = get_pad()
padLength = len(pad)
padRange = (50,200)
message = input("input the message to be encoded:   ")
message, pad = encode(message,padRange)
print("the message is:\n {}\n\nthe new pad is:\n {}\n\nstoring message...".format(message,pad))
set_message(message)
print("done.")
