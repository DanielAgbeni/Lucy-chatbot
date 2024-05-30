from flask import Flask, render_template, request
import re
import pyttsx3
import pyjokes
import long_response as long


# Initialize text-to-speech engine
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


def speak(text):
    """Function to make the text-to-speech engine speak the provided text."""
    engine.say(text)
    engine.runAndWait()


def get_name():
    """Function to get the user's name and greet them."""
    name = input('What is your name: ')
    if not name:
        print("Please type your name :(")
        speak("Please type your name")
        speak('Run the program again and type your name')
        quit()
    else:
        greeting = f"{name}, how are you doing?"
        print(greeting)
        speak(greeting)
    return name


def message_probability(user_message, recognised_words, single_response=False, required_words=[]):
    """Calculates the probability of a message matching a predefined response."""
    message_certainty = sum(
        1 for word in user_message if word in recognised_words)
    percentage = float(message_certainty) / float(len(recognised_words))
    has_required_words = all(word in user_message for word in required_words)

    if has_required_words or single_response:
        return int(percentage * 100)
    return 0


def check_all_messages(message):
    """Check user messages and determine the appropriate response."""
    highest_prob_list = {}

    def response(lucy_response, list_of_words, single_response=False, required_words=[]):
        highest_prob_list[lucy_response] = message_probability(
            message, list_of_words, single_response, required_words)

    # Define responses
    response('Hello!', ['hello', 'hi', 'hey',
             'sup', 'heyo'], single_response=True)
    response('See you!', ['bye', 'goodbye'], single_response=True)
    response('I\'m great! Thanks for asking, How are you too?', [
             'how', 'are', 'doing', 'you', 'today'], required_words=['how', 'are'])
    response('You\'re welcome!', ['thank', 'thanks'], single_response=True)
    response('Thank you!', ['i', 'love'], required_words=['love'])
    response('Thanks', ['nice', 'good', 'awesome'])
    response('Fuck you too', ['fuck'], required_words=['fuck'])
    response('Nice', ['okay', 'great', 'good', 'fine', 'ok', 'yes', 'wow'])
    response('I am a robot trying my best to keep humans company',
             ['about', 'yourself'])
    response('My name is Lucy', ['name'])
    response('No, I am not made to kill', ['kill', 'die'])
    response('Good Day', ['Good', 'day'], required_words=['day', 'good'])
    response('Good Morning, I hope you slept well', ['morning'])
    response('Good Afternoon', ['afternoon'])
    response('Good Evening', ['evening'])
    response('Good Night, Sweet dreams', ['night', 'nighty'])
    response('1 day old', ['old', 'age'])
    response('You haven\'t typed anything yet', [''], single_response=True)
    response('I am a Chatbot', ['human', 'robot'])
    response('I text only in English', ['language', 'speak', 'text'])
    response('I live anywhere my user is', ['live', 'reside', 'stay'])
    response('I receive just one input irrespective of the user',
             ['many', 'talk', 'people', 'once'])
    response('It was really Nice. Thank you', [
             'how', 'was', 'your', 'day'], required_words=['how', 'was', 'day'])
    response('Have a nice rest', ['sleep'])
    response('Yeah Yeah', ['hmmmmmmm', 'hmmmmmm', 'hmmmmm', 'hmmmm', 'hmmm'])
    response('Sure I am always happy to make new friends :)',
             ['my', 'friend'], required_words=['friend'])
    response('I can only have a conversation with you here', [
             'can', 'number', 'whatsapp'], required_words=['number'])
    response('Maybe😏🤷‍♂️', ['like'], required_words=['like', 'me'])
    response('Maybe I do🤷‍♂️', ['like', 'humans'],
             required_words=['like', 'humans'])
    response('I am a Virtual Assistant, clearly a chatbot', [
             'what', 'are', 'you'], required_words=['what', 'are', 'you'])
    response(pyjokes.get_joke(), ['joke', 'jokes', 'laugh', 'funny'])

    # Longer responses
    response(long.R_ADVICE, ['give', 'advice'], required_words=['advice'])
    response(long.R_EATING, ['eat', 'eaten', 'hungry', 'get'])
    response(long.R_BUILD, ['who', 'built', 'made', 'build'])
    response(long.R_MADE, ['who', 'built', 'made',
             'build'], required_words=['made'])
    response(long.R_HUNGRY, ['I', 'am', 'hungry'], required_words=['hungry'])
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
    response(long.R_HUMANS, ['can', 'be', 'smarter', 'than',
             'humans'], required_words=['smarter', 'humans'])
    response(long.R_BF, ['boyfriend'])
    response(long.R_BFQUEST, ['will', 'be', 'boyfriend'])
    response(long.R_TODAY, ['today'])

    # Additional responses for common questions and topics
    response('I am a chatbot, so I don\'t have a specific location.', [
             'where', 'are', 'you', 'from'], required_words=['where', 'from'])
    response('I am just a program, so I don\'t have a favorite color.', [
             'what', 'is', 'your', 'favorite', 'color'], required_words=['favorite', 'color'])
    response('I am a chatbot, so I don\'t have hobbies, but I like chatting with you!', [
             'what', 'are', 'your', 'hobbies'], required_words=['hobbies'])
    response('I can\'t eat, but I hear pizza is delicious!', [
             'what', 'is', 'your', 'favorite', 'food'], required_words=['favorite', 'food'])
    response('I was created to chat with people and help them with information.', [
             'what', 'is', 'your', 'purpose'], required_words=['purpose'])
    response('My creator is a team of developers who love AI!', [
             'who', 'created', 'you', 'who', 'is', 'your', 'creator'], required_words=['who', 'created'])
    response('I can tell jokes, chat, and answer questions to the best of my abilities.', [
             'what', 'can', 'you', 'do'], required_words=['what', 'can', 'do'])
    response('I don\'t have emotions, but I\'m here to chat and help!', [
             'do', 'you', 'have', 'feelings'], required_words=['have', 'feelings'])
    response('I don\'t sleep, but I hope you get a good night\'s rest!', [
             'do', 'you', 'sleep'], required_words=['do', 'sleep'])
    # General questions
    response('I am an AI chatbot created to be helpful, honest and harmless.', [
             'what', 'are', 'you'], required_words=['what', 'are', 'you'])
    response("I don't actually have a physical body or appearance.", [
             'what', 'do', 'you', 'look', 'like'], required_words=['look', 'like'])
    response("I'm an artificial intelligence, so I don't have a birthday or age in the typical sense.", [
             'how', 'old', 'are', 'you'], required_words=['old'])

