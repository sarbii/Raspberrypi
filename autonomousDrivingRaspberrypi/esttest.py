from subprocess import call
call("sudo pigpiod", shell=True)
import pygame
import RPi.GPIO as GPIO
import pigpio
import time

GPIO.setmode(GPIO.BOARD)
pi = pigpio.pi()

ESC_GPIO = 17 #GPIO17 - 11pin

ESC_PWM_MIN = 1462
ESC_PWM_MAX = 1542

clock = pygame.time.Clock()

print("ESC test...")
pi.set_servo_pulsewidth(ESC_GPIO, ESC_PWM_MIN)
time.sleep(0.1)
pi.set_servo_pulsewidth(ESC_GPIO, 1470)
time.sleep(0.1)
pi.set_servo_pulsewidth(ESC_GPIO, 1480)
time.sleep(0.1)
pi.set_servo_pulsewidth(ESC_GPIO, 1490)
time.sleep(0.1)
pi.set_servo_pulsewidth(ESC_GPIO, 1500)
time.sleep(0.1)
pi.set_servo_pulsewidth(ESC_GPIO, 1510)
time.sleep(0.1)
pi.set_servo_pulsewidth(ESC_GPIO, 1520)
time.sleep(0.1)
pi.set_servo_pulsewidth(ESC_GPIO, 1530)
time.sleep(0.1)
pi.set_servo_pulsewidth(ESC_GPIO, ESC_PWM_MAX)
time.sleep(0.1)
pi.set_servo_pulsewidth(ESC_GPIO, 0)

print("Test Complete!")
time.sleep(1)
