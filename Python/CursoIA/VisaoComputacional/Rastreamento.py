import cv2

rastreador = cv2.TrackerCSRT_create()
video = cv2.VideoCapture('Arquivos/rua.mp4')
ok, frame = video.read()

bbox = cv2.selectROI(frame)
print(bbox)

ok = rastreador.init(frame, bbox)
print(ok)

while True: 
    ok, frame = video.read()
    if not ok:
        break
    ok, bbox = rastreador.update(frame)
    print(bbox)

    if ok:
        (x,y,w,h) = [int(v) for v in bbox]
        cv2.rectangle(frame, (x,y), (x+w,y+h), (0,255,0), 2, 1)
    else:
        cv2.putText(frame, 'Falha no rastreamento', (100,80),
        cv2.FONT_HERSHEY_COMPLEX, .75, (0,0,255), 2)
    cv2.imshow('Rastreando', frame)
    if cv2.waitKey(1) and 0XFF == 27:
        break