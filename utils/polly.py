import boto3
import streamlit as st
import uuid


polly_client = boto3.client(
    "polly",
    region_name=st.secrets["AWS_REGION"],
    aws_access_key_id=st.secrets["AWS_ACCESS_KEY"],
    aws_secret_access_key=st.secrets["AWS_SECRET_KEY"]
)


def text_to_speech(text, voice_id):

    response = polly_client.synthesize_speech(
        Text=text,
        OutputFormat="mp3",
        VoiceId=voice_id,
        Engine="standard"
    )


    audio_file = f"audio_{uuid.uuid4()}.mp3"


    with open(audio_file, "wb") as f:
        f.write(
            response["AudioStream"].read()
        )


    return audio_file
    