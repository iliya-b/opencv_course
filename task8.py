#- изменить контрасть изображения
import cv2
import numpy as np
   
def increaseContrast(image, clipLim):
    labImage = cv2.cvtColor(image, cv2.COLOR_BGR2LAB)
    lChannel, a, b = cv2.split(labImage)
    
    gridSize = (8, 8)

    clahe = cv2.createCLAHE(clipLimit=clipLim, tileGridSize=gridSize)
    cl = clahe.apply(lChannel)
    limg = cv2.merge((cl,a,b))

    return cv2.cvtColor(limg, cv2.COLOR_LAB2BGR)

source = cv2.imread('cat.jpg')
result= increaseContrast(source, 2)

cv2.imwrite('result8.jpg', result)

cv2.imshow("Source", source)
cv2.imshow('Result ', result)

cv2.waitKey(0)
cv2.destroyAllWindows()