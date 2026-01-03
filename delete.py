import tkinter as tk
from tkinter import messagebox 

import reset as rs

def side_del (save_blank, side_up, main_frame):
    import main_diary as md 
    
    #인덱스 할당
    index = md.current_index
    
    if index is None:
        messagebox.showwarning("경고", "삭제할 일기를 먼저 선택하세요.")
        
        return
    #삭제 할 떄 정말 삭제할 지 이야기 해주는 안내창
    del_answer = messagebox.askyesno("삭제", "정말로 삭제하겠습니까?")
    
    #만약 에를 눌렀다면
    if del_answer:
        del save_blank[index]
        
        #index 초기화
        md.current_index = None

        # 사이드바 새로고침
        md.side_title(side_up, main_frame)
        # 메인틀 새로고침
        rs.re_set(main_frame, side_up)