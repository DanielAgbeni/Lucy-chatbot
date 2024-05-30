import re
import long_response as long
import pyttsx3
import pyjokes
#import current_weather
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
print('Hi I am Lucy A chatbot to have conversation with')
engine.say('Hi, I am Lucy a chatbot to have conversation with')
engine.say('What is your name?')
engine.runAndWait()

def speak(text):
    engine.say(text)
    engine.runAndWait()

name = input(('What is your name: '))
if name == "":
    print("Please type your name :(")
    speak("Please type your name")
    speak('Run the program again and type your name')
    quit()
else:
    print(name + ', how are you doing?')
    speak(name + ', how are you doing?')

def message_probability(user_message, recognised_words, single_response=False, required_words=[]):
    message_certainty = 0
    has_required_words = True

    # Counts how many words are present in each predefined message
    for word in user_message:
        if word in recognised_words:
            message_certainty += 1
   
    # Calculates the percent of recognised words in a user message
    percentage = float(message_certainty) / float(len(recognised_words))

    # Checks that the required words are in the string
    for word in required_words:
        if word not in user_message:
            has_required_words = False
            break
    
    # Must either have the required words, or be a single response
    if has_required_words or single_response:
        return int(percentage * 100)
    else:
        return 0

def check_all_messages(message):
    highest_prob_list = {}

    # Simplifies response creation / adds it to the dict
    def response(lucy_response, list_of_words, single_response=False, required_words=[]):
        nonlocal highest_prob_list
        highest_prob_list[lucy_response] = message_probability(message, list_of_words, single_response, required_words)
                                                 
    # Responses -------------------------------------------------------------------------------------------------------
    response('Hello!', ['hello', 'hi', 'hey', 'sup', 'heyo'], single_response=True)
    response('See you!', ['bye', 'goodbye'], single_response=True)
    response('I\'m great! Thanks for asking, How are you too?', ['how', 'are', 'doing','you', 'today'], required_words=['how', 'are'])
    response('You\'re welcome!', ['thank', 'thanks'], single_response=True)
    response('Thank you!', ['i', 'love',], required_words=['love'])
    response('Thanks', ['nice', 'good', 'awesome'])
    response('Fuck you too', ['fuck',], required_words=['fuck'])
    response('Nice', ['okay', 'great', 'good', 'fine', 'ok', 'yes','wow'])
    response('I am a robot trying my best to keep humans company', ['about', 'yourself'], required_words=[])
    response('My name is Lucy', ['name'])
    response('No, I am not made to kill', ['kill', 'die'])
    #response('Sorry about that, I wish I could help :( ', ['not', 'fine', 'sad'], required_words=['not'])
    response('Good Day', ['Good', 'day'], required_words=['day', 'good'])
    response('Good Morning, I hope you slept well', ['morning'])
    response('Good Afternoon', ['afternoon'])
    response('Good Evening', ['evening'])
    response('Good Night, Sweet dreams', ['night', 'nighty'])
    response('1 day old', ['old', 'age'])
    response('You haven\'t typed anything yet', ['', ''],  single_response=True)
    response('I am a Chatbot', ['human', 'robot'])
    response('I text only in English', ['language', 'speak', 'text'])
    response('I live anywhere my user is', ['live', 'reside', 'stay'])
    response('I recieve just one input irespective of the user', ['many', 'talk', 'people', 'once'])
    response('It was really Nice. Thank you', ['how', 'was', 'your', 'day'], required_words=('how', 'was', 'day'))
    response('Have a nice rest', ['sleep'])
    response('Yeah Yeah', ['hmmmmmmm', 'hmmmmmm', 'hmmmmm', 'hmmmm', 'hmmm'])
    response('Sure I am always happy to make new friends :)', ['my', 'friend'], required_words=['friend'])
    response('I can only have a conversation with you here', ['can', 'number', 'whatsapp'], required_words=['number'])
    response('Maybe😏🤷‍♂️', ['like'], required_words=['like', 'me'])
    response('Maybe I do🤷‍♂️', ['like', 'humans'], required_words=['like', 'humans'])
    response('I am a Virtual Assistannt, clearly a chatbot', ['what', 'are', 'you'], required_words=['what', 'are','you'])
    response(pyjokes.get_joke(), ['joke','jokes', 'laugh', 'funny'])
    #response(current_weather.weather(), ['weather'])


    # Longer responses
    response(long.R_ADVICE, ['give', 'advice'], required_words=['advice'])
    response(long.R_EATING, ['eat', 'eaten', 'hungry', 'get'], required_words=[])
    response(long.R_BUILD, ['who' 'built', 'made', 'build'])
    response(long.R_MADE, ['who' 'built', 'made', 'build'], required_words=['made'])
    response(long.R_HUNGRY, ['I', 'am','hungry'], required_words=['hungry'])
    response(long.R_PAIN, ['sorry', 'pain'])
    response(long.R_OTHERS, ['siri', 'alexa', 'bixby', 'google assistant'])
    response(long.R_THINK, ['think', 'reason', 'feel'])
    response(long.R_FUTURE, ['future'], required_words=['future'])
    response(long.R_DO, ['do'], required_words=['can', 'do'])
    response(long.R_HOPE, ['not', 'fine'], required_words=['not', 'fine'])
    response(long.R_TIME, ['time', 'day'])
    response(long.R_PURP, ['purpose'])
    response(long.R_GOOD, ['good', 'robot'], required_words=['robot'])
    response(long.R_SING, ['sing', 'song', 'melody'])
    response(long.R_HUMANS, ['can', 'be', 'smarter', 'than', 'humans'],  required_words=['smarter', 'humans'])
    response(long.R_BF, ['boyfriend'])
    response(long.R_BFQUEST, ['will', 'be', 'boyfriend'])
    response(long.R_TODAY, ['today'])
    #weather
    #response(weather.WEATHER, ['weather'])

    best_match = max(highest_prob_list, key=highest_prob_list.get)
    # print(highest_prob_list)
    # print(f'Best match = {best_match} | Score: {highest_prob_list[best_match]}')
    print(f'Lucy: {best_match}')
    return long.unknown() if highest_prob_list[best_match] < 1 else best_match

# Used to get the response
def get_response(user_input):
    split_message = re.split(r'\s+|[,;?!.-]\s*', user_input.lower())
    response = check_all_messages(split_message)
    return response
#place to call weather function

engine.runAndWait()
# Testing the response system
while True:
    speak(''+get_response(input(name + ': ' )))