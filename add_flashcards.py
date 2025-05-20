import tkinter as tk
from tkinter import *
from tkinter import ttk
from flashcard import *
from tkinter.messagebox import showerror
import tkinter.filedialog as filedialog

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

# CARDS TO ADD ARRAY ------------------------------------------
card_stack = [Flashcard("Port 23", "Telnet"),
              Flashcard("Port 68", "DHCP"),
              Flashcard("Port 161", "SNMP")]
list_variable = tk.Variable(value=([card.return_front() for card in card_stack]))

# FUNCTIONS -----------------------------------------------
def add_card_to_stack():
    if len(flashcard_front_entry.get()) == 0:
        showerror(title = "Entry Error", message = "Please enter text for the front of the flashcard" )
    elif len(flashcard_back_entry.get()) == 0:
        showerror(title = "Entry Error", message = "Please enter text for the back of the flashcard")

    else:
        card_stack.append(Flashcard(flashcard_front_entry.get(), flashcard_back_entry.get()))
        list_variable.set(value=([card.return_front() for card in card_stack]))
        flashcard_front_entry.delete(0, tk.END)
        flashcard_back_entry.delete(0, tk.END)
        flashcard_front_entry.focus()
        for card in card_stack:
            print(f'{card.return_front()} ==> {card.return_back()}')

def save_stack():
    file_types = [("Text files", "*.txt"), ("Python files", "*.py")]
    file_path = filedialog.asksaveasfilename(initialfile="untitile_stack.py", defaultextension=".py", filetypes=file_types, initialdir="./card_stacks")

    if file_path:
        try:
            with open(file_path, "w") as f:
                for card in card_stack:
                    f.write(f"{str(card)}\n")
        except Exception as e:
            showerror("Save error", f"Failed to save file: \n{e}")


# FRAME to put all the widgets into
add_cards_frame = ttk.Frame(root, borderwidth=1)
add_cards_frame.grid(column=0, row=0)

# FRAME to hold Listbox that displays added cards
flashcard_stack_frame = ttk.Frame(root, borderwidth=1)
flashcard_stack_frame.grid(column=1, row=0)

# Front of flashcard LABEL
flashcard_front_label = ttk.Label(add_cards_frame, text="Front of Flashcard")
flashcard_front_label.grid(column=0, row=0, padx=25, pady=25)

# Front of the flashcard ENTRY BOX
flashcard_front_entry = ttk.Entry(add_cards_frame)
flashcard_front_entry.grid(column=1, row=0)
flashcard_front_entry.bind("<Return>", lambda e: add_card_to_stack())
flashcard_front_entry.focus()

# Back of flashcard LABEL
flashcard_back_label = ttk.Label(add_cards_frame, text="Back of Flashcard")
flashcard_back_label.grid(column=0, row=1)

# Back of the flashcard ENTRY BOX
flashcard_back_entry = ttk.Entry(add_cards_frame)
flashcard_back_entry.grid(column=1, row=1)
flashcard_back_entry.bind("<Return>", lambda e: add_card_to_stack())

# BUTTON to add the card to the stack
submit_btn = ttk.Button(add_cards_frame, text="Add Card", command=add_card_to_stack)
submit_btn.grid(column=0, row=2, columnspan=2, padx=25, pady=10)
submit_btn.bind("<Return>", lambda e: add_card_to_stack())

# BUTTON to save current stack
save_btn = ttk.Button(add_cards_frame, text="Save Card Stack", command=save_stack)
save_btn.grid(column=0, row=3, columnspan=2, padx=25, pady=10)

# List of flashcards added to stack
flashcard_stack = Listbox(flashcard_stack_frame, listvariable=list_variable, height=10)
flashcard_stack.grid()

################### MENUBAR at top of window to hold things like open and save
# Create menubar and assign it to the root 
menubar = Menu(root)
root.config(menu=menubar)

# Create a file menu whose container is menubar
file_menu = Menu(menubar)

# Adding item to file menu
file_menu.add_command(
    label="Exit",
    command=root.destroy,
)

# Add file menu to menubar
menubar.add_cascade(
    label="File",
    menu=file_menu,
    underline=0
)



root.mainloop()


"""
    Things to work on:
        - Classes for each type of word
            - eg: noun, verb, adjective, adverb, etc

        - A way to remove cards

        - A way to edit cards

        - A widget that lists all the flashcards that have been added
            - A way to select the item in the list and to edit it if needed
        
        - Save that stack of flashcards to a text file to be used in the study portion of the program
          
        - A way to open already made stacks to add/remove/edit

        - Save file
            - Save lists in another file
            - Use tkinter filedialog
"""
