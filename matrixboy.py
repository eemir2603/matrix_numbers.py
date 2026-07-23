import random
import time

# Words and Numbers
characters = "0101010101HACKTHEPLANET01010101ADYTON"

print("Connection Establishing...")
time.sleep(1)

# LOOP
while True:

    satir = ""
    for i in range(10): 
        secilen = random.choice(karakterler)
        satir += secilen + "  "
    
    print(satir)
    
    time.sleep(0.05)
