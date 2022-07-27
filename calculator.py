from tkinter import *
root = Tk()

def click(event):
    global scvalue

    if screen.get() == "Error":
        scvalue.set("")
        screen.update()

    text = event.widget.cget("text")

    #If = is chosen
    if text == "=":
        if scvalue.get().isdigit():
            value = int(scvalue.get())
        else:
            try:
                value = eval(screen.get())
            except Exception as e:
                value = "Error"
                print(e)
        
        scvalue.set(value)
        screen.update()
    
    #If C-Clear is clicked
    elif text == "C":
        scvalue.set("")
        screen.update()
    
    else:
        scvalue.set(scvalue.get() + text)
        screen.update()

#Main    
root.geometry("345x640") #Set size of canvas
root.title("Calculator") #Title of canvas
root.configure(background="black")

scvalue =StringVar() #Variable scvalue is set to be of type string
scvalue.set("") #scvalue is initialized as 0

#Main display for the I/O
screen = Entry(root, textvar = scvalue, font="Calibri 36",justify=RIGHT, bg="black", fg="white", relief=FLAT ) #An entry is taken on the canvas
screen.pack(side=TOP, fill=X, ipady=20, pady=10, padx=10) #ipady= Internal padding

#Buttons on the calculator
buttons = [[" ", "C", "%", "/"],
        ["7", "8", "9", "*"],
        ["4", "5", "6", "-"],
        ["1", "2", "3", "+"],
        ["00", "0", ".", "="]]
#Creating the buttons and packing them onto the calculator
for row in buttons:
    f = Frame(root, bg="black", borderwidth=0)
    f.pack(side=TOP, fill=X, padx=20)
    for btn in row:
        b = Button(f, text=btn, font="Calibri 27", relief=FLAT, width=3,
        height=1, pady=15, bg="black", fg="white", activebackground="black", activeforeground="white")
        b.pack(side=LEFT)
        b.bind("<Button>", click)
root.mainloop()