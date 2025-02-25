from gtts import gTTS
import os
from counting_number_text.countword import countwords
from changing_speed_audio.change_audio_speed import change_audio_speed

text_file = r'.\text.txt'
output_file = r'notes\output_audio.mp3'
language = 'en' # specify the language

try:
    countwords() 
    with open(text_file, 'r', encoding='utf-8') as file:
        text = file.read().strip()

    if not text:
        print("Error: The file is empty. Add the text and try again")
    else:
        tts = gTTS(text, lang=language)
        tts.save(output_file)
        print(f'Ready! The audio file is saved as: {output_file}')

        os.system(f'start {output_file}')


        input_speed = input("Change the audio speed? (y/n): ").strip().lower()
        if input_speed == 'y':
            speed_factor = input("Enter the speed factor (for example, 1.5 for acceleration, 0.8 for deceleration): ").strip()

            try:
                speed_factor = float(speed_factor)
                change_audio_speed(speed_factor)
                print(f"Audio file changed and saved as: changed_audio.mp3")
            except ValueError:
                print("Error: Enter the correct number for speed!")
        else:
            os.system(f'start {output_file}')


except FileNotFoundError:
    print(f"Error: File {text_file} not found")
except Exception as e:
    print(f"An error has occurred: {e}")
