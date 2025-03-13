from tkinter import *
from tkinter import ttk

# Create window, give size and a title
root = Tk()
root.title("Flashcard App")
root.geometry("900x500")

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
word_dict = {
    'bed': 'το κρεβάτι',
    'sofa': 'ο καναπές',
    'street': 'ο δρόμος',
    'park': 'το πάρκο',
    'garden': 'ο κήοπος',
    'bathroom': 'το μπάνιο',
    'kitchen': 'η κουζίνα',
    'dinig room': 'η τραπεζαρία',
    'room': 'το δωμάτιο',
    'office': 'το γραφείο'
}




# State variable
idx = 0
word = StringVar(value=test_words[0])
word2 = test_words[0]

# Create and grid outer frame for everything to go into
mainFrame = ttk.Frame(root, padding=(5, 5, 12, 0))
mainFrame.grid(column=0, row=0, sticky=(N,W,E,S))
root.grid_columnconfigure(0, weight=1)
root.grid_rowconfigure(0, weight=1)


# Methods to make the flashcard app work
def next_word(event=None):    # Next method
    global idx
    idx = (idx + 1) % len(test_words)
    word.set(test_words[idx])

def prev_word(event=None):    # Previous method
    global idx
    if(idx - 1 >= 0):
        idx = idx - 1
    else:
        idx = len(test_words) - 1
    word.set(test_words[idx])


# Create widgets for the page
flashcard = ttk.Label(mainFrame, textvariable=word)


next_button = ttk.Button(mainFrame, text="Next Word", padding=(20, 10))    # NEXT BUTTON
next_button.bind('<ButtonPress-1>', next_word)

prev_button = ttk.Button(mainFrame, text="Previous Word", padding=(20, 10))    # PREVIOUS BUTTON
prev_button.bind('<ButtonPress-1>', prev_word)

translate_button = ttk.Button(mainFrame, text="Translate Word", padding=(20, 10))    # TRANSLATE BUTTON

# Grid all the widgets
flashcard.grid(column=0, row=0, sticky=(N,W,E,S))
prev_button.grid(column=0, row=1, sticky=(N,W,E,S))
translate_button.grid(column=1, row=1, sticky=(N,W,E,S))
next_button.grid(column=2, row=1, sticky=(N,W,E,S))




root.mainloop()
