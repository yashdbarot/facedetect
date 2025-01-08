import cv2
import os
import uuid

# Initialize the video capture object
cap = cv2.VideoCapture(0)
if not cap.isOpened():
    print("Error: Could not open webcam.")
    exit()

# Load Haar Cascade for face detection
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# Create a directory to save the captured images
dataset_dir = 'dataset'
os.makedirs(dataset_dir, exist_ok=True)

person_name = input("Enter the name of the person: ")
person_dir = os.path.join(dataset_dir, person_name)
os.makedirs(person_dir, exist_ok=True)

count = 0
try:
    while True:
        ret, frame = cap.read()
        if not ret:
            print("Failed to capture frame. Exiting...")
            break

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

        for (x, y, w, h) in faces:
            count += 1
            face = frame[y:y+h, x:x+w]  # Save in color
            face_filename = os.path.join(person_dir, f'{str(uuid.uuid4())}.jpg')
            cv2.imwrite(face_filename, face)
            print(f"Saved: {face_filename}")
            cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)

        cv2.imshow('Capturing Faces', frame)
        if cv2.waitKey(1) & 0xFF == ord('q') or count >= 100:
            break
finally:
    cap.release()
    cv2.destroyAllWindows()
