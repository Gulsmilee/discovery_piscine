#!/usr/bin/env python3
import sys

# sys.argv[0] her zaman programın kendi ismidir (aff_first_param.py)
# sys.argv[1] ise  yazdığım İLK parametredir.

# Önce parametre girilmiş mi diye kontrol ediyoruz (uzunluk 1'den büyük mü?)
if len(sys.argv) > 1:
    # Eğer varsa, ilk parametreyi (indeks 1) yazdır
    print(sys.argv[1])
else:
    # Eğer hiç parametre yoksa "none" yazdır
    print("none")
