# SPI based Digital Temperature Monitor using RP2040
This project demonstrates how to use the RP2040’s PIO (Programmable I/O) as an SPI slave to transmit internal temperature sensor data to a master device. It is written in MicroPython, and developed using Thonny IDE on a Raspberry Pi Pico demoboard.
<h2>Table of Contents</h2>
  <li><a href="#rp2040">Introduction to RP2040 Microcontroller</a></li>
  <li><a href="#raspberrypi">Introduction to Raspberry Pi</a></li>
<h2>1-Introduction to RP2040 Microcontroller</h2>
The RP2040 is a 32-bit dual-core ARM Cortex-M0+ microcontroller designed by Raspberry Pi, known for its high performance, low cost, and ease of use, featuring a rich set of peripherals and unique Programmable I/O (PIO) subsystem. 
<h3>1.1-Key Features</h3>

- **Dual-core ARM Cortex-M0+** @ 133MHz
- **264kB** of embedded **SRAM** in 6 banks
- 6 dedicated IO for **16MB** external **QSPI Flash** with **eXecute In Place (XIP)**
- **4 channel ADC with internal temperature sensor, 500ksps, 12-bit conversion**
- **30** multi-function General Purpose IO
- Dedicated hardware for commonly used peripherals
   - **2 UARTs**
   - **2 SPI** controllers
   - **16 PWM** channels
   - **USB 1.1 Host/Device**
     
- **8 Programmable IO** state machine for extended peripheral support
<h3>1.2-Block Diagram</h3>

![RP2040 Block Diagram](diagrams/rp2040_block_dia.png)
<h3>1.3-Pinout</h3>

![RP2040 Pinout](diagrams/rp2040_pinout.png)

For more details on GPIO pin functions and internal peripheral mappings, refer to the official [RP2040 Datasheet](https://datasheets.raspberrypi.com/rp2040/rp2040-datasheet.pdf).Each GPIO pin on the RP2040 is connected to various internal peripherals (like SPI,UART,I2C etc.) , offering high flexibility for custom I/O functions.SIO, PIO0 and PIO1 are connected to all GPIO pins and are controlled by software (or software controlled state machines) so can be used to implement
many functions.

<h2>Introduction to Raspberry Pi</h2>









