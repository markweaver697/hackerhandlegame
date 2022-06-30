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

def zerocool():
    quotes =[
    "What, your mom buy you a 'Puter for Christmas?",
    "there's an Olympic-size swimming pool up on the roof.",
    "U HAVE TREAD\n UPON MY DOMAIN & \n MUST NOW SUFFER \n WHO R U?",
    "ACID BURN\n SEZ LEAVE B 4\nU R EXPUNGED",
    ]
    title = "Hello Dade!"
    return quotes, title

def masterofdisaster():
    quotes=[
    "You're hopeless, man, utterly hopeless",
    "Now I'm trying to save you from yourself but you gotta stop letting your mama dress you, man!",
    "What are you, stoned or stupid?",
    "Where are your brains, in your ass? Don't you know anything?",
    "Stupid, man. It's universally stupid.",
    "Look, you wanna be elite? You gotta do a righteous hack. None of this accidental shit.",
    ]
    title = "Hello Joey!"
    return quotes, title

def cerealkkiller():
    quotes=[
        "you can I crash at your place tonight?"
    ]
    title = "Hello Emmanuel! Are you the dude who started 2600 magazine?"
    return quotes, title

def lord_nikon():
    quotes =[
    "he has an identic memory"
    ]
    title = "Hello Paul!"
    return quotes, title

def acidburn():
    quotes=[
    "you're in the butterzone now baby"
    ]
    title = "hello Kate!"
    return quotes, title

def phantonphreak():
    quotes = ['this is gonna be good']
    title = "Hello Ramon!"
    return quotes, title

handles_dict = {
    "zero cool":zerocool(),
    "crash override": zerocool(),
    "master of disaster": masterofdisaster(),
    "cereal killer": cerealkkiller(),
    "acid burn": acidburn(),
    "lord nikon": lord_nikon(),
    "phantom phreak":phantonphreak(),
    "king of nynex":phantonphreak()
}

def handlegame():
    answers = ['cereal killer', 'acid burn','zero cool', 'master of disaster', 'lord nikon','phantom phreak', 'king of nynex']
    text = "Do you have a handle?"
    title = "Hacker Check 0.2 beta"
    output = easygui.ynbox(text,title)
    if output:
        handlename = gethandle()
        handlename = handlename.lower()
        if (handlename in answers):
            quotes, title =  handles_dict.get(handlename)
            quote = random.choice(quotes)   
            message =(f"{quote} \n Do you want to play again?")
            msg = easygui.ynbox(message, title) 
            if  msg:
                handlegame()
            else:
                exit()
        else:
            message =(f"{handlename} , What kind of name is that? I've never heard of you \n you're hopeless!\n Do you want to play again?")
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
