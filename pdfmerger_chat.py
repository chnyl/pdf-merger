import tkinter as tk
from tkinter import filedialog
from PyPDF2 import PdfMerger, PdfReader

# Create Tkinter window and hide it
root = tk.Tk()
root.withdraw()

# Ask the user to select PDF files to merge
pdf_files = filedialog.askopenfilenames(
    filetypes=[("PDF Files", "*.pdf")],
    title="Select PDF files to merge",
    multiple=True  # Allows the user to select multiple files at once
)

# Create an instance of PdfFileMerger
pdf_merger = PdfMerger()

# Loop through the selected PDF files and add them to the merger
for pdf_file in pdf_files:
    pdf_merger.append(PdfReader(pdf_file, "rb"))

# Ask the user to select a name and location for the merged PDF file
merged_file = filedialog.asksaveasfilename(
    defaultextension=".pdf",
    filetypes=[("PDF Files", "*.pdf")],
    title="Save merged PDF file as"
)

# Write the merged PDF to the selected location
with open(merged_file, "wb") as output:
    pdf_merger.write(output)

# Close the merger
pdf_merger.close()
