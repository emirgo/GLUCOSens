"""
    Author: Emirhan Gocturk (460385)
    Description: GLUCOSens desktop client
    Date: 11 October 2021
"""
  
import tkinter as tk
import tkinter.ttk as ttk
import serial.tools.list_ports
import matplotlib


#to be used on our canvas
HEIGHT = 400
WIDTH = 400

# --- functions ---
def serial_ports():    
    return serial.tools.list_ports.comports()

def on_select(event=None):

    # get selection from event    
    print("event.widget:", event.widget.get())

    # or get selection directly from combobox
    print("comboboxes: ", cb.get())

def single_Sensor():    
    clicked_new = int(clicked)
# --- functions ---



# --- main ---
root = tk.Tk() #here we create our tkinter window
root.title("Sensor Interface")

#we use canvas as a placeholder, to get our initial screen size (we have defined HEIGHT and WIDTH)
canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH)
canvas.pack()

#we use frames to organize all the widgets in the screen

# --- frame 1 ---
frame1 = tk.Frame(root)
frame1.place(relx=0, rely=0.05, relheight=0.1, relwidth=1, anchor='nw') #we use relheight and relwidth to fill whatever the parent is - in this case- root

label0 = tk.Label(frame1, text="COM ")
label0.config(font=("TkDefaultFont", 12))
label0.place(relx = 0, rely=0.3, relwidth=0.3, relheight=0.5)


cb = ttk.Combobox(frame1, values=serial_ports())
cb.place(relx=0.5, rely=0.5, anchor='center')
# assign function to combobox
cb.bind('<<ComboboxSelected>>', on_select)
# --- frame 1 ---



root.mainloop() #here we run our app
# --- main ---