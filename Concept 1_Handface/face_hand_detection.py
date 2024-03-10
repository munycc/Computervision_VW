import cv2
import json 
import mediapipe as mp


# Initialize the video capture device (webcam)
cap = cv2.VideoCapture(0)

# Initialize mediapipe module for hand detection
mpHands = mp.solutions.hands
hands = mpHands.Hands()


# Initialize Haar cascade classifier for face detection
face_cascade = cv2. CascadeClassifier (cv2.data.haarcascades +'haarcascade_frontalface_default.xml')




# Function Start

while True:

    success, img = cap.read()
    h, w, c = img.shape

    # resizing the frame for better view
    #img = cv2.resize(img, (1500, 1000))

    # process image and find hand
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = hands.process(imgRGB)


    # Get rectangle around hand
    hand_landmarks = results.multi_hand_landmarks
    if hand_landmarks:
        for handLMs in hand_landmarks:
            x_max = 0
            y_max = 0
            x_min = w
            y_min = h
            for lm in handLMs.landmark:
                x, y = int(lm.x * w), int(lm.y * h)
                if x > x_max:
                    x_max = x
                if x < x_min:
                    x_min = x
                if y > y_max:
                    y_max = y
                if y < y_min:
                    y_min = y
            rect_2= cv2.rectangle(img, (x_min, y_min), (x_max, y_max), (0, 255, 0), 2)
            rect1x, rect1y = ((x_min+x_max)/2, (y_min+y_max)/2)
            x1 = int(rect1x)
            y1 = int(rect1y)
            rect1center = int(rect1x),int(rect1y)
            point_1 = cv2.circle( rect_2, (rect1center), radius=8, color=(0,255,0), thickness=-1)

                
                    
    # process image and find face 
    gray = cv2.cvtColor (img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale (gray, 2, 4)
       
    # Get rectangle and point for face
    for (x,y,w1,h1) in faces:
        x_max2 = x+w1
        y_max2= y+h1
        rect = cv2. rectangle (img, (x,y), (x+w1, y+h1), (255,0,0), 2)
        rect2x, rect2y = ((x+x_max2)/2, (y+y_max2)/2)
        x2 = int(rect2x)
        y2 = int(rect2y)
        rect2center = int(rect2x),int(rect2y)
        point_2 = cv2.circle( rect, (rect2center), radius=8, color=(255,0,0), thickness=-1)


            

    cv2.imshow("Image", img)

   
    # Enter key 'e' to break the loop
    if cv2.waitKey(5) & 0xFF == ord('e'):
       
        a = print ("Rectangle height and width")
        b = print (h,w)

        c = print ("Hand_point")
        d = print(rect1center)

        e = print("Face_point")
        f = print(rect2center)

        print(x_max)
        print(y_max)
        print(x_max2)
        print(y_max2)

        break
   
cap.release ()
cv2.destroyAllWindows()


# Append all of the different positions, size of the overall windows
List =[]
List.append (h)
List.append (w)
List.append (x1)
List.append (y1)
List.append (x2)
List.append (y2)
List.append (str (y_max2))
List.append (str (y_max) )


dict_1= {k: v for v, k in enumerate(List)}
print (dict_1)


# Create the Json file
with open("sample.json", "w") as outfile:
    json.dump(dict_1, outfile)

