from gtts import gTTS
mytext = 'Welcome to geeksforgeeks!'
language = 'en'
myobj = gTTS(text=mytext, lang=language, slow=False)

# Saving the converted audio in a mp3 file named
# welcome
myobj.save("welcome.mp3")
