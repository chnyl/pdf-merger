import os
import tkinter as tk
import tkinter.simpledialog as sd
from PyPDF2 import PdfMerger

################ 함수 ################
# PDF이름 받는 함수
def ouput_pdf_name(num):
    all_pdfs = []
    for i in range(num):
        win4 = tk.Tk()
        win4.withdraw()
        win4.resizable(True, True)
        win4.geometry('600x200+500+500')
        win4.option_add("*Font", "Arial 10")
        pdf_name = sd.askstring("PDF 생성", f"{i+1}번째 PDF의 파일명을 입력하세요")
        new_pdf_name = naming(pdf_name)
        all_pdfs.append(new_pdf_name)
    return all_pdfs

# 파일이름 뒤에 .pdf 붙혀주는 함수
suffix = '.pdf'
def naming (pdf_name) :
    return str(pdf_name) + suffix

################ MAIN ################
#1) 변환하고 싶은 파일이 있는 주소 붙혀넣기
win1 = tk.Tk()
win1.withdraw()
win1.resizable(True, True)
win1.geometry('600x200+500+500')
win1.option_add("*Font", "Arial 10")
current_directory = sd.askstring("파일주소입력", "변환하고 싶은 파일이 있는 주소를 붙혀넣으세요")

#2) PDF 병합 과정
win2 = tk.Tk()
win2.withdraw()
win2.resizable(True, True)
win2.geometry('600x200+500+500')
win2.option_add("*Font", "Arial 10")
num_pdfs = sd.askinteger("PDF 개수", "병합할 PDF 개수를 입력하세요")
all_pdfs = ouput_pdf_name(num_pdfs)

#3) 병합된 PDF 파일 이름 작성
win3 = tk.Tk()
win3.withdraw()
win3.resizable(True, True)
win3.geometry('600x200+500+500')
win3.option_add("*Font", "Arial 10")
merged_file_name = naming(sd.askstring("PDF 생성", "최종 PDF 이름을 써주세요"))

################ 추가 과정 ################
#1) 파일 디렉토리를 새롭게 변환하는 과정
# print('# 현재 파일 경로:', __file__)
# print('# 실행 폴더 경로:', os.getcwd())
# print("# 변경 전 작업디렉토리: %s"%os.getcwd())
os.chdir(current_directory)
# print("→ 변경 후 작업디렉토리: %s"%os.getcwd())

#2) PDF 병합 과정
merger = PdfMerger()
for pdf in all_pdfs:
    merger.append(pdf)
merger.write(merged_file_name)
merger.close()
