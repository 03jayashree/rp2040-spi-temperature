# rp2040-spi-temperature
This project demonstrates how to use the RP2040’s PIO (Programmable I/O) as an SPI slave to transmit internal temperature sensor data to a master device. It is written in MicroPython, and developed using Thonny IDE on a Raspberry Pi Pico demoboard.
<h2>Table of Contents</h2>
  <li><a href="#introduction">Introduction to RP2040 Microcontroller</a></li>
<h2>1-Introduction to RP2040 Microcontroller</h2>
The RP2040 is a 32-bit dual-core ARM Cortex-M0+ microcontroller designed by Raspberry Pi, known for its high performance, low cost, and ease of use, featuring a rich set of peripherals and unique Programmable I/O (PIO) subsystem. 
<h3>Key Features</h3>
- **Dual-core ARM Cortex-M0+** @ 133MHz  
- **264kB SRAM** (6 banks), up to **16MB external QSPI Flash** with XIP  
- **DMA controller**, **USB 1.1** with host/device support  
- **30 multi-function GPIO** (4 ADC capable), **12-bit 500ksps ADC**  
- **2x UART**, **2x SPI**, **2x I2C**, **16 PWM channels**  
- **8 PIO state machines** for flexible, user-defined interfaces (VGA, SD, etc.)  
- **Operates at 3.3V** IO logic level


