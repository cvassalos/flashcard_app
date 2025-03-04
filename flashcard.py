from tkinter import *
from tkinter import ttk

# Create window, give size and a title
root = Tk()
root.title("Flashcard App")
root.geometry("900x500")

# Hard-coded list of words
words = {
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
# def nextCard(*args):


# State variable
word = StringVar(value=words)
word1 = word[0]

# Create and grid outer frame for everything to go into
mainFrame = ttk.Frame(root, padding=(5, 5, 12, 0))
mainFrame.grid(column=0, row=0, sticky=(N,W,E,S))
root.grid_columnconfigure(0, weight=1)
root.grid_rowconfigure(0, weight=1)

# Create widgets for the page
flashcard = ttk.Label(mainFrame, text=word1)

# Grid all the widgets
flashcard.grid(column=0, row=0, sticky=(N,W,E,S))


root.mainloop()
