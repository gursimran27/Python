import face_recognition
import cv2

# Load sample images and encode faces
sample_image1 = face_recognition.load_image_file("./elon.jpeg")
sample_encoding1 = face_recognition.face_encodings(sample_image1)[0]

sample_image2 = face_recognition.load_image_file("./akshay.jpg")
sample_encoding2 = face_recognition.face_encodings(sample_image2)[0]

# Create a list of known face encodings
known_face_encodings = [
    sample_encoding1,
    sample_encoding2
]
known_face_names = [
    "Person 1",
    "Person 2"
]

# Load an image with multiple faces
image = cv2.imread("./group.jpeg")
rgb_image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

# Find all the faces and face encodings in the image
face_locations = face_recognition.face_locations(rgb_image)
face_encodings = face_recognition.face_encodings(rgb_image, face_locations)

# Loop through each face found in the image
for (top, right, bottom, left), face_encoding in zip(face_locations, face_encodings):
    # Compare this face to known faces
    matches = face_recognition.compare_faces(known_face_encodings, face_encoding)
    name = "Unknown"

    # If a match is found, use the name of the known face
    if True in matches:
        first_match_index = matches.index(True)
        name = known_face_names[first_match_index]

    # Draw a box around the face and label it
    cv2.rectangle(image, (left, top), (right, bottom), (0, 255, 0), 2)
    cv2.putText(image, name, (left + 6, bottom - 6), cv2.FONT_HERSHEY_DUPLEX, 0.5, (0, 255, 0), 1)

# Display the resulting image
cv2.imshow("Faces Identified", image)
cv2.waitKey(0)
cv2.destroyAllWindows()
