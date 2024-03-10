import cv2
import mediapipe
import json
 


# Initialize the video capture device (webcam)
capture = cv2.VideoCapture(0)


# Initialize mediapipe module for finger detection
drawingModule = mediapipe.solutions.drawing_utils
handsModule = mediapipe.solutions.hands


# Get the width and height of the video frame
frameWidth = capture.get(cv2.CAP_PROP_FRAME_WIDTH)
frameHeight = capture.get(cv2.CAP_PROP_FRAME_HEIGHT)

# Initialize an empty list to store previous finger locations
previousLocations = []


# process each frame in infinite loop, until the user finishes, to get ou press 'e'
with handsModule.Hands(static_image_mode=False, min_detection_confidence=0.7, min_tracking_confidence=0.7, max_num_hands=1) as hands:
 
    while (True):
 
        success, frame = capture.read()
 
        if success == False:
            continue
 
        frame = cv2.flip(frame, 1)
 
        results = hands.process(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
        circleColor = (0, 0, 0)

        # If there are detected hand landmarks, extract the landmark for the index finger tip and convert it to pixel coordinates
        if results.multi_hand_landmarks != None:
 
            normalizedLandmark = results.multi_hand_landmarks[0].landmark[handsModule.HandLandmark.INDEX_FINGER_TIP]
            pixelCoordinatesLandmark = drawingModule._normalized_to_pixel_coordinates(normalizedLandmark.x,
                                                                                      normalizedLandmark.y,
                                                                                      frameWidth,
                                                                                      frameHeight)
 
            cv2.circle(frame, pixelCoordinatesLandmark, 10, (255,0,0), -1)
            print (pixelCoordinatesLandmark)
            
           
            # store the current location of the index finger tip
            previousLocations.append(pixelCoordinatesLandmark)

            
            
        cv2.imshow('Test image', frame)
 
        if cv2.waitKey(5) & 0xFF == ord('e'):
            print (previousLocations)
            break
 

cv2.destroyAllWindows()
capture.release()

# Filter Null elements
updated_locations = list(filter(None, previousLocations))

points_dict = {}
for i, point in enumerate(updated_locations):
    points_dict[i] = point


# Create a Json file for points position
with open('points.json', 'w') as f:
    json.dump(points_dict, f)


List =[]
List.append (int(frameHeight))
List.append (int(frameWidth))

dict_1= {k: v for v, k in enumerate(List)}
print (dict_1)

# Create a Json file for rectangle frame
with open("rectangle.json", "w") as outfile:
    json.dump(dict_1, outfile)
