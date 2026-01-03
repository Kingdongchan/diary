import tkinter as tk
from tkinter import messagebox

import button as bt
import label as lb
import text as tx 

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
title_txt = tx.text(root, 100, 500, 1, 1, "ne")
title_txt.txt_maker()

root.mainloop()   