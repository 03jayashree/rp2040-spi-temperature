### Introduction to Micropython
MicroPython is a lightweight implementation of Python 3 designed specifically for microcontrollers and embedded systems. It allows you to write Python code to control hardware like sensors, displays, motors, etc., on boards like the Raspberry Pi Pico, ESP32, and Arduino-compatible boards. You get an interactive prompt (the REPL) to execute commands immediately via USB Serial, and a built-in filesystem. The Pico port of MicroPython includes modules for accessing low-level chip-specific hardware.
### Installing MicroPython on a Pico-series Device
Follow these steps to install MicroPython on any pico series demoboard:
1. **Download the Firmware**  
   Visit the official Raspberry Pi documentation and download the MicroPython `.uf2` file for your board:  
   [👉 MicroPython Firmware Download](https://www.raspberrypi.com/documentation/microcontrollers/micropython.html)
2. **Enter BOOTSEL Mode**  
   - Unplug your Pico from any power source.  
   - Hold down the **BOOTSEL** button.  
   - While holding it, plug the Pico into your computer via USB.
3. **Upload the Firmware**  
   - A new drive named **RPI-RP2** will appear.  
   - Drag and drop the `.uf2` file onto this drive.
4. **Automatic Reboot**  
   - The board will reboot automatically and launch MicroPython.
### Connecting to the MicroPython REPL over USB
You can access the MicroPython REPL (Read-Eval-Print Loop) directly from your Raspberry Pi using the USB serial interface:
1.Connect your Raspberry Pi Pico via USB.
2.Check the serial port:
```bash ls /dev/tty* ```



