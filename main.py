import tkinter as tk

root = tk.Tk()
root.title("Diary")
root.geometry("800x600")

#사이드바 형성
side_frame = tk.Frame(root, width=200, bg="lightgray")
side_frame.pack(side="left")

#메인바 형성
main_frame = tk.Frame(root, width=600, bg="white")
side_frame.pack(side="left")



root.mainloop()
