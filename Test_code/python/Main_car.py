
import pygame
from MotorModule_new import Motor

pygame.init()

joystick = pygame.joystick.Joystick(0)
joystick.init()
motor = Motor(10, 9, 11, 17, 22, 27, 14, 15, 18)
prev_x, prev_y = joystick.get_axis(0), joystick.get_axis(1)

# Main Loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.JOYBUTTONDOWN:
            if event.button == 0:
                print("button 0 down")
                motor.move(0.6, 0, 0.1)
            elif event.button == 1:
                print("button 1 down")
                motor.move(-0.6, 0, 0.1)
            elif event.button == 2:
                print("button 2 down")
                motor.move(0, -0.8, 0.1)
            elif event.button == 3:
                print("button 3 down")
                motor.move(0, 0.8, 0.1)
            elif event.button == 5:
                print("button 5 down")
            elif event.button == 6:
                print("button 6 down")
            elif event.button == 7:
                print("button 7 down")
            elif event.button == 8:
                print("button 8 down")

    x, y = joystick.get_axis(0), joystick.get_axis(1)
    if x != prev_x or y != prev_y:
        if abs(x) > abs(y) and abs(x) > 0.15:
            y = 0
            print(f"Joystick values: x={x}, y={y}")
            motor.move(y*0.4, x*0.4, 0.1)
        elif abs(y) > abs(x) and abs(y) > 0.15:
            x = 0
            print(f"Joystick values: x={x}, y={y}")
            motor.move(y*0.4 , x*0.4, 0.1)
        else:
            print(f"Joystick values: x={x}, y={y}")
            motor.move(0,  0, 0.1)
        prev_x, prev_y = x, y
