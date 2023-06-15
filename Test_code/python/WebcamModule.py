import cv2

cap = cv2.VideoCapture(cv2.CAP_V4L2)
#cap = cv2.VideoCapture(-1)

def getImg(display=False, size=[240, 180]):
    _, img = cap.read()
    img = cv2.resize(img, (size[0], size[1]))
    if display:
        cv2.imshow("Image", img)
        cv2.waitKey(1)
    return img

if __name__ == '__main__':
    while True:
        img = getImg(True)
