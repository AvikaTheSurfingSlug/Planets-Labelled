import cv2
img = cv2.imread("solar-system.jpg")
cv2.putText(img, "Sun", (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255))
cv2.putText(img, "Mercury", (110, 180), cv2.FONT_HERSHEY_SIMPLEX, 0.4, (255, 255, 255))
cv2.putText(img, "Venus", (190, 180), cv2.FONT_HERSHEY_SIMPLEX, 0.4, (255, 255, 255))
cv2.putText(img, "Earth", (300, 180), cv2.FONT_HERSHEY_SIMPLEX, 0.4, (255, 255, 255))
cv2.putText(img, "Mars", (390, 180), cv2.FONT_HERSHEY_SIMPLEX, 0.4, (255, 255, 255))
cv2.putText(img, "Jupiter", (560, 50), cv2.FONT_HERSHEY_SIMPLEX, 0.4, (255, 255, 255))
cv2.putText(img, "Saturn", (780, 130), cv2.FONT_HERSHEY_SIMPLEX, 0.4, (255, 255, 255))
cv2.putText(img, "Uranus", (980, 130), cv2.FONT_HERSHEY_SIMPLEX, 0.4, (255, 255, 255))
cv2.putText(img, "Neptune", (1100, 130), cv2.FONT_HERSHEY_SIMPLEX, 0.4, (255, 255, 255))
cv2.imshow("solar system", img)
cv2.waitKey(0)
cv2.imwrite("solar-labelled-system.jpg",img)