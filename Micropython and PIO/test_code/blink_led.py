from machine import Pin      # Import Pin class to control GPIO pins
from time import sleep       # Import sleep to add delay

led = Pin(25, Pin.OUT)       # Initialize GPIO pin 25 as output (onboard LED on Pico)

while True:                  # Infinite loop
    led.toggle()             # Toggle the LED state (ON to OFF or OFF to ON)
    sleep(0.5)               # Wait for 0.5 seconds before toggling again
