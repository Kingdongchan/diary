import tkinter as tk

#라벨 클래스 생성
class label:
    def __init__(self, main, text, row, column):
        self.main = main
        self.text = text
        self.row = row
        self.column = column
        
    def lb_meker(self):
        label = tk.Laberl(self.main, text=self.text)
        label.grid(row=self.row, column=self.column)
    