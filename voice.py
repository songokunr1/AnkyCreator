from gtts import gTTS


def record_voice(text, language='en', file_name=None):
    myobj = gTTS(text=text, lang=language, slow=False)
    if not file_name:
        file_name = text
    myobj.save(f"audio/{file_name}.mp3")


record_voice('may i have')