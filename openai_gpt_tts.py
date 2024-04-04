from openai import OpenAI

client = OpenAI()

response = client.audio.speech.create(
    model="tts-1",
    voice="alloy",
    input="If you can hear me, this is working",
)

response.stream_to_file("Outputs/openai_gpt_tts_output.mp3")
