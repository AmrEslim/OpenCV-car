
from MotorModule import Motor
from LaneModule import getLaneCurve
import WebcamModule
import cv2
import time

##################################################
motor = Motor(10, 11, 9, 17, 22, 27)
##################################################

def main():
    img = WebcamModule.getImg()
    curveVal= getLaneCurve(img, 1)
    print("original Value -----------> : ")
    print(curveVal)
    #sen = 1  # SENSITIVITY
    maxVAl= 0.03 # MAX SPEED
    if curveVal>maxVAl:curveVal = maxVAl
    if curveVal<-maxVAl: curveVal =-maxVAl
    #print("converted Value -----------> : ")
    #print(curveVal)
    #if curveVal>0:
    #    if curveVal<0.05: curveVal=0
    #else:
    #    if curveVal>-0.05: curveVal=0
    motor.move(0.06, curveVal, 0.01)
    #cv2.imshow("Image", img)
    #cv2.waitKey(1)

if __name__ == '__main__':
    while True:
        main()
