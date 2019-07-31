from subprocess import call
call("sudo pigpiod", shell=True)
import pygame
import RPi.GPIO as GPIO
import pigpio
import time

GPIO.setmode(GPIO.BOARD)
pi = pigpio.pi()

ESC_GPIO = 17 #GPIO17 - 11pin
ESC_PWM_MIN = 1470
ESC_PWM_MAX = 1530

pygame.init()
clock = pygame.time.Clock()
pygame.joystick.init()

print("ESC Calibration...")

pi.set_servo_pulsewidth(ESC_GPIO, ESC_PWM_MAX)
print("PWM_MAX...")
print(pi.get_servo_pulsewidth(ESC_GPIO))
time.sleep(1.5)

pi.set_servo_pulsewidth(ESC_GPIO, ESC_PWM_MIN)
print("PWM_MIN...")
print(pi.get_servo_pulsewidth(ESC_GPIO))
time.sleep(1.5)
	
pi.set_servo_pulsewidth(ESC_GPIO, 0)
print("Calibration Complete!")
time.sleep(1)
