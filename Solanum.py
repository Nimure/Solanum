# import module
from tkinter import *

# create object
root = Tk()

# Adjust size
root.geometry("600x600")

# setup window
root.title("Choose")

# Change the Label Text
def show():
    label.config( text = clicked.get() )

# Dropdoqn menu options
options = [
    "Explain",
    "Identify",
    "Me",
    "Quantum Moon",
    "You",
    "Eye of the Universe"
]

options2 = [
    "Explain",
    "Identify",
    "Me",
    "Quantum Moon",
    "You",
    "Eye of the Universe"
]

# datatype of menu test
clicked = StringVar()
clicked2 = StringVar()

#Initial menu text
clicked.set( "Explain" )
clicked2.set( "Identify" )

#Create Dropdown Menu
popupmenu = OptionMenu( root , clicked, *options )
popupmenu.grid(row=3, column=1)
popupmenu2 = OptionMenu( root , clicked2, *options2 )
popupmenu2.grid(row=3, column=2)

# create Label
label = Label( root , text = " " )

#Execute tkinter
root.mainloop()

# setup window
root.title("Choose")





