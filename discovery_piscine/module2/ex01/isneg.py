#!/usr/bin/env python3
import sys

try:
	line = input()
	num = int(line)
	if num< 0:
		print("This number is negative.")
	elif num>0:
		print("This number is positive.")
	else:
		print("This number is both positive and negative.")
except EOFError:
    pass
except ValueError:
    # Sayı dışında bir şey girilirse hata vermemesi için
    pass
