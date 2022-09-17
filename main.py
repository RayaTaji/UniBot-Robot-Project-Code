
import speech_recognition as sr
import pyttsx3
import datetime


listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
recognizer = sr.Recognizer()


#Dictionary classes

class Lecture:
   lectures = {'logicWhr': 'Floor 2 Room 201',
               'logicW': 'sunday & tuesday from 1:30 to 2:30 pm',
               'Data MiningWhr': 'Floor 2 Room 209',
               'Data MiningW': 'sunday & tuesday from 12:30 to 1:30 pm',
               'Software DesignWhr': 'Floor 2 Room 206',
               'Software DesignW': 'Monday & Wednesday from 9:00 to 10:30 am'}
l1 = Lecture.lectures

class Departments:
   HeadDPT = {'AI': ['Dr Muhammad al shariah, his office is at floor 3 room 111'],
              'CS': ['Dr Abdul Rahman , his office is at floor 3 room 444'],
              'SE': ['Dr Qassim al Kharma , his office is at floor 3 room 222'],
              'CSec': ['Dr Mosleh , his office is at floor 3 room 555']}
d1 = Departments.HeadDPT

class Calendar:
   calender = {'Mid Exams': ['Mid exams start in 17th of april  & end in 12th of may '],
               'Subject Deadline': ['The deadline for teaching subjects is in june 9th '],
               'Final Exams': ['Final exams start in 19th of june and end in 26th of june'],
               'Summer Vacation': ['Summer vacation begins in 29th of june and ends in 14th of july']}
c1 = Calendar.calender

class Locations:
   location = {'washroom': ['There''s a washroom at first floor & third for only students & floor 3 for only staff'],
               'library': ['It''s in the 3rd floor'],
               'prayroom': ['There is a prayer room in 1st floor and another one in 2nd floor'],
               'Auditorium': ['There is an Auditorium in 1st floor'],
               'Restaurant': ['There is a Restaurant after the Horani building']}
lc = Locations.location

class ExamHalls:
   exams = {'database': 'starts at 12 pm and ends at 2 pm Sunday June 2, room no 201, second floor',
            'logic': 'starts at 10:30 am and ends at 12 pm Sunday June 2, room no 206, second floor',
            'calculus': 'starts at 9 am and ends at 11 am Sunday June 2, room no 209, second floor'}
e = ExamHalls.exams

#Our robot's speech config

def talk(text):
    engine.say(text)
    engine.runAndWait()

newVoiceRate = 140
engine.setProperty('rate', newVoiceRate)


# noinspection PyBroadException
def take_command():
    try:

       with sr.Microphone() as source:
            recognizer.adjust_for_ambient_noise(source, 1.2)
            recognizer.energy_threshold = 10000

            print('Listening...')
            voice = listener.listen(source, phrase_time_limit=4)
            command = listener.recognize_google(voice)
            command = command.lower()




    except:
        pass
    return command

def run_uni():
    command = take_command()
    print(command)

    # Greeting when started
    if 'hey uni' in command:

     hour = int(datetime.datetime.now().hour)

     if 0 <= hour < 12:
            print("Good morning, I'm Uni Bot, How can i help you?")
            talk("Good morning, I'm Uni Bot, How can i help you?")

     elif 12 <= hour < 18:
            print("Good afternoon, I'm Uni Bot, How can i help you?")
            talk("Good afternoon, I'm Uni Bot, How can i help you?")

     elif hour > 18:
            print("Good evening, I'm Uni Bot, How can i help you?")
            talk("Good evening, I'm Uni Bot, How can i help you?")

#Extra services done by UniBot
    #where is the dean office

    elif ' dean office ' in command:
        ans = command.replace('where is the dean office of it faculty', '')
        print('floor 3 room 201')
        talk('floor 3 room 201' + ans)
        talk('Do you have anymore questions?')

    #what's the time?
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        print(time)
        talk('Current time is ' + time)
        talk('Do you have anymore questions?')

    #Who are the Head departments
    elif 'ai' in command:

        print(d1['AI'])
        talk(d1['AI'])
        talk('Do you have anymore Questions?')

    elif 'software engineering' in command:

        print(d1['SE'])
        talk(d1['SE'])
        talk('Do you have anymore Questions?')

    elif 'computer science' in command:

        print(d1['CS'])
        talk(d1['CS'])
        talk('Do you have anymore Questions?')


    elif 'cyber security' in command:
        print(d1['CSec'])
        talk(d1['CSec'])
        talk('Do you have anymore Questions?')

# Lectures time and place
    elif 'where is the logic lecture' in command:
        print(l1['logicWhr'])
        talk(l1['logicWhr'])
        talk('Do you have anymore Questions?')

    elif 'when is the logic lecture' in command:
        print(l1['logicW'])
        talk(l1['logicW'])
        talk('Do you have anymore Questions?')

    elif 'where is the data mining lecture' in command:
        print(l1['Data MiningWhr'])
        talk(l1['Data MiningWhr'])
        talk('Do you have anymore Questions?')

    elif 'when is the data mining lecture' in command:
        print(l1['Data MiningW'])
        talk(l1['Data MiningW'])
        talk('Do you have anymore Questions?')

    elif 'where is the software design lecture' in command:
        print(l1['Software DesignWhr'])
        talk(l1['Software DesignWhr'])
        talk('Do you have anymore Questions?')

    elif 'when is the software design lecture' in command:
        print(l1['Software DesignW'])
        talk(l1['Software DesignW'])
        talk('Do you have anymore Questions?')

    #calender
    elif 'when are the midterm exams' in command:
        print(c1['Mid Exams'])
        talk(c1['Mid Exams'])
        talk('Do you have anymore Questions?')

    elif 'when are the final exams' in command:
        print(c1['Final Exams'])
        talk(c1['Final Exams'])
        talk('Do you have anymore Questions?')

    elif 'when is the deadline for teaching subjects' in command:
        print(c1['Subject Deadline'])
        talk(c1['Subject Deadline'])
        talk('Do you have anymore Questions?')

    elif 'when is the summer vacation' in command:
        print(c1['Summer Vacation'])
        talk(c1['Summer Vacation'])
        talk('Do you have anymore Questions?')

#Locations
    elif 'where is the prayer room' in command:

        print(lc['prayroom'])
        talk(lc['prayroom'])
        talk('Do you have anymore Questions?')

    elif 'where is the washroom' in command:

        print(lc['washroom'])
        talk(lc['washroom'])
        talk('Do you have anymore Questions?')

    elif 'where is the library' in command:
        print(lc['library'])
        talk(lc['library'])
        talk('Do you have anymore Questions?')

    elif 'auditorium' in command:
        print(lc['Auditorium'])
        talk(lc['Auditorium'])
        talk('Do you have anymore Questions?')

    elif 'restaurant' in command:
        print(lc['Restaurant'])
        talk(lc['Restaurant'])
        talk('Do you have anymore Questions?')

    elif ' calculus exam' in command:
        print(e['calculus'])
        talk(e['calculus'])
        talk('Do you have anymore Questions?')

    elif ' database exam' in command:
        print(e['database'])
        talk(e['database'])
        talk('Do you have anymore Questions?')

#end program
    else:
        if 'no' in command:
            talk('Have a Nice Day')
            print('Have a Nice Day')
            exit()


        else:
          talk('I could not hear that. Please repeat')

while True:
 run_uni()
