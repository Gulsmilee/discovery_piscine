#!/usr/bin/env python3
import sys

# En az 2 parametre (sys.argv[0] + en az 2 argüman = toplam 3)
if len(sys.argv) < 3:
    print("none")
else:
    # Parametreleri tersten döndür (sys.argv[0]'ı dahil etme)
    for param in reversed(sys.argv[1:]):
        print(param)
