import tkinter as tk

#버튼 클래스 생성
class button:
    def __init___(self, main, text, width, height, row, column, sticky, command=None):
        self.main = main
        self.text = text
        self.width = width
        self.height = height
        self.row = row
        self.column = column
        self.command = command
        self.stikcy = sticky
        
    def bnt_maker(self):
        bnt = tk.Button(self.main, text=self.text, width=self.width, height=self.height, command=self.command)
        bnt.grid(row=self.row, column=self.column, sticky=self.stikcy)
        