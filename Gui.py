
import tkinter as tk
window = tk.Tk()
window.title("SOE_Generator")
window.geometry('340x250')
a = tk.Label(window, text= "Release Title").grid(row=0, column=0)
b = tk.Label(window, text= "Date").grid(row=1, column=0)
a1 = tk.Entry(window).grid(row=0,column=2)
b1 = tk.Entry(window).grid(row=1, column=2)
cb1 = tk.Checkbutton(window, text="DBA").grid(row=4, column=1)
cb2 = tk.Checkbutton(window,text="BDA").grid(row=5, column=1)
bt1 = tk.Button(window, text="Submit").grid(row=6, column=1)
