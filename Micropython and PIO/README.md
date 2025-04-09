# 1.Introduction to Micropython
MicroPython is a lightweight implementation of Python 3 designed specifically for microcontrollers and embedded systems. It allows you to write Python code to control hardware like sensors, displays, motors, etc., on boards like the Raspberry Pi Pico, ESP32, and Arduino-compatible boards. You get an interactive prompt (the REPL) to execute commands immediately via USB Serial, and a built-in filesystem. The Pico port of MicroPython includes modules for accessing low-level chip-specific hardware.

## 1.1.Installing MicroPython on a Pico-series Device
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
     
## 1.2. Connecting to the MicroPython REPL over USB
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
 ## 1.3. Supported Features of MicroPython

### 1. REPL Access
- **REPL over USB and UART (GP0/GP1):**  
  Interact with your board in real-time via USB or UART. Useful for debugging, testing, and live coding.

### 2. Filesystem
- **1600 kB `littlefs2` Filesystem:**  
  The onboard flash is formatted with `littlefs2`, allowing storage of scripts, logs, and configuration files.

### 3. `utime` Module
Provides basic time-related utilities:
- `sleep(seconds)` – Pause execution.
- `ticks_ms()` / `ticks_us()` – Retrieve system ticks for timing.

### 4. `ubinascii` Module
Utility for encoding and decoding:
- `hexlify(data)` – Convert binary data to hexadecimal.
- `unhexlify(hex_str)` – Convert hexadecimal strings back to bytes.

### 5. `machine` Module – Direct Hardware Control

#### 5.1. `machine.Pin`
- Use GPIOs as digital input/output.

#### 5.2. `machine.Timer`
- Schedule functions to run at regular intervals or after delays.

#### 5.3. `machine.ADC`
- Read analog voltages from pins (e.g., sensors or potentiometers).

#### 5.4. `machine.I2C` / `machine.SoftI2C`
- Communicate with I2C peripherals.
- `SoftI2C` enables flexible pin usage for SDA and SCL.

#### 5.5. `machine.SPI` / `machine.SoftSPI`
- Communicate with SPI devices like SD cards or shift registers.
- `SoftSPI` allows using any GPIO pins.

#### 5.6. `machine.WDT`
- Watchdog Timer resets the device automatically if the code becomes unresponsive.

#### 5.7. `machine.PWM`
- Generate PWM signals to control devices like LEDs, motors, and servos.

#### 5.8. `machine.UART`
- Use UART for asynchronous serial communication.

## 1.4. ADC
An analogue-to-digital converter (ADC) measures some analogue signal and encodes it as a digital number. The ADC on RP-series microcontrollers measures voltages.

The ADC on RP2040 has a resolution of 12-bits, meaning that it can transform an analogue signal into a digital signal as a number ranging from 0 to 4095 – though this is handled in MicroPython transformed to a 16-bit number ranging from 0 to 65535, so that it behaves the same as the ADC on other MicroPython microcontrollers.

RP2040 have five ADC channels total, four of which are brought out to chip GPIOs: GP26, GP27, GP28 and GP29. On Pico, the first three of these are brought out to GPIO pins, and the fourth can be used to measure the VSYS voltage on the board.

The ADC’s fifth input channel is connected to a temperature sensor built into RP2040.

You can specify which ADC channel you’re using by pin number:
```bash
adc = machine.ADC(26) # Connect to GP26, which is channel 0
```
or by channel:
```bash
adc = machine.ADC(4) # Connect to the internal temperature sensor
adc = machine.ADC(0) # Connect to channel 0 (GP26)
```
For the temp. redaing code refer to `test_code`.




