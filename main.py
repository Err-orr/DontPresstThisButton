import tkinter
#This is the module used to create GUIs.

window = tkinter.Tk()
#This creates a new tkinter window.

button = tkinter.Button(window, text="Do not press the button", width=40)
#Now this creates a button for the window.

button.pack(padx=10, pady=10)
#Then this button gets placed inside of the window using x and y padding.

clickCount = 0
#This counts how many times the button has been clicked

#Now we give the button some commands.
def onClick(event):
  #Global allows the function to use the clickCount that was created outside of the function
  global clickCount
  clickCount = clickCount + 1
  #If the button is clicked for the first time,
  if clickCount == 1:
    button.configure(text="Seriously? Do. Not. Press. It!")
    #The text gets updated.
  #If the button gets clicked the second time,
  elif clickCount == 2:
    button.configure(text="GAH! Next time, no more button -_-")
    #The text gets updated again.
  #If the button gets clicked the third time,
  else:
    button.pack_forget()
    #The button gets deleted.

button.bind("<ButtonRelease-1>", onClick)
#We link our function to the button.

window.mainloop()
#Makes the whole code run.