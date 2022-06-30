from cgi import parse_multipart
import random
import tkinter
from turtle import end_poly
import easygui
import random

from matplotlib.pyplot import pause

def handlegame():
    nohandle=[
     "You're hopeless, man, utterly hopeless",
     "Now I'm trying tosave you from yourself but you gotta stop letting your mama dress you, man!",
     "What are you, stoned or stupid?",
     "Whereare your brains, in your ass? Don't you knowanything?",
     "Stupid, man. It's universally stupid.",
     "Look, you wanna be elite? You gotta do a righteous hack. None of this accidental shit.",
    ]
    yeshandle=[
     "What, your mom buy you a 'Puter for Christmas?",
     "there's an Olympic size swimming pool up on the roof.",
     "U HAVE TREAD\n UPON MY DOMAIN & \n MUST NOW SUFFER \n WHO R U?",
     "ACID BURN\n SEZ LEAVE B 4\nU R EXPUNGED",
    ]
    text = "Do you have a handle?"
    title = "Hacker Check 0.2 beta"
    output = easygui.ynbox(text,title)
    if output:
        quote = random.choice(yeshandle)
        message =f"${quote} \n Do you want to play again?"
        title = "you're a somebody"
        msg = easygui.ynbox(message, title)
        if msg:
            handlegame()
        else:
            exit()
        
    else:
        quote = random.choice(nohandle)
        message =f"${quote} \n Do you want to play again?"
        title = "you're a nobody"
        msg = easygui.ynbox(message,title)
        if msg:
            handlegame()
        else:
            exit()

