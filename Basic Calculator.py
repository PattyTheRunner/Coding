from tkinter import*    # Imports tkinter

def set(number):
    calc_entry.insert(END, number)     # Inserts the number at the end.

def clear():
    calc_entry.delete(0, END)     # Deletes everything in the entry widget.

def calculate():
    expression = calc_entry.get()
    try:
        ans = eval(expression)    # Tries to calculate it.
    except:
        ans = "Error"    # Displays error if unable to.
    clear()     # Deletes everything in the entry widget.
    set(ans)     # Displays the answer.

window = Tk()     # Creates a tkinter window.
window.title('Calculator')       # Creates a title: Calculator
window.minsize(width=300, height=300)      # Makes the size of the window.
window.config(padx=20, pady=20)       # Gives it some padding.

calc_entry = Entry(window, width=30)      # Creates an entry window.
calc_entry.grid(row=0, column=0, columnspan=4, pady=5)      # Makes a grid for the buttons.

button1 = Button(window, text='1', width=3, height=4,
                 command=lambda:set('1'))
button1.grid(row=3, column=0)

button2 = Button(window, text='2', width=3, height=4,
                 command=lambda:set('2'))
button2.grid(row=3, column=1)

button3 = Button(window, text='3', width=3, height=4,
                 command=lambda:set('3'))
button3.grid(row=3, column=2)

button4 = Button(window, text='4', width=3, height=4,
                 command=lambda:set('4'))
button4.grid(row=2, column=0)

button5 = Button(window, text='5', width=3, height=4,
                 command=lambda:set('5'))
button5.grid(row=2, column=1)

button6 = Button(window, text='6', width=3, height=4,
                 command=lambda:set('6'))
button6.grid(row=2, column=2)

button7 = Button(window, text='7', width=3, height=4,
                 command=lambda:set('7'))
button7.grid(row=1, column=0)

button8 = Button(window, text='8', width=3, height=4,
                 command=lambda:set('8'))
button8.grid(row=1, column=1)

button9 = Button(window, text='9', width=3, height=4,
                 command=lambda:set('9'))
button9.grid(row=1, column=2)

button0 = Button(window, text='0', width=3, height=4,
                 command=lambda:set('0'))
button0.grid(row=4, column=0)

buttonadd = Button(window, text='+', width=3, height=4,
                 command=lambda:set('+'))
buttonadd.grid(row=4, column=3)

buttonsub = Button(window, text='-', width=3, height=4,
                 command=lambda:set('-'))
buttonsub.grid(row=3, column=3)

buttonmul = Button(window, text='*', width=3, height=4,
                 command=lambda:set('*'))
buttonmul.grid(row=2, column=3)

buttondiv = Button(window, text='/', width=3, height=4,
                 command=lambda:set('/'))
buttondiv.grid(row=1, column=3)

buttonC = Button(window, text='C', width=3, height=4,
                 command=clear)
buttonC.grid(row=4, column=2)

buttondec = Button(window, text='.', width=3, height=4,
                 command=lambda:set('.'))
buttondec.grid(row=4,      column=1)


buttonequal = Button(window, text='=', width=11, height=4,
                 command=calculate)
buttonequal.grid(row = 6, column = 1, columnspan = 2)                        # Buttons

window.mainloop()