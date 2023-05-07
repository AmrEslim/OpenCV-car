from MotorModule_new import Motor
import KeyModule as kp

##################
motor= Motor(2,3,4,17,22,27,14,15,18)
####################

kp.init()	
	
 
def main():
	if kp.getKey('s'):
		motor.move(0.6,0,0.1)
	elif kp.getKey('w'):
		motor.move(-0.6,0,0.1)
	elif kp.getKey('a'):
	    motor.move(0,-0.8,0.1)
	elif kp.getKey('d'):
	    motor.move(0,0.8,0.1)
	else:
		motor.stop(0.1)
	
	
	
	
	
 
if __name__ == '__main__':
    while True:
        main()
