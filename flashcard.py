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

# function to iterate through list of words



# State variable
idx = 1
test_word = StringVar(value="TESING")
test_word2 = test_words[idx]
word = StringVar(value=test_word2)
# word.trace_add('w', callback)

# Create and grid outer frame for everything to go into
mainFrame = ttk.Frame(root, padding=(5, 5, 12, 0))
mainFrame.grid(column=0, row=0, sticky=(N,W,E,S))
root.grid_columnconfigure(0, weight=1)
root.grid_rowconfigure(0, weight=1)

# Create widgets for the page
flashcard = ttk.Label(mainFrame, text=test_word2)
next_button = ttk.Button(mainFrame, text="Next Word", padding=(20, 10))

# Grid all the widgets
flashcard.grid(column=0, row=0, sticky=(N,W,E,S))
next_button.grid(column=0, row=1, sticky=(N,W,E,S))


# Methods to make the flashcard app work
def next_word():
    idx += 1
    test_word2 = test_words[idx + 1]

def callback(name, index, mode):
    return var.get()


root.mainloop()
