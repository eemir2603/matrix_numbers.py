import random
import time

# Harfler ve Sayılar Havuzu
karakterler = "0101010101HACKTHEPLANET01010101ADYTON"

print("MATRIX BAĞLANTISI KURULUYOR...")
time.sleep(1)

# SONSUZ DÖNGÜ (PC'yi yormaz, merak etme)
while True:
    # Ekrana rastgele karakterlerden oluşan bir satır bas
    satir = ""
    for i in range(10): # Her satırda 10 blok olsun
        secilen = random.choice(karakterler)
        satir += secilen + "  "
    
    print(satir)
    
    # Çok hızlı akmasın, gözümüz görsün (0.05 saniye bekle)
    time.sleep(0.05)
