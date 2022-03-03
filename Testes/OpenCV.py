import cv2 as cv2, numpy as np

video = cv2.VideoCapture(0,cv2.CAP_DSHOW)
imgMao = cv2.imread('fotos/mao.png',cv2.IMREAD_GRAYSCALE)
while True:
    ret, frame = video.read()
    #cv2.imshow('frame',frame)
    resultado = cv2.matchTemplate(frame ,imgMao, cv2.TM_CCOEFF_NORMED)
    cv2.imshow('Resultado', resultado)
    if cv2.waitKey(1) == ord('q'):
        break

video.release()
cv2.destroyAllWindows()



'''imgMao = cv.imread('fotos/mao.png',cv.IMREAD_COLOR)
cv.namedWindow('Hello World')
cv.imshow('Hello World', imgMao)
cv.waitKey()'''