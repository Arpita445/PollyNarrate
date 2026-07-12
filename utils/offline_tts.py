import pyttsx3


def generate_offline_audio(text):

    engine = pyttsx3.init()

    engine.setProperty(
        "rate",
        150
    )

    engine.setProperty(
        "volume",
        1.0
    )

    audio_file = "offline_audio.wav"

    engine.save_to_file(
        text,
        audio_file
    )

    engine.runAndWait()

    return audio_file
    