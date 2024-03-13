from tkinter import *


def miles_to_km():
    miles = float(entry1_miles.get())
    km = miles * 1.60934
    kilometer_result_label.config(text=f"{km}")


screen = Tk()
screen.title("Mile to Km Converter")
screen.minsize(285, 150)

button = Button(text="Calculate", command=miles_to_km)
button.grid(column=4, row=3)

label1 = Label(text="Miles")
label1.grid(column=6, row=0)

label2 = Label(text="is equal to")
label2.grid(column=0, row=2)

label3 = Label(text="Km")
label3.grid(column=6, row=2)

entry1_miles = Entry(width=10)
entry1_miles.grid(column=4, row=0)

kilometer_result_label = Label(text="0")
kilometer_result_label.grid(column=4, row=2)

screen.mainloop()
