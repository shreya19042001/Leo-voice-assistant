import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import smtplib

# Initialize text-to-speech engine
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning!")
    elif hour >= 12 and hour < 18:
        speak("Good Afternoon!")
    else:
        speak("Good Evening!")
    speak("I am Leo. How may I help you?")

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        try:
            audio = r.listen(source)
            print("Recognizing...")
            query = r.recognize_google(audio, language='en-in')
            print(f"User said: {query}\n")
            return query
        except sr.UnknownValueError:
            print("Sorry, I did not understand that.")
            return "None"
        except sr.RequestError as e:
            print(f"Could not request results from Google Speech Recognition service; {e}")
            return "None"
        except KeyboardInterrupt:
            speak("Program interrupted. Exiting...")
            print("Program interrupted. Exiting...")
            exit()

def sendEmail(to, content):
    try:
        if content is None or content.strip() == "":
            print("Empty content. No email sent.")
            return
        
        smtp_user = 'sanaahshan@gmail.com'  # Your email address
        smtp_pass = 'Shreya@19'  # Your email password
        
        if not smtp_user or not smtp_pass:
            print("Email credentials are not set.")
            return

        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(smtp_user, smtp_pass)
        server.sendmail(smtp_user, to, content)
        server.close()
    except Exception as e:
        print(f"Failed to send email: {e}")

if __name__ == "__main__":
    wishMe()
    try:
        while True:
            query = takeCommand().lower()
            if 'wikipedia' in query:
                speak('Searching Wikipedia...')
                query = query.replace("wikipedia", "")
                try:
                    results = wikipedia.summary(query, sentences=2)
                    speak("According to Wikipedia")
                    print(results.encode('utf-8', errors='ignore').decode('utf-8'))
                    speak(results)
                except wikipedia.exceptions.DisambiguationError:
                    speak(f"Multiple results found for {query}. Please be more specific.")
                except wikipedia.exceptions.PageError:
                    speak(f"No results found for {query}.")
                except Exception as e:
                    print(e)
                    speak("Sorry, I couldn't retrieve the information.")

            elif 'open youtube' in query:
                webbrowser.open("youtube.com")

            elif 'open google' in query:
                webbrowser.open("google.com")

            elif 'open stackoverflow' in query:
                webbrowser.open("stackoverflow.com")

            elif 'play music' in query:
                music_dir = 'D:\\Non Critical\\songs\\Favourite Songs2'
                if os.path.exists(music_dir):
                    songs = os.listdir(music_dir)
                    if songs:
                        print(songs)
                        os.startfile(os.path.join(music_dir, songs[0]))
                    else:
                        speak("No songs found in the directory.")
                else:
                    speak(f"Directory does not exist. Please check the directory {music_dir}")

            elif 'the time' in query:
                strTime = datetime.datetime.now().strftime("%H:%M:%S")
                speak(f"The time is {strTime}")

            elif 'email' in query:
                speak("What should I say in the email?")
                content = takeCommand()
                if content and content.lower() != "none":
                    to = "shreyaguptajnvb@gmail.com"
                    sendEmail(to, content)
                    speak("Email has been sent!")
                else:
                    speak("No content provided for the email.")

            elif 'stop' in query:
                speak("Thank you, have a great day!")
                break

            else:
                speak("Sorry, I did not understand the command. Please try again.")
    except KeyboardInterrupt:
        speak("Program interrupted. Exiting...")
        print("Program interrupted. Exiting...")
