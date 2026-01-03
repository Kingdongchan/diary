import tkinter as tk
from tkinter import messagebox

import cls.button as bt
import cls.label as lb
import cls.text as tx 

def diary_main():
    #저장을 누르면 화면을 비우고 배열에 담는 로직
    def msg_save():
        
        t = title_txt.blank.get("1.0", "end-1c")
        c = content_txt.blank.get("1.0", "end-1c")
        
        save_txt = {"제목":t, "내용":c}
        
        #저장을 누르면 저장 완료 창을 띄우기
        messagebox.showinfo("저장", "저장이 완료되었습니다.")
        # 화면을 비우는 로직 생성)
        for widget in root.winfo_children():
            widget.destroy()
            

    root= tk.Tk()
    # '제목'이라는 단어를 입력시키기
    title = lb.label(root, "제목", 0, 0, "ne")
    title.lb_meker()
    # 제목을  쓸 수 있는 입력칸 생성
    title_txt = tx.text(root, 100, 1, 0, 1, "ne")
    title_txt.txt_maker()
    # '내용'이라는 단어를 입력시키기
    content = lb.label(root, "내용", 1, 0, "ne")
    content.lb_meker()
    # 내용을 쓸 수 있는 입력칸 생성
    content_txt = tx.text(root, 100, 50, 1, 1, "ne")
    content_txt.txt_maker()
    # 저장 버튼 생성
    save = bt.button(root, "저장", 2, 2, "n", msg_save)
    save.bnt_maker()
   