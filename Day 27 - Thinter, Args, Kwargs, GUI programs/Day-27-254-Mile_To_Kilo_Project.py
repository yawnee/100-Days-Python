# Pack - pack the widgets from the top to the bottom, next in the series
# Place - places the widget where specified (x, y)
# Grid - program is imagined as a grid (rows, columns)

from tkinter import *


def convert_miles_to_km():
    new_km_value = float(m_input.get()) * 1.60934
    my_label_final_km.config(text=new_km_value)


window = Tk()
window.title("Mile to Km Converter")
window.minsize(width=300, height=100)

# Label #1: Miles
my_label_Miles = Label(text="Miles", font=("Arial", 10, "normal"))
my_label_Miles.grid(column=3, row=0)
my_label_Miles.config(padx=15, pady=10)

# Label #2: Is equal to
is_equal_label = Label(text="is equal to", font=("Arial", 10, "normal"))
is_equal_label.grid(column=0, row=1)
is_equal_label.config(padx=15, pady=10)

# Label #3: Kilometer
my_label_km = Label(text="km", font=("Arial", 10, "normal"))
my_label_km.grid(column=3, row=1)
my_label_km.config(padx=15, pady=10)

# Entry #1: Miles value
m_default = 0
m_input = Entry(width=10)
print(m_input.get())
m_input.grid(column=1, row=0)

# Label #4: Kilometer
km_final = 0
my_label_final_km = Label(text=km_final, font=("Arial", 10, "normal"))
my_label_final_km.grid(column=1, row=1)
my_label_final_km.config(padx=15, pady=10)

# Button #1: Calculate
button = Button(text="Calculate", command=convert_miles_to_km)
button.grid(column=1, row=2)
button.config(padx=15, pady=10)


window.mainloop()
