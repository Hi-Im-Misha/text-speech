import subprocess

input_file = r"..\notes\output_audio.mp3"
output_file = r"..\notes\changed_audio.mp3"

def change_audio_speed(speed_factor):

    cmd = f'ffmpeg -i "{input_file}" -filter:a "atempo={speed_factor}" -vn "{output_file}"'
    subprocess.run(cmd, shell=True)

    print("The audio has been changed and saved!")