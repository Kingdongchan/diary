import tkinter as tk
from tkinter import messagebox 

def side_del (index, save_blank):
    #삭제 할 떄 정말 삭제할 지 이야기 해주는 안내창
    del_answer = messagebox.askyesno("삭제", "정말로 삭제하겠습니까?")
    
    #만약 에를 눌렀다면
    if del_answer:
        
        del save_blank[index]