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
For the complete code refer to `test_code`.

## 1.5. Micropython SPI
Refer to `spi_example.py`

### **Constructors**

- *class* **machine.SPI**(*id, ...*):Construct an SPI object on the given bus, id. Values of id depend on a particular port and its hardware. Values 0, 1, etc. are commonly used to select hardware SPI block #0, #1, etc.
- *class* **machine.SoftSPI**(*baudrate=1000000,polarity=0, phase=0, bits=8, firstbit=MSB, sck=None, mosi=None, miso=None*):Construct a new software SPI object. Additional parameters must be given, usually at least sck, mosi and miso, and these are used to initialise the bus.

### **Methods**

- **SPI.init**(*baudrate=1000000, *, polarity=0, phase=0, bits=8, firstbit=SPI.MSB, sck=None, mosi=None, miso=None*)
Initialise the SPI bus with the given parameters:
   - `baudrate` is the SCK clock rate.
   - `polarity` can be 0 or 1, and is the level the idle clock line sits at.
   - `phase` can be 0 or 1 to sample data on the first or second clock edge respectively.
   - `bits` is the width in bits of each transfer. Only 8 is guaranteed to be supported by all hardware.
   - firstbit can be SPI.MSB or SPI.LSB.
   - `sck`, `mosi`, `miso` are pins (machine.Pin) objects to use for bus signals. For most hardware SPI blocks (as selected by `id` parameter to the constructor), 
      pins are fixed and cannot be changed. In some cases, hardware blocks allow 2-3 alternative pin sets for a hardware SPI block. Arbitrary pin assignments are 
      possible only for a bitbanging SPI driver (`id` = -1).
- **SPI.deinit**():Turn off the SPI bus.
- **SPI.read**(*nbytes, write=0x00*):Read a number of bytes specified by `nbytes` while continuously writing the single byte given by `write`. Returns a `bytes` object with the data that was read.
- **SPI.readinto**(*buf, write=0x00*):Read into the buffer specified by `buf` while continuously writing the single byte given by `write`. Returns `None`.
- **SPI.write**(*buf*):Write the `bytes` contained in buf. Returns `None`.
- **SPI.write_readinto**(*write_buf,read_buf*):Write the bytes from `write_buf` while reading into `read_buf`. The buffers can be the same or different, but both buffers must have the same length. Returns `None`.
### **Constants**

- **SPI.MSB** / **SoftSPI.MSB**:Set the first bit to be the most significant bit
- **SPI.LSB** / **SoftSPI.LSB** :Set the first bit to be the least significant bit

```bash 
NOTE:The above class is only for SPI Master.The RP2040 doesn’t have built-in support for SPI slave in MicroPython, so trying to use it that way doesn’t work well—MicroPython alone can’t keep up with the exact timing SPI needs. PIO (Programmable I/O) solves this by handling the SPI signals (like clock and data) at the hardware level, with precise timing. It works alongside MicroPython, which takes care of logic and processing. So, by combining PIO and MicroPython, we can get a reliable SPI slave setup that the RP2040 couldn’t do with MicroPython alone.
```

  














