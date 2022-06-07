import cv2

car_classifier = 'cars.xml'
body_classifier = 'fullbody.xml'

car_classifier_file = cv2.CascadeClassifier(car_classifier)
body_classifier_file = cv2.CascadeClassifier(body_classifier)

webcam = cv2.VideoCapture('cv.mp4')

while True:

    sucessful_frame_read, frame = webcam.read()

    if sucessful_frame_read:

        bw_video = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    else:
        break

    cars_coordinates = car_classifier_file.detectMultiScale(bw_video)
    pedestrain_coordinates = body_classifier_file.detectMultiScale(bw_video)

    for (x, y, w, h) in cars_coordinates:
        cv2.rectangle(frame, (x+1, y+1), (x+w, y+h), (255, 0, 0), 5)
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 5)

    for (x, y,w,h) in pedestrain_coordinates:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 255), 5)

    cv2.imshow('Car Detector', frame)
    key = cv2.waitKey(1)

    if key==81 or key==113:
        break

webcam.release()










































'''
import cv2

image_file = 'car.jpg'

car_classifier_file = 'cars.xml'


img = cv2.imread(image_file)

car_detector = cv2.CascadeClassifier(car_classifier_file)


bw_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

cars = car_detector.detectMultiScale(bw_img)

print(cars)

for (x, y, w, h) in cars:
    cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 2)

cv2.imshow('Car', img)
cv2.waitKey()

print('all ok')

'''