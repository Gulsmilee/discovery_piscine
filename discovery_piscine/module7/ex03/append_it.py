#!/usr/bin/env python3
import sys

if len(sys.argv) < 2:
    print("none")
else:
    for param in sys.argv[1:]:
        # Eğer kelime zaten 'ism' ile bitmiyorsa
        if not param.endswith("ism"):
            print(f"{param}ism")
#Gelen kelimelerin sonu "ism" ile bitmiyorsa sonuna "ism" ekleyip yazdırırız
