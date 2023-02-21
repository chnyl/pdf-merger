import os
from PyPDF2 import PdfMerger

################ 함수 ################
# PDF이름 받는 함수
def ouput_pdf_name(num):
    all_pdfs = []
    for i in range(num):
        pdf_name = input(f"{i+1}번째 PDF의 파일명을 입력하세요 : ")
        new_pdf_name = naming(pdf_name)
        all_pdfs.append(new_pdf_name)
    return all_pdfs

# 파일이름 뒤에 .pdf 붙혀주는 함수
suffix = '.pdf'
def naming (pdf_name) :
    return str(pdf_name) + suffix

################ MAIN ################
#1) 변환하고 싶은 파일이 있는 주소 붙혀넣기
current_directory = input("변환하고 싶은 파일이 있는 주소를 붙혀넣으세요 : ")

#2) PDF 병합 과정
num_pdfs = int(input("병합할 PDF 개수를 입력하세요 : "))
all_pdfs = ouput_pdf_name(num_pdfs)
print("병합할 PDF파일들은 아래와 같습니다\n", all_pdfs)

#3) 병합된 PDF 파일 이름 작성
merged_file_name = naming(input("최종 PDF 이름을 써주세요 : "))

################ 추가 과정 ################
#1) 파일 디렉토리를 새롭게 변환하는 과정
print('# 현재 파일 경로:', __file__)
print('# 실행 폴더 경로:', os.getcwd())
print("# 변경 전 작업디렉토리: %s"%os.getcwd())
os.chdir(current_directory)
print("→ 변경 후 작업디렉토리: %s"%os.getcwd())

#2) PDF 병합 과정
merger = PdfMerger()
for pdf in all_pdfs:
    merger.append(pdf)
merger.write(merged_file_name)
merger.close()
