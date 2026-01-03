import tkinter as tk
import main_diary as md
   
root = tk.Tk()
root.title("Diary")
root.geometry("1000x720")

#사이드바 형성
side_frame = tk.Frame(root, width=100, bg="lightgray")
side_frame.pack(side="left", fill="y")
#줄어드는 것을 방지하는 명령어
side_frame.pack_propagate(False)

# 사이드 바 2공간으로 나누기
#위에 칸 큰 제목이 들어올 곳
side_up = tk.Frame(side_frame, width=200, bg="lightgray")
side_up.pack(side="top", fill="both", expand=True)

#아래칸(버튼이 들어올 곳)
side_down = tk.Frame(side_frame, width=200, bg="lightgray")
side_down.pack(side="bottom",fill="x")

#삭제버튼 만들기
del_button = tk.Button(side_down, text="삭제", bg="white")
del_button.pack()

#메인바 형성
main_frame = tk.Frame(root, width=100, bg="white")
main_frame.pack(side="left", fill="both", expand=True)

#메인틀에 +버튼을 누르면 일기를 쓸 수 있도록 하는 로직 필요
plus_button = tk.Button(main_frame, text="+", width=10, height=5, command=lambda:md.diary_main(main_frame, side_up))
plus_button.place(relx=0.5, rely=0.5, anchor="center")

root.mainloop()
