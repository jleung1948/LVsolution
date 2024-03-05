from gtts import gTTS
import os

def text_to_speech(text, lang='en'):
    tts = gTTS(text=text, lang=lang, slow=False)  # Create a gTTS object
    filename = "/mnt/data/speech.mp3"  # Define the output file path
    tts.save(filename)  # Save the spoken text to a file
    return filename

# Example usage
text = "Hello, welcome to the world of Python text to speech conversion."
output_file = text_to_speech(text)

print(f"Audio file created at: {output_file}")