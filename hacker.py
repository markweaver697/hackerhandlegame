import random
def hackerhandle():
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
    handle = input("Do you have a handle?\n Answer Yes or No:\n")
    if (handle.lower() !='no' and handle.lower() !='yes'):
        print('Your answer must be yes or no')
        hackerhandle()
    elif (handle.lower() == 'no'):
            print(random.choice(nohandle))
            hackerhandle()
    elif (handle.lower() == 'yes'):
            print(random.choice(yeshandle))

