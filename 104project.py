import cv2

# Read Image
img = cv2.imread("solar-system.jpg")



cv2.putText(img,  
           "Sun",
           (80, 100),  
           cv2.FONT_HERSHEY_COMPLEX_SMALL,
           2, 
           (255,255,255)
           )

cv2.putText(img,
            "Mercury",
           (105,190),
            cv2.FONT_HERSHEY_COMPLEX_SMALL,
            0.7,
            (255,255,255))

cv2.putText(img,
            "Venus",
            (190,170),
            cv2.FONT_HERSHEY_COMPLEX_SMALL,
            0.7,
            (255,255,255))

cv2.putText(img,
            "Moon",
            (280,170),
            cv2.FONT_HERSHEY_COMPLEX_SMALL,
            0.7,
            (255,255,255))

cv2.putText(img,
            "Earth",
            (280,265),
            cv2.FONT_HERSHEY_COMPLEX_SMALL,
            0.7,
            (255,255,255))

cv2.putText(img,
            "Mars",
            (380,170),
            cv2.FONT_HERSHEY_COMPLEX_SMALL,
            0.7,
            (255,255,255))

cv2.putText(img,
            "Jupiter",
            (570,50),
            cv2.FONT_HERSHEY_COMPLEX_SMALL,
            0.7,
            (255,255,255))

cv2.putText(img,
            "Saturn",
            (780,130),
            cv2.FONT_HERSHEY_COMPLEX_SMALL,
            0.7,
            (255,255,255))

cv2.putText(img,
            "Uranus",
            (960,130),
            cv2.FONT_HERSHEY_COMPLEX_SMALL,
            0.7,
            (255,255,255))

cv2.putText(img,
            "Neptune",
            (1110,130),
            cv2.FONT_HERSHEY_COMPLEX_SMALL,
            0.7,
            (255,255,255))

cv2.putText(img,
            "THE SOLAR SYSTEM",
            (280,400),
            cv2.FONT_HERSHEY_COMPLEX_SMALL,
            3,
            (255,255,255))
# Display Colored Image
cv2.imshow("Display Image",img)






cv2.waitKey(0)