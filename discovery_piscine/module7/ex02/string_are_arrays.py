#!/usr/bin/env python3
import sys

if len(sys.argv) != 2:
    print("none")
else:
    text = sys.argv[1]
    # Sadece küçük 'z' harflerini bul
    result = ""
    for char in text:
        if char == 'z':
            result += "z"
            
    if result == "":
        print("none")
    else:
        print(result)
#bir karakteri bir listenin elemanıymış gibi döngüye sokarız ve sadece 'z' olanları yan yana yazdırırız.
