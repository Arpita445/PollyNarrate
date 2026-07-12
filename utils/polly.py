import boto3
import uuid


polly_client = boto3.client(
    "polly",
    region_name="ap-south-1"
)


def text_to_speech(text, voice_id):

    max_length = 2500

    chunks = [
        text[i:i + max_length]
        for i in range(0, len(text), max_length)
    ]

    audio_files = []

    for chunk in chunks:

        response = polly_client.synthesize_speech(
            Text=chunk,
            OutputFormat="mp3",
            VoiceId=voice_id,
            Engine="standard"
        )

        audio_file = f"audio_{uuid.uuid4()}.mp3"

        with open(audio_file, "wb") as file:
            file.write(
                response["AudioStream"].read()
            )

        audio_files.append(audio_file)


    return audio_files[0]
    