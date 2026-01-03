import tkinter as tk
import main_diary as md

def re_set(main_frame, side_up):
    
    for widget in main_frame.winfo_children():
        widget.destroy()
        
    plus_button = tk.Button(main_frame, text="+", width=10, height=5, command=lambda:md.diary_main(main_frame, side_up))
    plus_button.place(relx=0.5, rely=0.5, anchor="center")
