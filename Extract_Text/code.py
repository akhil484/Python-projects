from PyPDF2 import PdfReader


reader = PdfReader("sample.pdf")
number_of_pages = len(reader.pages)

print(number_of_pages)

for page in reader.pages:
	text = page.extract_text()
	print(text)


