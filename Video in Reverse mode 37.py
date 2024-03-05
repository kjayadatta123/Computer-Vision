import cv2
cap = cv2.VideoCapture(r"C:\Users\K.JAYADATTA\Videos\Gara vs Rock Lee.mp4")
if not cap.isOpened():
    print("Error: Unable to open the video file.")
    exit()

total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
current_frame = total_frames - 1

while current_frame >= 0:
    cap.set(cv2.CAP_PROP_POS_FRAMES, current_frame)
    ret, frame = cap.read()
    if not ret:
        print("Error: Unable to read frame.")
        break
    cv2.imshow('Video in Reverse', frame)

    if cv2.waitKey(25) & 0xFF == ord('q'):
        break
    current_frame -= 1
cap.release()
cv2.destroyAllWindows()
