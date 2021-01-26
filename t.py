import speech_recognition
import logging


robot_ear = speech_recognition.Recognizer()

passage = []


def get_yes_no(msg: str):
    move_on = True

    continue_ = input(msg)
    continue_ = continue_.lower().strip()

    if continue_ not in ["y", "yes", ""]:
        move_on = False

    return move_on


move_on = True
while move_on:
    print("Say something: ")
    with speech_recognition.Microphone() as mic:
        audio = robot_ear.listen(mic)

        try:
            your_text: str = robot_ear.recognize_google(audio)
        except speech_recognition.UnknownValueError as e:
            logging.error(f"Please said something.")
            continue
        else:
            strip_text = your_text.strip()
            res = get_yes_no(f"Did you say: '{strip_text}' [Y/n]?")
            if res:
                passage.append(strip_text)

    print("\ntype Enter to continue talking. N to get the text")
    move_on = get_yes_no("Continue to talk [Y/n] ?")

print(
    ", ".join(passage)
)
