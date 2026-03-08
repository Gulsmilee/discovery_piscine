#!/usr/bin/env python3
import sys
#Kaç tane argüman geldiğini yazar, sonra for döngüsü ile her birinin uzunluğunu (len) ekrana basar.
if len(sys.argv) < 2:
    print("none")
else:
    params = sys.argv[1:]
    print(f"parameters: {len(params)}")
    for p in params:
        print(f"{p}: {len(p)}")
