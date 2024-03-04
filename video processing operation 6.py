import cv2
video_path = r"C:\Users\K.JAYADATTA\Videos\Gara vs Rock Lee.mp4"
cap = cv2.VideoCapture(video_path)
if not cap.isOpened():
    print("Error opening video file")
while cap.isOpened():
    ret, frame = cap.read()

    if ret:

        cv2.imshow('Frame', frame)

        if cv2.waitKey(15) & 0xFF == ord('q'):
            break
    else:
        break

cap.release()
cv2.destroyAllWindows()
