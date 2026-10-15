import tkinter as tk #It imports Tkinter and gives it another name of tk

def on_click(event): #This defines a function called on_click 
    text= event.widget.cget("text") #it will diplay the text on the widget
    if text == "=": #checks if the text is equal to = sign
        try:
            result = eval(str(entry_var.get())) #evaluates the expression which is enetered in the entry_var variable
            entry_var.set(result) #this will display the result
        except Exception as e: #this will be shown if the caluculation causes an error
            entry_var.set("error") #shows error when the expression is not valid
    elif text == "C": #checks weather the text is equal to C
        entry_var.set("") #it will clear the entry_var
    else:
        entry_var.set(entry_var.get()+text) #adds the buttons text to the entry_var

root=tk.Tk() #this will create the main window
root.title("CALUCULATOR") #sets the title as CALUCULATOR
root.geometry("500x500") #sets the windows dimensions to 500x500
root.config(bg='light blue') #sets the background clour to light blue

entry_var=tk.StringVar() #this will create a variable and sotes the value given to it 
entry=tk.Entry(root,textvar=entry_var,font="Arial 20 bold") #creates the caluculator inside the window and assigns the font
entry.pack(fill=tk.BOTH,ipadx=8,pady=10,padx=10) #places the caluculator inside the mainwindow

buttons=[ #creates a list inside a list called buttons
    ['7','8','9','/'], #numbers 7,8,9,/
    ['4','5','6','*'], #numbers 4,5,6,*
    ['1','2','3','-'], #numbers 1,2,3,-
    ['C','0','=','+'], #clear=C, number 0 ,=,+
] 

frame=tk.Frame(root) #creates a frame to have the caluculator buttons
frame.config(bg='navy blue') #gives the frame a background colour navy blue
frame.pack() #places the frame inside the main wondow

for row in buttons: #will run a for loop through each row inside the list buttons
    button_row=tk.Frame(frame) #creates a seperate frame for that specific row
    button_row.pack() #places the button_row inside the main window
    for btn_text in row: # will run a for loop through each button inside the each row 
        btn=tk.Button(button_row, text=btn_text, font='Arial 15 bold', height=2, width=5) #this iwll create a new caluculator button
        btn.pack(side=tk.LEFT, padx=5, pady=5) #will place the new button inside the main window toward the left side
        btn.bind('<Button-1>',on_click) #when the left mouse is clicked the function on_click is called

root.mainloop() #this iwll keep the main window running until the loop is closed