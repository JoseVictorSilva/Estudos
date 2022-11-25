import cv2 as cv

rastreador = cv.TrackerKCF_create()

video = cv.VideoCapture('../ArquivosBase/race.mp4')
ok,frame = video.read()
bbox = cv.selectROI(frame) #ROI Region Of Interest

ok = rastreador.init(frame, bbox)

while True:
    ok ,frame = video.read()
    if not ok: 
        break
    ok ,bbox = rastreador.update(frame)
    print(ok)

    if ok:
        (x, y, w, h) = [int(v) for v in bbox]
        cv.rectangle(frame, (x,y), (x+w, y+h), (0,255,0), 2, 1)
    else:
        cv.putText(frame, 'Erro', (100,80), cv.FONT_HERSHEY_SIMPLEX, 1, (0,0,255), 2)

    cv.imshow('Rastreamento',frame)
    if cv.waitKey(1) & 0XFF == 27:
        break