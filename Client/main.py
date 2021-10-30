"""
    Author: Emirhan Gocturk (460385)
    Description: GLUCOSens desktop client
    Date: 11 October 2021
"""
  
import tkinter as tk
import tkinter.ttk as ttk
import serial
import serial.tools.list_ports
import matplotlib
from serial.tools.list_ports_windows import comports
import serial
import time
import csv
import matplotlib
matplotlib.use("tkAgg")
import matplotlib.pyplot as plt
import numpy as np


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

def realTimePlotting():
    print("Conencting to: ", cb.get())
    print("...")
    comPort = cb.get().split(" ", 1)
    print(comPort[0])
    ser = serial.Serial(comPort[0])
    ser.flushInput()

    plot_window = 20
    y_var = np.array(np.zeros([plot_window]))

    plt.ion()
    fig, ax = plt.subplots()
    line, = ax.plot(y_var)

    while True:
        try:
            ser_bytes = ser.readline()
            try:
                decoded_bytes = float(ser_bytes[0:len(ser_bytes)-2].decode("utf-8"))
                print(decoded_bytes)
            except:
                continue
            with open("test_data.csv","a") as f:
                writer = csv.writer(f,delimiter=",")
                writer.writerow([time.time(),decoded_bytes])
            y_var = np.append(y_var,decoded_bytes)
            y_var = y_var[1:plot_window+1]
            line.set_ydata(y_var)
            ax.relim()
            ax.autoscale_view()
            fig.canvas.draw()
            fig.canvas.flush_events()
        except:
            print("Keyboard Interrupt")
            break

# --- functions ---



# --- main ---
root = tk.Tk() #here we create our tkinter window
root.title("GLUCOSens - Real Time Analyzer Interface")

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

button = tk.Button(root, text="Connect", command = realTimePlotting)
button.place(relx = 0.1, rely = 0.2)
# --- frame 1 ---



root.mainloop() #here we run our app
# --- main ---




"""
# get data through serial
chosenPort = cb.get()
ser = serial.Serial(chosenPort)
ser.flushInput()

while True:
    try:
        serialBytes = ser.readline()
        decodedBytes = float(serialBytes)
        print(decodedBytes)
    except:
        print('Keyboard Interrupt')
        break
"""