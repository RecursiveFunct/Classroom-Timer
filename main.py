'''
TODO:
    1. Reformat the time 
    2. Allow user to enter a time for timer
    3. Create a notifciation to user when timer time is elapsed
    4. Allow timer app to be paused and resumed
'''

from tkinter import *
from tkinter import ttk
import time 

def update_labels():
    elp_time = time.perf_counter() - str_time
    timer_label.config(text=f'Seconds: {elp_time // 1:.0f}')
    clock_label.config(text=time.strftime('%H:%M:%S'))
    root.after(50, update_labels) # test that this delay or debounce here does not effect time accuracy. 

def clear_timer():
    global str_time
    str_time = time.perf_counter() # start time reset

def set_time():
    # Creating new window for user to enter time 
    set_time_wind = Toplevel(root)
    set_time_wind.title("Enter Time")
    set_time_wind.geometry("100x100")

    ttk.Label(set_time_wind, text="testing new window").pack(pady=15)
    ttk.Button(set_time_wind, text='\u2191').pack(pady=5)
    ttk.Button(set_time_wind, text="Finish", command=set_time_wind.destroy).pack(pady=15)

# root init
root = Tk() 
root.title("Classroom Clock App")
root.geometry("300x300")
str_time = time.perf_counter() # Begin time tracking

# notebook setup
notebook = ttk.Notebook(root)
notebook.pack(padx = 10, pady = 10, expand=True, fill='both')

tab_clock = ttk.Frame(notebook)
tab_timer = ttk.Frame(notebook)
tab_clock.pack(fill="both", expand=True)
tab_timer.pack(fill="both", expand=True)

notebook.add(tab_clock, text="Clock")
notebook.add(tab_timer, text="Timer")

# clock tabs setup
ttk.Label(tab_clock, text="Time").pack(pady=20)
clock_label = ttk.Label(tab_clock, text="00:00:00")
clock_label.pack(expand=True)

# timer tabs setup
ttk.Label(tab_timer, text="Timer").pack(pady=20)
timer_label = ttk.Label(tab_timer, text="00:00:00")
timer_label.pack(expand=True)

ttk.Button(tab_timer, text="Enter Time", command=set_time).pack(pady=10)
ttk.Button(tab_timer, text="Clear Timer ❌", command=clear_timer).pack(pady=15)
ttk.Button(root, text="EXIT App", command=root.destroy).pack(pady=10)

# update and loop 
update_labels()
root.mainloop()
