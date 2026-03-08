#!/usr/bin/env python3
import sys

# 1. Metodu tanımla (ödevin şartı)
def downcase_it(metin):
    return metin.lower()

# 2. Terminalden gelen kelimeleri kontrol et
# sys.argv[1:] dosya isminden sonraki tüm kelimeleri bir liste yapar
parametreler = sys.argv[1:]

if not parametreler:
    # Eğer liste boşsa "none" yazdır
    print("none")
else:
    # Listedeki her kelimeyi metodumuza gönderip yazdır
    for kelime in parametreler:
        print(downcase_it(kelime))

