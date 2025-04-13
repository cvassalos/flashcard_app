from tkinter import *
from tkinter import ttk

# Create window and add title to it
root = Tk()
root.title("Add Flashcards")

# Width and height of window
window_width = 900
window_height = 500

# get screen dimensions
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

# Find the center point
center_x = int(screen_width / 2 - window_width / 2)
center_y = int(screen_height / 2 - window_height / 2)

# Set the position of the window to the center of the screen
root.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')

# FRAME to put all the widgets into
add_cards_frame = ttk.Frame(root, borderwidth=1)
add_cards_frame.grid(column=0, row=0)

# Front of flashcard LABEL
flashcard_front_label = ttk.Label(add_cards_frame, text="Front of Flashcard")
flashcard_front_label.grid(column=0, row=0)

# Front of the flashcard ENTRY BOX
flashcard_front_entry = ttk.Entry(add_cards_frame)
flashcard_front_entry.grid(column=1, row=0)

# Back of flashcard LABEL
flashcard_back_label = ttk.Label(add_cards_frame, text="Back of Flashcard")
flashcard_back_label.grid(column=0, row=1)

# Back of the flashcard ENTRY BOX
flashcard_back = ttk.Entry(add_cards_frame)
flashcard_back.grid(column=1, row=1)

root.mainloop()
