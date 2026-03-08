#!/usr/bin/env python3
import sys

if len(sys.argv) != 3:
    print("none")
else:
    try:
        start = int(sys.argv[1])
        end = int(sys.argv[2])
        
        # range(start, end + 1) bize start'tan end'e kadar (dahil) sayıları verir
        res = list(range(start, end + 1))
        print(res)
    except ValueError:
        print("none")
#İki sayı alır ve aradaki tüm sayıları içeren bir liste (array) oluşturur. range(başlangıç, bitiş + 1) mantığı kullanılır.
