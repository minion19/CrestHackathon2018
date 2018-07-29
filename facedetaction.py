import cv2
import face_recognition

cap = cv2.VideoCapture(0)
cap.set(3, 1000)
cap.set(4, 800)
riaan_image = face_recognition.load_image_file("riaan shah.jpg")
sashwat_image = face_recognition.load_image_file("sashwat jain.jpg")
malhar_image = face_recognition.load_image_file("malhar shah.jpg")

# load all images(faces)

riaan_encoding = face_recognition.face_encodings(riaan_image)[0]
sashwat_encoding = face_recognition.face_encodings(sashwat_image)[0]
malhar_encoding = face_recognition.face_encodings(malhar_image)[0]

# encode all faces

known_face_encodings = [
    sashwat_encoding,
    riaan_encoding,
    malhar_encoding
]

#setup a known database of encodings

known_face_names = [
    "Sashwat Jain",
    "Riaan Shah",
    "Malhar Shah"
]

#setup a known database of names

face_locations = []
face_encodings = []
face_names=[]
process_this_frame = True
#set variables

while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()
    small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)

    #resize frame

    rgb_small_frame = small_frame[:, :, ::-1]

    #GRB to RGB greyscale converter

    if process_this_frame:

        face_locations = face_recognition.face_locations(rgb_small_frame)
        face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)
        face_names = []


        for face_encoding in face_encodings:
            matches = face_recognition.compare_faces(known_face_encodings, face_encoding)
            name="UNKNOWN"
            if True in matches:
                index=matches.index(True)
                print (index)
                name = known_face_names[index]
            face_names.append(name)

    process_this_frame = not process_this_frame

    for (top, right, bottom, left), name in zip(face_locations, face_names):
        # Scale back up face locations since the frame we detected in was scaled to 1/4 size
        top *= 4
        right *= 4
        bottom *= 4
        left *= 4
        # Draw a box around the face
        cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)
        # Draw a label with a name below the face
        cv2.rectangle(frame, (left, bottom - 35), (right, bottom), (0, 0, 255), cv2.FILLED)
        font = cv2.FONT_HERSHEY_DUPLEX
        cv2.putText(frame, name, (left + 6, bottom - 6), font, 1.0, (255, 255, 255), 1)
        # Display the resulting image
    cv2.imshow('Video', frame)
    if cv2.waitKey(1) & 0xFF == 113:
        break
# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()