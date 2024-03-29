# initialize
from random import choice, randint
from time import sleep
from os import system, path, listdir
import subprocess
from datetime import datetime
try:
    conf = open("settings.conf") # open configuration file
    settings = conf.readlines() # read it
    music_dir = (settings[0])
except:
    print("please run setup.py for music functionality")
yes = ["of course", "yes", "that's right", "certainly"]
no = ["no", "of course not", "no way", "definitely not"]
thanks = ["thank you", "thanks", "thank you so much"]
wow = ["oh my gosh", "wow", "incredible", "amazing", "truly incredible"]
what = ["huh?", "what?", "i don't know what you mean by that"]
dont_know = ["i don't know", "i have no idea", "i dunno", "no idea"]
jokes = ["why did the chicken cross the road?", "what did the paleontologist say to the dinosaur?", "what is the strongest creature in the world?", "what is the best season to jump on a trampoline?", "can a kangaroo jump higher than a house?", "patient to his doctor: i have forgotten so many things lately, and its getting worse. what can i do?", "why did my washing machine stop pumping out water?", "what did the judge say when he went to the dentist?"]
answers = ["to get to the other side", "i've got a bone to pick with you", "the snail. It carries its whole house on its back", "spring time", "of course, a house can't jump at all", "doctor: yes, this is a known illness, unfortunately it has no cure. i'd also like to remind you about the 800 u.s. dollars that you owe me?", "and more importantly, where is my hamster?", "do you swear to pull the tooth, the whole tooth, and nothing but the tooth?"]
lastQuestion = "lol, nothing :P" # the last question alice was asked(in this case, nothing)
# definitions
def replace_spaces(original, rep): # input, what you want to replace the spaces with
    word = []
    string = ""
    for i in range(len(original)):
        word.append(original[i])
    for i in range(len(word)):
        if(word[i] == " "):
            word[i] = rep
    for i in range(len(word)):
        string = string + word[i]
    return(string)
def solve(question):
    try:
        inp = question.split(" ")
        if(inp[2] == "plus" or "and" or "+"):
            return(int(inp[1]) + int(inp[3]))
        if(inp[2] == "minus" or "-"):
            return(int(inp[1]) - int(inp[3]))
        if(inp[2] == "times" or "*"):
            return(int(inp[1]) * inp[3])
        if(inp[2] == "/"):
            return(int(inp[1]) / inp[3])
    except:
        pass
def say(info):
    print(info)
    system('pico2wave -w alice-voice.wav "' + info + '" && aplay alice-voice.wav')
# processing
def process():
    if(question[0:4] == "say "):
        say(question[4:])
    elif(question == "may i ask you a question" or question == "can i ask you something" or question == "may i ask you something" or question == "can i ask you a question"):
        say("you can ask")
    elif(split[0] == "hi" or question[0:5] == "hello" or question[0:12] == "good morning" or question[0:14] == "good afternoon"):
        say("hello to you too")
    elif(question[0:26] == "what is a good recipe for "):
        say("here are some good recipes for " + question[26:])
        say("you may be asked for your preferences on how you would like it")
        system("/usr/bin/x-www-browser www.yummly.com/recipes/" + replace_spaces(question[31:], "+") + question[26:] + " &")
    elif(question[0:31] == "what are some good recipes for "):
        say("here are some good recipes for " + question[31:])
        say("you may be asked for your preferences on how you would like it")
        system("/usr/bin/x-www-browser www.yummly.com/recipes/" + replace_spaces(question[31:], "+") + " &")
    elif(question == "who is your creator" or question == "who created you" or question == "when were you created" or question == "when were you born"):
        say("i was created some time in 2018 by Jonathan Schaffer")
    elif(question == "what is your name" or question == "what's your name" or question == "who are you"):
        say("my name is alice")
        if(question == "who are you"):
            say("i am a virtual assistant")
    elif(question[0:14] == "can i call you"):
        if(question[-5:] == "alice"):
            say("of course, that is my name")
        else:
            say("but my name is alice, not " + question[15:] + ". anyway, no you may not, if you don't like my name then tell my creator")
    elif(question == "what is the news" or question == "what is the latest news"):
        system("/usr/bin/x-www-browser cnn.com npr.com abcnews.go.com nbcnews.com &")
        say("here are some news websites")
    elif(question == "what day is today" or question == "what is today" or question == "what day is it" or question == "what is the date" or question == "what day is it today"):
        say("today is " + datetime.now().strftime("%A, %B %d"))
    elif(question == "what is the time" or question == "what time is it" or question == "what is the time" or question == "what time is it now"):
        say("it is " + datetime.now().strftime("%l:%M %p"))
    elif(question[0:5] == "go to" and question[-4:] == ".com"):
        say("going to " + question[6:])
        system("/usr/bin/x-www-browser " + question[6:])
    elif(question == "tell me a joke" or question == "give me a joke" or question == "tell me another joke"):
        jokenum = randint(0, len(jokes) - 1)
        say("ok, here is a good one")
        say(jokes[jokenum])
        say(answers[jokenum])
        say("ha ha ha")
    elif(question[0:14] == "are you spying" or question == "are you a spy"):
        say("i am not spying on you or anyone")
    elif(question == "aptitude moo"):
        say("haven't you learned your lesson from aptitude? There are no Easter Eggs in this program.")
    elif(question[:10] == "search for"):
        system("/usr/bin/x-www-browser https://duckduckgo.com/?q=" + replace_spaces(question[11:], "+") + " &")
        say("searching")
    elif(split[0] == "define"):
        system("/usr/bin/x-www-browser http://www.dictionary.com/browse/" + replace_spaces(question[7:], "+") + " &")
        say("definition of " + question[7:])
    elif(question == "what songs do i have" or question == "what music do i have"):
        say("here is a list of all the music i can currently play:")
        for file in listdir(music_dir):
            if(file.endswith(".wav") or file.endswith(".mid")):
                say(file[:-4])
    elif(split[0] == "play"):
        if(path.exists(music_dir + "/" + question[5:] + ".wav") or question[5:] == "nothing"):
            system("pkill aplay ; pkill timidity")
            say("playing " + question[5:])
            system("aplay " + music_dir + "/" + replace_spaces(question[5:], "\ ") + ".wav &")
        elif(path.exists(music_dir + "/" + question[5:] + ".mid")):
            system("pkill aplay ; pkill timidity")
            say("playing " + question[5:])
            system("timidity " + music_dir + "/" + replace_spaces(question[5:], "\ ") + ".mid &")
        else:
            say("I can only play midi and wave files from the music folder, either add them to the music folder or check that you spelled them right")
    elif(question == "stop"):
        system("pkill aplay && pkill timidity")
    elif(question == "what can you do"):
        say("""i can open web pages, tell jokes, search for things online, tell
you the date and time, play music, give you good recipes, and much more""")
    elif(question[0:4] == "who " or question[0:4] == "why " or question[0:4] == "can " or question[0:5] == "does " or question[0:5] == "when " or question[0:3] == "do " or question[0:3] == "is " or question[0:5] == "does " or question[0:5] == "will " or question[0:4] == "what" or question[0:4] == "how " or question[0:8] == "convert "):
        system("/usr/bin/x-www-browser https://duckduckgo.com/?q=" + replace_spaces(question, "+") + " &")
        say("here is what i found")
# main loop
while True:
    try:
        question = raw_input("").lower()
        split = question.split(' ')
        process()
        lastQuestion = question
    except KeyboardInterrupt:
        say("bye!")
        break
    except:
        say("oops, i just made a mistake, can you please tell jonathan what you said so he can fix it?")
