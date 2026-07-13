import boto3
import streamlit as st
import uuid


polly_client = boto3.client(
    "polly",
    region_name=st.secrets["AWS_REGION"],
    aws_access_key_id=st.secrets["AWS_ACCESS_KEY"],
    aws_secret_access_key=st.secrets["AWS_SECRET_KEY"]
)


def split_text(text, limit=2500):

    chunks = []

    words = text.split()

    current = ""

    for word in words:

        if len(current) + len(word) < limit:
            current += word + " "

        else:
            chunks.append(current)
            current = word + " "


    if current:
        chunks.append(current)


    return chunks



def text_to_speech(text, voice_id):

    chunks = split_text(text)


    audio_file = f"audio_{uuid.uuid4()}.mp3"


    # Language mapping for voices
    language_map = {

        # Hindi / Indian English
        "Aditi": "hi-IN",
        "Raveena": "en-IN",

        # English
        "Joanna": "en-US",
        "Matthew": "en-US",

        # French
        "Lea": "fr-FR",
        "Mathieu": "fr-FR",

        # Spanish
        "Lucia": "es-ES",
        "Enrique": "es-ES",

        # German
        "Marlene": "de-DE",
        "Hans": "de-DE",

        # Italian
        "Bianca": "it-IT",

        # Japanese
        "Mizuki": "ja-JP"

    }


    language_code = language_map.get(
        voice_id,
        "en-US"
    )


    with open(audio_file, "wb") as final_audio:


        for chunk in chunks:


            response = polly_client.synthesize_speech(

                Text=chunk,

                OutputFormat="mp3",

                VoiceId=voice_id,

                Engine="standard",

                LanguageCode=language_code

            )


            final_audio.write(
                response["AudioStream"].read()
            )


    return audio_file

    