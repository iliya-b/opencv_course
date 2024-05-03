import cv2

flipCode = 1
source = cv2.imread('cat.jpg')
result = cv2.flip(source, flipCode)

cv2.imwrite('result3.jpg', result)

cv2.imshow('Source', source)       
cv2.imshow('Result', result)

cv2.waitKey(0)
cv2.destroyAllWindows()