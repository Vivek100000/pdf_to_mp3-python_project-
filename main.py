import pyttsx3,PyPDF2
#very important project
PdfReader = PyPDF2.PdfReader(open('book.pdf','rb'))
speaker = pyttsx3.init()

for page_num in range(len(PdfReader.pages)):
    text = PdfReader.pages[page_num].extract_text()
    processed_text = text.strip().replace('\n',' ')


speaker.save_to_file(processed_text,'mp3_fromat.mp3')
speaker.runAndWait()

speaker.stop()