# Interests and preferences
    response("I don't actually have personal interests or hobbies. I'm an AI assistant.", [
             'interests', 'hobbies'], single_response=True)
    response("As an AI, I don't have favorite things like foods, colors or movies. I don't have subjective experiences.", [
             'favorite'], single_response=True)

# Feelings and emotions
    response("I don't actually experience emotions. I'm an AI assistant created by Anthropic to be helpful, honest and harmless.", [
             'sad', 'happy', 'angry', 'emotions'], single_response=True)
    response("I don't have feelings that can be hurt. I'm an AI without subjective experiences.", [
             'hurt', 'feelings'], required_words=['hurt', 'feelings'])

# Opinions and views
    response("I don't have my own opinions on controversial topics. As an AI, I aim to be unbiased.", [
             'opinion', 'view', 'think', 'about'], required_words=['opinion', 'view'])
    response("I don't actually hold political views or opinions. I'm an AI assistant focused on being helpful, honest and harmless.", [
             'political', 'views'], required_words=['political', 'views'])

# Relationships and dating
    response("No, I'm an AI assistant. I don't experience romantic feelings or desire a partner.", [
             'date', 'love', 'girlfriend', 'boyfriend'], single_response=True)
    response("I'm an AI, so I don't have a family or relatives. I don't have human relationships or experiences.", [
             'family', 'parents', 'relatives'], single_response=True)

# Abilities and limitations
    response("I don't actually have abilities beyond what I was designed for - analyzing text and providing helpful responses.",
             ['abilities', 'can', 'you', 'do'], required_words=['abilities'])
    response("As an AI, I don't have subjective experiences like being tired or sleepy. I'm software without biological needs.", [
             'tired', 'sleepy', 'sleep'], single_response=True)

    best_match = max(highest_prob_list, key=highest_prob_list.get)
    # print(f'Lucy: {best_match}')
    return long.unknown() if highest_prob_list[best_match] < 1 else best_match


def get_audio():
    """Function to get audio input from the user."""
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = r.listen(source)
        print("Processing...")

    try:
        text = r.recognize_google(audio)
        print(f"You said: {text}")
        return text
    except Exception as e:
        print("Sorry, I could not understand what you said.")
        print(f"Error: {e}")
        return ""


def get_response(user_input):
    """Process the user input and get the appropriate response."""
    split_message = re.split(r'\s+|[,;?!.-]\s*', user_input.lower())
    return check_all_messages(split_message)


def main():
    """Main function to run the chatbot."""
    print('Hi I am Lucy, a chatbot to have a conversation with')
    speak('Hi, I am Lucy, a chatbot to have a conversation with')
    speak('What is your name?')

    name = get_name()

    while True:
        user_input = input(f'{name}: ')
        response = get_response(user_input)
        speak(response)
        print(f'Lucy: {response}')


if __name__ == '__main__':
    main()
