# import cv2

# detector = cv2.CascadeClassifier('./haarcascade_frontalface_default.xml')

# img=cv2.imread("./Akshay Kumar_0.jpg",0)
# faces = detector.detectMultiScale(img, 1.3, 5)


# for(x,y,w,h) in faces:
#     cv2.rectangle(img, (x,y), (x+w,y+h), (255,0,0), 2)
#     # Displaying the image with rectangles around face
#     # cv2.imwrite("../python/face.jpg",img[y:y+h,x:x+w])
#     cv2.imshow('k',img)

# cv2.waitKey(0)
# cv2.destroyAllWindows()




from transformers import pipeline
import PyPDF2

# Initialize the summarization pipeline
summarizer = pipeline("summarization", model="t5-base", tokenizer="t5-base", framework="tf")

# Open the PDF file and extract text
with open("./sad.pdf", "rb") as file:
    pdf = PyPDF2.PdfReader(file)
    text = ""
    for page_num in range(len(pdf.pages)):
        page = pdf.pages[page_num]
        text += page.extract_text()

# Summarize the text
summary = summarizer(text, max_length=70, min_length=150, do_sample=False)

# Print the summary
print(summary[0]['summary_text'])
