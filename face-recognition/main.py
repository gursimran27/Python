import cv2
import face_recognition

img=cv2.imread("./WhatsApp Image 2024-03-05 at 19.48.23_10432969.jpg")
rgd_img=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
img_encoding=face_recognition.face_encodings(rgd_img)[0]



img2=cv2.imread("./WhatsApp Image 2024-03-05 at 19.49.08_03c69606.jpg")
rgd_img2=cv2.cvtColor(img2,cv2.COLOR_BGR2RGB)
img_encoding2=face_recognition.face_encodings(rgd_img2)[0]


result=face_recognition.compare_faces([img_encoding],img_encoding2)

print(result)




# import cv2 

# # Load the pre-trained face detector
# detector = cv2.CascadeClassifier('./haarcascade_frontalface_default.xml')

# # Create a VideoCapture object and read from input file 
# cap = cv2.VideoCapture("./video (2160p).mp4")

# # Check if camera opened successfully 
# if not cap.isOpened(): 
#     print("Error opening video file") 

# count = 0

# # Read until video is completed 
# while cap.isOpened():
#     ret, img = cap.read() # Read the frames using the VideoCapture object
    
#     if ret:
#         # Convert the frame to grayscale
#         converted_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        
#         # Detect faces in the grayscale frame
#         faces = detector.detectMultiScale(converted_image, 1.1, 10)
        
#         for (x, y, w, h) in faces:
#             count += 1
#             # Draw a rectangle around each detected face
#             cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)
            
#             # Save images of each detected face
#             cv2.imwrite("./samples/face." + str(count) + ".jpg", converted_image[y:y+h, x:x+w])

#     else:
#         print("All frames have been processed. Exiting the loop...")
#         break  # Break out of the loop if no frames are left to read

# print("All faces detected. Closing the program...")
# cap.release()
# cv2.destroyAllWindows()
