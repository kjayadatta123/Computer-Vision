import cv2

cap = cv2.VideoCapture(r"D:\movies\movies\Spy x Family\@Animee_4u - Spy x Family (2022) S01E01 100p HDRip [Telugu .mkv")

if not cap.isOpened():
    print("Error opening video file")

while cap.isOpened():
    ret, frame = cap.read()
    if ret:
        cv2.imshow('Frame', frame)
        if cv2.waitKey(250) & 0xFF == ord('q'):
            break
    else:
        break

cap.release()
cv2.destroyAllWindows()
