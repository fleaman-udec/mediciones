import time
import board
import busio
import adafruit_msa301

i2c = busio.I2C(scl=board.GP1, sda=board.GP0)
msa = adafruit_msa301.MSA301(i2c)
msa.data_rate = adafruit_msa301.DataRate.RATE_125_HZ

count = 1
while count < 20:
    count += 1
    print(msa.acceleration)
    time.sleep(0.1)
