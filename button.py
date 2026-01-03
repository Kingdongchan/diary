import tkinter as tk

#버튼 클래스 생성
class button:
    def __init__(self, main, text, row, column, sticky, command=None):
        self.main = main
        self.text = text
        self.row = row
        self.column = column
        self.command = command
        self.stikcy = sticky
        
    def bnt_maker(self):
        bnt = tk.Button(self.main, text=self.text, command=self.command)
        bnt.grid(row=self.row, column=self.column, sticky=self.stikcy)
        