# Project 2 - Merge PDF
!pip install PyPDF2

# Step 1: import library
import PyPDF2 # deal with pdf file
from google.colab import files # using google colab's files section

# Step 2: Upload PDF Files
uploaded_files = files.upload()

# Step 3: Activate PDF Merger
merger = PyPDF2.PdfMerger()

# Step 4: Add each uploaded files
for pdf in uploaded_files.keys():
  merger.append(pdf)

# Step 5: Save merged files
merger.write('merged_files.pdf')
merger.close()

print('Merged PDF is saved!')
