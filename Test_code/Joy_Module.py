# We use Pygame to access the Xbox One Controller
import pygame
from time import sleep
from pygame.constants import JOYBUTTONDOWN
from MotorModule_new import Motor
pygame.init()

joysticks = []
for i in range(0, pygame.joystick.get_count()):
    joysticks.append(pygame.joystick.Joystick(i))
    joysticks[-1].init()

# Print out the name of the controller
print(pygame.joystick.Joystick(0).get_name())

# Xbox Joystick Axis:
# Axis 0 up down, down value is -1, up value is 1
# Axis 1 Left, Right, Left value is: -1, right value is 1
# center is always 0

##################
motor= Motor(2,3,4,17,22,27,14,15,18)
####################

# Main Loop
while True or KeyboardInterrupt:

    # Check for joystick events
    for event in pygame.event.get():
        if event.type ==JOYBUTTONDOWN:
            if event.button == 0:
                print("button 0 down")
                motor.move(0.6,0,0.1)
            if event.button == 1:
                print("button 1 down")
                motor.move(-0.6,0,0.1)
            if event.button == 2:
                print("button 2 down")
                motor.move(0,-0.8,0.1)
            if event.button == 3:
                print("button 4 down")
                motor.move(0,0.8,0.1)
            if event.button == 5:
                print("button 5 down")
            if event.button == 6:
                print("button 6 down")
            if event.button == 7:
                print("button 7 down")
            if event.button == 8:
                print("button 8 down")
            else:
                print("car isn't moving")
                motor.stop(0.1)
        if event.type == pygame.JOYAXISMOTION:
            if event.axis < 2: # Left stick
                if event.axis == 0: # left/right
                    if event.value < -0.5:
                        print("left")
                        motor.move(0,0.8,0.1)
                    if event.value > 0.5:
                        print("right")                        
                        motor.move(0,-0.8,0.1)
                if event.axis == 1: # up/down
                    if event.value < -0.5:
                        print("up")
                        motor.move(0.6,0,0.1)
                    if event.value > 0.5:
                        print("down")
                        motor.move(-0.6,0,0.1)
