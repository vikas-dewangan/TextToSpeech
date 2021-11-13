import pyttsx3
import PyPDF2
while True:
    book = open("ppc.pdf","rb")
    pdfReader = PyPDF2.PdfFileReader(book)
    pages = pdfReader.numPages
    speaker = pyttsx3.init()
    page = pdfReader.getPage(int(input(f"enter page number from 0 to {pages-1}:")))
    text = page.extractText()
    speaker.say(text)
    speaker.runAndWait()