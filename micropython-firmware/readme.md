# esptool

## install esptool

```
python -m pip install esptool
```

## erase_flash

```
python -m esptool --chip esp32s2 --port COM9 --baud 921600 erase_flash
```

## write_flash

```
python -m esptool --chip esp32s2 --port COM9 --baud 921600 write_flash 0x1000 BPI-Leaf-S2_MicroPython_v1.19.1-dirty.bin
```
