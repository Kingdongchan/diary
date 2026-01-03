import tkinter as tk

#텍스트 클래스 생성
class text:
    def __init__(self, main, width, height, row, column, sticky):
        self.main = main
        self.width = width
        self.height = height
        self.row = row
        self.column = column
        self.stikcy = sticky
        
    def txt_maker(self):
        txt = tk.Text(self.main, width=self.width, height=self.height)
        txt.grid(row=self.row, column=self.column, sticky=self.stikcy)
        