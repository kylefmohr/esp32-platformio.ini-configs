# esp32-platformio.ini-configs
With the wide variety of configurations available for ESP32 variants (S2, S3, C3, C6, H2, etc) microcontrollers [it has become increasingly difficult to use these boards with PlatformIO/the ESP32 Arduino core](https://github.com/platformio/platform-espressif32/issues/1225), as programs will compile fine, but won't actually work unless you specify the correct amount of flash the board has, whether it has PSRAM, whether that Flash/PSRAM is QSPI or Octal, etc. etc. 

This repo aims to collect working configurations for ESP32 variant boards. 
