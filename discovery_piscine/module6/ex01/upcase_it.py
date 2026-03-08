#!/usr/bin/env python3
import sys

# Sadece 1 parametre (sys.argv[0] hariç) bekleniyor
if len(sys.argv) != 2:
    print("none")
else:
    print(sys.argv[1].upper())

