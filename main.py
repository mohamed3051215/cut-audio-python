from pydub import AudioSegment
import time


def ask_for_data():
    try:
        audio_path = input("Enter the path of the audio file:  ")
        new_audio_path = input("Enter the path of the new audio file:  ")
        start_minutes = int(input("Enter the start time in minutes:  "))
        start_seconds = int(input("Enter the start time in seconds:  "))
        end_minutes = int(input("Enter the end time in minutes:  "))
        end_seconds = int(input("Enter the end time in seconds:  "))

    except ValueError:
        print("Invalid input. Please try again.")
        ask_for_data()

    return audio_path, new_audio_path, start_minutes, start_seconds, end_minutes, end_seconds


def convert_to_milliseconds(start_minutes, start_seconds, end_minutes, end_seconds):
    return ((start_minutes * 60) + start_seconds) * 1000, ((end_minutes * 60) + end_seconds)*1000


def process(audio_path, new_audio_path, start_milliseconds, end_milliseconds):

    audio_file = AudioSegment.from_file(audio_path, format='mp3')
    audio_file = audio_file[start_milliseconds:end_milliseconds]
    audio_file.export(new_audio_path, format="wav")
    print("Audio file created successfully.")


if __name__ == "__main__":
    audio_path, new_audio_path, start_minutes, start_seconds, end_minutes, end_seconds = ask_for_data()
    print(audio_path, new_audio_path, start_minutes,
          start_seconds, end_minutes, end_seconds)
    start_milliseconds, end_milliseconds = convert_to_milliseconds(
        start_minutes, start_seconds, end_minutes, end_seconds)
    process(audio_path, new_audio_path, start_milliseconds, end_milliseconds)
    time.sleep(2)
