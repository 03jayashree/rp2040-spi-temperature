### Introduction to Micropython
MicroPython is a lightweight implementation of Python 3 designed specifically for microcontrollers and embedded systems. It allows you to write Python code to control hardware like sensors, displays, motors, etc., on boards like the Raspberry Pi Pico, ESP32, and Arduino-compatible boards. You get an interactive prompt (the REPL) to execute commands immediately via USB Serial, and a built-in filesystem. The Pico port of MicroPython includes modules for accessing low-level chip-specific hardware.
### Installing MicroPython on a Pico-series Device
Follow these steps to install MicroPython on any pico series demoboard:
1. **Download the Firmware**  
   Visit the official Raspberry Pi documentation and download the MicroPython `.uf2` file for your board:  
   [MicroPython Firmware Download](https://www.raspberrypi.com/documentation/microcontrollers/micropython.html)
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
1. **Connect your Raspberry Pi Pico** via the micro USB port.
2. **Check available serial devices**:

    ```bash
   ls /dev/tty*
   ```
   Look for a device like `/dev/ttyACM0`. To confirm, unplug and replug the Pico and observe which device disappears/reappears.
3. **Install `minicom`**:

   ```bash
   sudo apt install minicom
   ```
4. **Open the REPL using `minicom`**:

   ```bash
   minicom -o -D /dev/ttyACM0
   ```
5. **Interact with the REPL**:
   Press `Enter` a few times until you see the `>>>` prompt.
   If you press `CTRL-D` on your keyboard whilst the `minicom` terminal is focused, you should see a message similar to this:

   ```bash
   MPY: soft reboot
   MicroPython v1.13-422-g904433073 on 2021-01-19; Raspberry Pi Pico with RP2040
   Type "help()" for more information.
   >>>
   ```
   It will display the firmware version and reload the REPL prompt.
6. **Say "Hello, Pico!"**:
   Once you're in the REPL, try typing your first Python command:
   ```python
   >>> print("Hello, Pico!")
   Hello, Pico!
   >>>
   ```
 ### Supported features of Micropython
 #### 1.REPL Access
- **REPL over USB and UART (GP0/GP1):**  
  Interact with your board in real-time via USB or UART. Useful for debugging, testing, and live coding.
 #### 2.Filesystem
- **1600 kB `littlefs2` Filesystem:**  
  The onboard flash is formatted with `littlefs2`, allowing file storage (scripts, logs, config files).
 #### 3.`utime` Module
 Provides basic time-related utilities:
- `sleep(seconds)` – Pause execution.
- `ticks_ms()` / `ticks_us()` – Retrieve system ticks for interval measurements.
 #### 4.`ubinascii` Module
 Utility for encoding and decoding:
- `hexlify(data)` – Converts binary data to hexadecimal.
- `unhexlify(hex_str)` – Converts hexadecimal string back to bytes.
#### 5.`machine` Module – Direct Hardware Control
   ##### 5.1.`machine.Pin`
   - Use GPIOs as digital input/output.
   ##### 5.2.`machine.Timer`
   - Schedule functions at intervals or delays.
   ##### 5.3.`machine.ADC`
   - Read analog voltages (e.g., potentiometers, sensors).
   ##### 5.4.`machine.I2C`/ `machine.SoftI2C`
   - Communicate with I2C peripherals.
   - `SoftI2C` allows using any GPIOs as SDA/SCL.
   ##### 5.5.`machine.SPI` / `machine.SoftSPI`







