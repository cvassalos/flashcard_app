# from tkinter import *
# from tkinter import ttk

# # Calculate feet to meters
# def calculate(*args):
#     try: 
#         value = float(feet.get())
#         meters.set(int(0.3048 * value * 10000.0 + 0.5)/10000.0)
#     except ValueError:
#         pass

# # Set up main application window
# root = Tk()
# root.title("Feet to Meters")

# #Create Content Frame
# mainframe = ttk.Frame(root, padding="3 3 12 12")
# mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
# root.columnconfigure(0, weight=1)
# root.rowconfigure(0, weight=1)

# # Create Entry Widget
# feet = StringVar()
# feet_entry = ttk.Entry(mainframe, width=7, textvariable=feet)
# feet_entry.grid(column=2, row=1, sticky=(W, E))

# #Create Additional Widgets
# meters = StringVar()
# ttk.Label(mainframe, textvariable=meters).grid(column=2, row=2, sticky=(W, E))

# ttk.Button(mainframe, text="Calculcate", command=calculate).grid(column=3, row=3, sticky=W)

# ttk.Label(mainframe, text="feet").grid(column=3, row=1, sticky=W)
# ttk.Label(mainframe, text="is equivalent to").grid(column=1, row=2, sticky=E)
# ttk.Label(mainframe, text="meters").grid(column=3, row=2, sticky=W)

# # Gives each grid item padding
# # Starts cursor in the enter feet area
# # Hitting "Return" calculates
# for child in mainframe.winfo_children():
#     child.grid_configure(padx=5, pady=5)
# feet_entry.focus()
# root.bind("<Return>", calculate)

# root.mainloop()

from tkinter import *
from tkinter import ttk

class FeetToMeters:

    def __init__(self, root):
        root.title("Feet to Meters")

        mainframe = ttk.Frame(root, padding="3 3 12 12", relief="solid", borderwidth=1)
        mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
        root.columnconfigure(0, weight=1)
        root.rowconfigure(0, weight=1)

        self.feet = StringVar()
        self.meters = StringVar()
        self.meters.set("0.0")  # Default value for debugging

        feet_entry = ttk.Entry(mainframe, width=7, textvariable=self.feet)
        feet_entry.grid(column=2, row=1, sticky=(W, E))

        ttk.Label(mainframe, textvariable=self.meters).grid(column=2, row=2, sticky=(W, E))
        ttk.Button(mainframe, text="Calculate", command=self.calculate).grid(column=3, row=3, sticky=W)

        ttk.Label(mainframe, text="feet").grid(column=3, row=1, sticky=W)
        ttk.Label(mainframe, text="is equivalent to").grid(column=1, row=2, sticky=E)
        ttk.Label(mainframe, text="meters").grid(column=3, row=2, sticky=W)

        for child in mainframe.winfo_children():
            child.grid_configure(padx=5, pady=5)

        feet_entry.focus()
        root.bind("<Return>", self.calculate)

    def calculate(self, *args):
        try:
            value = float(self.feet.get())
            self.meters.set(int(0.3048 * value * 10000.0 + 0.5)/10000.0)
            print(f"Feet: {value}, Meters: {self.meters.get()}")  # Debugging output
        except ValueError:
            self.meters.set("Invalid input")

root = Tk()
FeetToMeters(root)
root.mainloop()
