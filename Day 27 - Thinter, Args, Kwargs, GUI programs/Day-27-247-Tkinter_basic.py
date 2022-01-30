import tkinter

# from tkinter import * <- removes all of the extra words of tkinter.

window = tkinter.Tk()  # Brings the class
window.title('My First GUI Program')  # changes the title
window.minsize(width=1280, height=720)  # changes window size

# Label
my_label = tkinter.Label(text="I Am a Label", font=("Arial", 24, "bold"))  # Types on the screen
my_label.pack()  # Brings label to the screen

my_label["text"] = "New Text"  # different method of changing text
my_label.config(text="New Text")  # different method of changing text


# Button function
def button_clicked():
    print("I got clicked")
    new_text = input.get()
    my_label.config(text=new_text)


button = tkinter.Button(text="click me", command=button_clicked)
button.pack()

# Entry text box

input = tkinter.Entry(width=30)
input.pack()

window.mainloop()
