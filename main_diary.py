import tkinter as tk
from tkinter import messagebox

import cls.button as bt
import cls.label as lb
import cls.text as tx 
#save_txt을 담을 공간 생성
save_blank = []

def diary_main(main_frame, side_frame):
    # +버튼을 누르면 +버튼이 사라지게끔 하는 로직
    for widget in main_frame.winfo_children():
        widget.destroy
    #저장을 누르면 화면을 비우고 배열에 담는 로직
    def msg_save():
        
        t = title_txt.blank.get("1.0", "end-1c")
        c = content_txt.blank.get("1.0", "end-1c")
        
        save_txt = {"제목":t, "내용":c}
        #save_blank에 save_txt 담기
        save_blank.append(save_txt)        
        #저장을 누르면 저장 완료 창을 띄우기
        messagebox.showinfo("저장", "저장이 완료되었습니다.")
        # 화면을 비우는 로직 생성)
        for widget in main_frame.winfo_children():
            widget.destroy()
            
    # '제목'이라는 단어를 입력시키기
    title = lb.label(main_frame, "제목", 0, 0, "ne")
    title.lb_meker()
    # 제목을  쓸 수 있는 입력칸 생성
    title_txt = tx.text(main_frame, 100, 1, 0, 1, "ne")
    title_txt.txt_maker()
    # '내용'이라는 단어를 입력시키기
    content = lb.label(main_frame, "내용", 1, 0, "ne")
    content.lb_meker()
    # 내용을 쓸 수 있는 입력칸 생성
    content_txt = tx.text(main_frame, 100, 50, 1, 1, "ne")
    content_txt.txt_maker()
    # 저장 버튼 생성
    save = bt.button(main_frame, "저장", 2, 2, "n", msg_save)
    save.bnt_maker()
    
    #사이드바에 자신이 쓴 제목을 노출시키는 메인 바가 있어야 함
    side_frame_title = tk.Frame(side_frame, height=2, bg="gray", bd=1, relief="groove")
    side_frame.grid(sticky="n")
    #텍스트담은 곳에 제목을 띄우기
    for i in range(len(save_blank)):
        save_blank_type = save_blank[i]["제목"]
        side_frame_text = tk.Label(side_frame_title, text=save_blank_type, bg="gray")
        side_frame_text.grid(row=i, column=0, sticky="n")
        
        