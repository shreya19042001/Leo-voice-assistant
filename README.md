# Leo-voice-assistant

Leo Voice Assistant is a Python script that acts as a voice-controlled assistant. It can perform various tasks like searching Wikipedia, opening websites, playing music, telling the time, and sending emails.

## Features

- **Greeting**: Provides a personalized greeting based on the time of day.
- **Wikipedia Search**: Searches Wikipedia and reads out the summary of the results.
- **Website Navigation**: Opens specified websites like YouTube, Google, and Stack Overflow.
- **Music Playback**: Plays the first song from a specified music directory.
- **Time**: Announces the current time.
- **Email**: Sends an email based on the user’s voice command.

## Libraries Used

- **`pyttsx3`**: For text-to-speech conversion.
- **`speech_recognition`**: For recognizing speech from the microphone.
- **`datetime`**: For handling date and time.
- **`wikipedia`**: For searching and retrieving Wikipedia summaries.
- **`webbrowser`**: For opening web pages in a browser.
- **`os`**: For interacting with the operating system, like file paths.
- **`smtplib`**: For sending emails via SMTP.

## Installation

1. Install the required libraries using pip:
   pip install pyttsx3 speech_recognition wikipedia
