import tkinter as tk
from tkinter import messagebox

import cls.button as bt
import cls.label as lb
import cls.text as tx 
#save_txt을 담을 공간 생성
save_blank = []

def diary_main(main_frame, side_up):
    # +버튼을 누르면 +버튼이 사라지게끔 하는 로직
    for widget in main_frame.winfo_children():
        widget.destroy()
    #저장을 누르면 화면을 비우고 배열에 담는 로직
    def msg_save():
        
        t = title_txt.blank.get("1.0", "end-1c")
        c = content_txt.blank.get("1.0", "end-1c")
        
        save_txt = {"제목":t, "내용":c}
        #save_blank에 save_txt 담기
        save_blank.append(save_txt)
                
        side_title(side_up, main_frame)
        #저장을 누르면 저장 완료 창을 띄우기
        messagebox.showinfo("저장", "저장이 완료되었습니다.")
        # 화면을 비우는 로직 생성)
        for widget in main_frame.winfo_children():
            widget.destroy()
            
        plus_button = tk.Button(main_frame, text="+", width=10, height=5, command=lambda:diary_main(main_frame, side_up))
        plus_button.place(relx=0.5, rely=0.5, anchor="center")
            
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
    

#사이드바에 표시하는 로직 형성    
def side_title(side_up, main_frame):

    for widget in side_up.winfo_children():
        widget.destroy()
        
    #중앙에 있도록 하는 가중치 명령어 
    side_up.columnconfigure(0, weight=1)
    
    #텍스트담은 곳에 제목을 띄우기
    for i in range(len(save_blank)):
        data = save_blank[i]
        side_frame_text = tk.Button(side_up, text=data["제목"], bg="white", relief="raised", command=lambda:see_save_diary(main_frame, data))
        side_frame_text.grid(row=i, column=0, sticky="ew")
        
#버튼을 눌렀을 떄 전에 썻던 내용들이 나와야함
def see_save_diary(main_frame, data):
    
    for widget in main_frame.winfo_children():
        widget.destroy()
            
    # '제목'이라는 단어를 입력시키기
    title = lb.label(main_frame, "제목", 0, 0, "ne")
    title.lb_meker()
    
    see_title_txt = tx.text(main_frame, 100, 1, 0, 1, "ne")
    see_title_txt.txt_maker()
    see_title_txt.blank.insert("1.0", data["제목"])
    
    # '내용'이라는 단어를 입력시키기
    content = lb.label(main_frame, "내용", 1, 0, "ne")
    content.lb_meker()
    
    see_content_txt = tx.text(main_frame, 100, 30, 1, 1, "ne")
    see_content_txt.txt_maker()
    see_content_txt.blank.insert("1.0", data["내용"])
    
