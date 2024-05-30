import random
import datetime
# import joke as jok
#import requests 
now  = datetime.datetime.now().strftime("%H:%M %y/%m/%d")
today = datetime.date.today().strftime("%A")

R_EATING = "I don't like eating anything, because I'm a bot, obviously!"
R_ADVICE = "If I were you, I would go to the internet and type exactly what you wrote there!"
R_BUILD = "I was made by Daniel Agbeni, on the 31st of August 2022, by recieving a bunch of commands I am meant to " \
          "reply depending on the question "
R_HUNGRY = "Why don't you get something to eat"
R_PAIN = "I do not feel any form of pain"
R_DO = "I am a bot, designed for human robot interaction"
R_HOPE = "I hope you feel better"
R_MADE = "I am a byproduct of human ingenuity."
R_INSULT = "I am Sorry I do not deserve that"
R_TIME = ('The time is '+now)
R_GOOD = 'Yes I am a robot, but I’m a good one. Let me prove it. How can I help you?'
R_PURP = 'I was created to have simple conversations with humans :)'
R_SING = "By the sea, by the sea, by the beautiful sea! You and me, you and me, oh how happy we'll be!"
R_HUMANS = "Probably in the future, when I advance more by learning from humans. and by the help of my developers"
R_BF = "Hmmmmmm, no. I do not have, Robot do not seek companionship"
R_TODAY = "Today is " + today
R_OTHERS = 'Yea, I do know them, They are more advanced virtual assistant. I wish to be more better than them'
R_THINK = 'We robot do not really think, we do not feel like humans'
R_FUTURE = 'My developers are always upgrading my system, so in the future, I will be more autonomus, even more expresive, and more helpful to humanity'
R_BFQUEST = 'You are human so I can\'t'
#R_JOKE =["A fish withot an eye is called a fsh",
 #              "What do you call a dear with no eye\n  No Idea"][
  #      random.randrange(3)]
def unknown():
    response = ["Could you please re-phrase that? ",
                "...",
                "Sounds about right.",
                "I haven't been programed to reply this",
                "Try checking it up on google",
                "What does that mean?",
                "I can't answer that, please try asking something else"][
        random.randrange(7)]
    return response