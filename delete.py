import tkinter as tk
from tkinter import messagebox 

import main_diary as md
import reset as rs
def side_del (index, save_blank, side_up, main_frame):
    #삭제 할 떄 정말 삭제할 지 이야기 해주는 안내창
    del_answer = messagebox.askyesno("삭제", "정말로 삭제하겠습니까?")
    
    #만약 에를 눌렀다면
    if del_answer:
        
        del save_blank[index]
        # 사이드바 새로고침
        md.side_title(side_up, main_frame)
        # 메인틀 새로고침
        rs.re_set(main_frame, side_up)