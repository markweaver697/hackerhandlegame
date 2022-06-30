from cgi import parse_multipart
import random
import tkinter
import easygui
import random

def gethandle():
        text = "what is your handle?"
        title = "Tell me who you are"
        output = easygui.enterbox(text, title)
        message = (str(output))
        return(message.lower())


def handlegame():
    masterofdisaster=[
    "You're hopeless, man, utterly hopeless",
    "Now I'm trying to save you from yourself but you gotta stop letting your mama dress you, man!",
    "What are you, stoned or stupid?",
    "Where are your brains, in your ass? Don't you know anything?",
    "Stupid, man. It's universally stupid.",
    "Look, you wanna be elite? You gotta do a righteous hack. None of this accidental shit.",
    ]
    zerocool=[
    "What, your mom buy you a 'Puter for Christmas?",
    "there's an Olympic-size swimming pool up on the roof.",
    "U HAVE TREAD\n UPON MY DOMAIN & \n MUST NOW SUFFER \n WHO R U?",
    "ACID BURN\n SEZ LEAVE B 4\nU R EXPUNGED",
    ]
    cerealkiller=[
        "you can I crash at your place tonight?"
    ]
    lordnikon=[
        "he has an identic memory"
    ]
    acidburn=[
        "you're in the butterzone now baby"
    ]
    phantom = ['this is gonna be good']
    answers = ['cereal killer', 'acid burn','zero cool', 'master of disaster', 'lord nikon''phantom phreak', 'king of nynex']
    text = "Do you have a handle?"
    title = "Hacker Check 0.2 beta"
    output = easygui.ynbox(text,title)
    if output:
        handlename = gethandle()
        if (handlename in answers):
            if (handlename == 'zero cool' or handlename == 'crash override'):
                quote = random.choice(zerocool)
                title = "Hello Dade!"
            if (handlename == 'master of disaster'):
                quote = random.choice(zerocool)
                title = 'Hello Joey!'
            if (handlename == 'acid burn'):
                quote = random.choice(acidburn)
                title = 'Hello Kate'
            if (handlename == 'cereal killer'):
                quote = random.choice(cerealkiller)
                title = "Hello Emmanuel! Are you the dude who started 2600 magazine?"
            if (handlename == 'lord nikon'):
                quote = random.choice(lordnikon)
                title = "Hello Paul!"
            if (handlename == 'phantom phreak' or handlename == 'king of nynex'):
                quote = random.choice(phantom)
                title = "Hello Paul!"

            message =(f"{quote} \n Do you want to play again?")
            msg = easygui.ynbox(message, title) 
            if  msg:
                handlegame()
            else:
                exit()
        else:
            message =(f"{handlename} , What kind of name is that? I've neveer heard of you \n you're hopeless!\n Do you want to play again?")
            title = "You're handle isin't cool enough"
            msg = easygui.ynbox(message,title)
            if msg:
                handlegame()
            else:
                exit()
    else:
        message =("you have to have a handle to play the game\n Do you want to play again?")
        title = "No handle, No play"
        msg = easygui.ynbox(message,title)
        if msg:
            handlegame()
        else:
            exit()
             
handlegame()
