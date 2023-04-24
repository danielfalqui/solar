import cv2

img = cv2.imread("solar-system.jpg")

cv2.putText(img, "Sol", (100,80), cv2.FONT_HERSHEY_SIMPLEX, 2, (0,0,255))
cv2.putText(img, "Mercurio", (120,250), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0,0,255))
cv2.putText(img, "Venus", (195,250), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0,0,255))
cv2.putText(img, "Terra", (290,260), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0,0,255))
cv2.putText(img, "Marte", (380,260), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0,0,255))
cv2.putText(img, "Jupiter", (580,360), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0,0,255))
cv2.putText(img, "Saturno", (750,280), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0,0,255))
cv2.putText(img, "Urano", (975,280), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0,0,255))
cv2.putText(img, "Netuno", (1110,280), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0,0,255))

cv2.imshow("resultado", img)
cv2.waitKey(0)