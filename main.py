import genanki

# List of Linux directories and their descriptions
from WordsCollector import strWordsCollector
from srtWordsCollector import read_srt_file
from translator import Translator
from voice import record_voice

linux_dirs = [
    ('/', 'Root directory, starting point of the filesystem hierarchy.'),
    ('/bin', 'Contains essential system command executables.'),
    ('/sbin', 'Contains essential system administration command executables.'),
    ('/boot', 'Contains files needed to start the boot process.'),
    ('/etc', "Contains system-wide configuration files and scripts."),
    ('/dev', 'Contains device files representing hardware devices.'),
    ('/home', 'Contains personal directories for each user.'),
    ('/lib', 'Contains shared libraries and kernel modules.'),
    ('/opt', 'Optional directory for storing third-party software.'),
    ('/proc', 'Virtual filesystem providing an interface to kernel internal data structures.'),
    ('/sys', 'Virtual filesystem providing an interface to kernel internal data structures for devices, drivers, and other components.'),
    ('/tmp', 'Temporary directory for storing files deleted after a system reboot.'),
    ('/usr', 'Contains user-related files, shared libraries, header files, documentation, and non-essential software binaries.'),
    ('/var', 'Contains variable data files, such as logs, databases, and mail spools.'),
]

# Define Anki note model
model_id = 160739231
model = genanki.Model(
    model_id,
    'Simple Model',
    fields=[
        {'name': 'Question'},
        {'name': 'Answer'},
        {'name': 'MyMedia'},
    ],
    templates=[
        {
            'name': 'Card 1',
            'qfmt': '{{Question}}<br>{{MyMedia}}',  # AND THIS
            'afmt': '{{FrontSide}}<hr id="answer">{{Answer}}',
        }
    ])

# Generate Anki cards and add them to a deck
deck_id = 2059400111
deck = genanki.Deck(deck_id, 'Angielski_automation')
my_package = genanki.Package(deck)
# my_package.media_files = ['welcome.mp3']

srt_file_path = r'C:\Users\Administrator\Downloads\The.srt'
subtitles = read_srt_file(srt_file_path)
collector = strWordsCollector(subtitles)
new_words = collector.get_words()

print(new_words)
print(len(new_words.split(' ')))

# translator = Translator()
# word = 'oath'
# translated_word = translator.translate('oath')
# record_voice(word)
#
# my_package.media_files = [f'audio/{word}.mp3']
# note = genanki.Note(model=model, fields=[word, translated_word, fr'[sound:{word}.mp3]'])
# deck.add_note(note)



# translated_word = local_translator.translate(new_words.split()[0])

# print(translated_word)

# print(len(top1000))
# print(top1000)
# for dir_name, description in linux_dirs:
#     note = genanki.Note(model=model, fields=[dir_name, description, '[sound:welcome.mp3]'])
#     deck.add_note(note)

# Save the deck to an Anki package (*.apkg) file


# my_package.write_to_file('linux_filesystem3.apkg')