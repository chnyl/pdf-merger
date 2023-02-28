import tkinter as tk
from tkinter.filedialog import askdirectory, askopenfilename, askopenfilenames, asksaveasfilename
from tkinter import messagebox
from PyPDF2 import PdfMerger, PdfReader

root = tk.Tk()
root.title('PDF병합')
root.minsize(400, 300)
root.option_add("*Font", "Arial 10")

# 기능1 : 파일 여러개 선택
def select_files():
    try:
        filenames = askopenfilenames(initialdir="./", filetypes=(("pdf files", ".pdf"), ('All files', '*.*')))
        if filenames:
            for filename in filenames:
                listbox1.insert(0, filename)
    except:
        messagebox.showerror("Error", "오류가 발생했습니다.")
        listbox1.delete(0, "end")

# 기능2: 병합
def merging():
    try:
        merges = messagebox.askyesno("병합하기", "병합하시겠습니까?")
        if merges:
            pdf_merger = PdfMerger()
            for pdf_file in listbox1:
                pdf_merger.append(PdfReader(pdf_file, "rb"))
            merged_file = asksaveasfilename(defaultextension=".pdf")
            with open(merged_file, "wb") as output:
                pdf_merger.write(output)
            # pdf_merger.write('병합PDF')
            # pdf_merger.close()
    except:
        messagebox.showerror("Error", "오류가 발생했습니다.")

# 기능3: 초기화
def refresh():
    try:
        reply = messagebox.askyesno("초기화", "정말로 초기화 하시겠습니까?")
        if reply:
            listbox1.delete(0, "end")
            messagebox.showinfo("Success", "초기화 되었습니다.")
    except:
        messagebox.showerror("Error", "오류가 발생했습니다.")

'''1. 프레임 생성'''
# 상단 프레임 (LabelFrame)
frm1 = tk.LabelFrame(root, text="파일 추가", pady=15, padx=15)   # pad 내부
frm1.grid(row=0, column=0, pady=10, padx=10, sticky="nswe") # pad 내부
root.columnconfigure(0, weight=1)   # 프레임 (0,0)은 크기에 맞춰 늘어나도록
root.rowconfigure(0, weight=1)      
# 하단 프레임 (Frame)
frm2 = tk.Frame(root, pady=10)
frm2.grid(row=1, column=0, pady=10)

'''2. 요소 생성'''
# 레이블
lbl3 = tk.Label(frm1, text='파일 여러 개 선택')
# 리스트박스
listbox1 = tk.Listbox(frm1, width=60)
# 버튼
btn1 = tk.Button(frm1, text="파일 선택", width=8, command=select_files)
btn2 = tk.Button(frm2, text="병합하기", width=8, command=merging)
btn3 = tk.Button(frm2, text="초기화", width=8, command=refresh)
# 스크롤바 - 기능 연결
scrollbar = tk.Scrollbar(frm1)
scrollbar.config(command=listbox1.yview)
listbox1.config(yscrollcommand=scrollbar.set)

'''3. 요소 배치'''
# 상단 프레임
lbl3.grid(row=0, column=0, sticky="n")
listbox1.grid(row=1, column=0, rowspan=2, sticky="wens")
scrollbar.grid(row=1, column=2, rowspan=3, sticky="wens")
btn1.grid(row=1, column=3, sticky="n")
# 상단프레임 grid (2,1)은 창 크기에 맞춰 늘어나도록
frm1.rowconfigure(2, weight=1)      
frm1.columnconfigure(1, weight=1)   
# 하단 프레임
btn2.grid(row=0, column=0)
btn3.grid(row=0, column=1)

'''실행'''
root.mainloop()