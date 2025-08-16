import os
import subprocess
import platform
from gtts import gTTS

def text_to_speech_with_gtts(input_text, output_filepath):
    language="en"

    audioobj= gTTS(
        text=input_text,
        lang=language,
        slow=False
    )
    audioobj.save(output_filepath)
    os_name = platform.system()
    try:
        if os_name == "Windows":  # Windows
            subprocess.run(['powershell', '-c', f'(New-Object Media.SoundPlayer "{output_filepath}").PlaySync();'])
        else:
            raise OSError("Unsupported operating system")
    except Exception as e:
        print(f"An error occurred while trying to play the audio: {e}")


#input_text = "Hi, I am doing fine, how are you? This is a test for Rohiya Shafiq"
#output_filepath = "test_text_to_speech.mp3"
#text_to_speech_with_gtts(input_text, output_filepath)