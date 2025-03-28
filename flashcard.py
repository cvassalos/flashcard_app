from tkinter import *
from tkinter import ttk

# Create window, give size and a title
root = Tk()
root.title("Flashcard App")


# Hard-coded list of words
test_words = [
    'apple',
    'banana',
    'capybara',
    'dog',
    'elephant',
    'frog',
    'grapes'
]

word_dict = [
    ('bed', 'το κρεβάτι'),
    ('sofa', 'ο καναπές'),
    ('street', 'ο δρόμος'),
    ('park', 'το πάρκο'),
    ('garden', 'ο κήοπος'),
    ('bathroom', 'το μπάνιο'),
    ('kitchen', 'η κουζίνα'),
    ('dinig room', 'η τραπεζαρία'),
    ('room', 'το δωμάτιο'),
    ('office', 'το γραφείο')
]
# Dictionary Data Structure
# word_dict = {
#     'bed': 'το κρεβάτι',
#     'sofa': 'ο καναπές',
#     'street': 'ο δρόμος',
#     'park': 'το πάρκο',
#     'garden': 'ο κήοπος',
#     'bathroom': 'το μπάνιο',
#     'kitchen': 'η κουζίνα',
#     'dinig room': 'η τραπεζαρία',
#     'room': 'το δωμάτιο',
#     'office': 'το γραφείο'
# }


##### Gives window it's geometry and opens it in middle of the screen

# Width and height sizes
window_width = 900
window_height = 500

# get the screen dimensions
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

# find the center point
center_x = int(screen_width / 2 - window_width / 2)
center_y = int(screen_height / 2 - window_height / 2)

# set the position of the window to the center of the screen
root.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')

# Change app icon ----------------------------- NOT WORKING FOR SOME REASON
root.iconbitmap('./images/flashcard.ico')


# State variable --------------------- GOING TO SWITCH TO USING DICTIOINARY GETTING RID OF THIS NONESENSE
idx = 0
english_idx = 0
translated_idx = 0
# english_words = word_dict.keys()
# translated_words = word_dict.values()


word = StringVar(value=word_dict[english_idx][translated_idx])
# word = StringVar(value=test_words[0])

# Configuring the grid
root.grid_columnconfigure(0, weight=1)
root.grid_columnconfigure(1, weight=1)
root.grid_columnconfigure(1, weight=1)

# Create and grid outer frame for everything to go into
mainFrame = ttk.Frame(root, padding=(30, 30))
mainFrame.grid(column=0, row=0, sticky="nsew")
root.grid_columnconfigure(0, weight=1)
root.grid_rowconfigure(0, weight=1)

print(mainFrame.winfo_width())
print(mainFrame.winfo_height())


# Methods to make the flashcard app work
def next_word(event=None):    # Next method
    global english_idx
    english_idx = (english_idx + 1) % len(word_dict)
    word.set(word_dict[english_idx][translated_idx])

def prev_word(event=None):    # Previous method
    global english_idx
    if(english_idx - 1 >= 0):
        english_idx = english_idx - 1
    else:
        english_idx = len(word_dict) - 1
    word.set(word_dict[english_idx][translated_idx])

def translate_word(event=None):
    global translated_idx
    # if translated_idx == 1:
    #     translated_idx = 0
    # else:
    #     translated_idx = 1
    translated_idx = 1 if translated_idx == 0 else 0
    word.set(word_dict[english_idx][translated_idx])

# Create widgets for the page
flashcard = ttk.Label(mainFrame, textvariable=word, style='Flashcard.Label')


next_button = ttk.Button(mainFrame, text="Next Word", padding=(20, 10))    # NEXT BUTTON
next_button.bind('<ButtonPress-1>', next_word)

prev_button = ttk.Button(mainFrame, text="Previous Word", padding=(20, 10))    # PREVIOUS BUTTON
prev_button.bind('<ButtonPress-1>', prev_word)

translate_button = ttk.Button(mainFrame, text="Translate Word", padding=(20, 10))    # TRANSLATE BUTTON
translate_button.bind('<ButtonPress-1>', translate_word)

# Grid all the widgets
flashcard.grid(column=0, row=0, columnspan=3, sticky="nsew", pady=20)
prev_button.grid(column=0, row=1, sticky="ew", padx=5, pady=10)
translate_button.grid(column=1, row=1, sticky="ew", padx=5, pady=10)
next_button.grid(column=2, row=1, sticky="ew", padx=5, pady=10)

root.grid_rowconfigure(1, weight=1)

# Styling the TKinter App




root.mainloop()
