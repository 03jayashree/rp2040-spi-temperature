import machine
import utime

# Initialize the internal temperature sensor (ADC channel 4)
sensor_temp = machine.ADC(4)

# Conversion factor to convert raw ADC reading (0–65535) to voltage (0–3.3V)
conversion_factor = 3.3 / 65535

while True:
    # Read raw 16-bit ADC value and convert it to voltage
    reading = sensor_temp.read_u16() * conversion_factor

    # Convert voltage to temperature in Celsius using RP2040's formula:
    # Vbe = 0.706V at 27°C, slope = -1.721 mV per °C
    temperature = 27 - (reading - 0.706) / 0.001721

    # Print the temperature value to the console
    print(temperature)

    # Wait for 2 seconds before the next reading
    utime.sleep(2)
