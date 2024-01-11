from gtts import gTTS
from google.cloud import texttospeech
import os
import boto3
from io import BytesIO

# Aws access key
AWS_ACCESS_KEY =  ""
AWS_SECRET_ACCESS_KEY = ""

# google text to speech credential
ACCOUNT = {}

text_title = "lorensum ipsum ipsum"

client = boto3.client(
    's3',
    aws_access_key_id=AWS_ACCESS_KEY,
    aws_secret_access_key=AWS_SECRET_ACCESS_KEY
)

credentials = service_account.Credentials.from_service_account_info(ACCOUNT)

"""Synthesizes speech from the input string of text."""
clientTextToSpeech = texttospeech.TextToSpeechClient(credentials=credentials)

input_text = texttospeech.SynthesisInput(text=text_title)

voice = texttospeech.VoiceSelectionParams(
    language_code="en-gb",
    name="en-GB-Standard-A",
    ssml_gender=texttospeech.SsmlVoiceGender.FEMALE,
)

audio_config = texttospeech.AudioConfig(
    audio_encoding=texttospeech.AudioEncoding.MP3
)

response = clientTextToSpeech.synthesize_speech(
    input=input_text, voice=voice, audio_config=audio_config
)

client.put_object(Bucket='data_folder', Key=f'title_speech.mp3', Body=response.audio_content,
                                  ContentDisposition='inline', ContentType='audio/mp3')
