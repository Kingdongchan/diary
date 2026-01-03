import tkinter as tk
import main_diary as md

root = tk.Tk()
root.title("Diary")
root.geometry("1000x720")

#사이드바 형성
side_frame = tk.Frame(root, width=200, bg="lightgray")
side_frame.pack(side="left", fill="y")

# 사이드 바 2공간으로 나누기
#위에 칸 큰 제목이 들어올 곳
side_up = tk.Frame(side_frame, width=200, bg="lightgray")
side_up.pack(side="top")
#아래칸(버튼이 들어올 곳
side_down = tk.Frame(side_frame, width=200, bg="lightgray")
side_down.pack(side="top")

#메인바 형성
main_frame = tk.Frame(root, width=600, bg="white")
main_frame.pack(side="left", fill="both", expand=True)

plus_button = tk.Button(main_frame, text="+", width=10, height=5, command=lambda:md.diary_main(main_frame))
plus_button.place(relx=0.5, rely=0.5, anchor="center")

root.mainloop()
