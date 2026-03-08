#!/usr/bin/env python3
import sys
import re

if len(sys.argv) != 3:
    print("none")
else:
    keyword = sys.argv[1]
    text = sys.argv[2]
    # BURAYA DİKKAT: Alttaki satır else ile aynı hizada değil, 
    # tam olarak 4 boşluk içeride olmalı!
    matches = re.findall(keyword, text)
    
    if not matches:
        print("none")
    else:
        print(len(matches))
