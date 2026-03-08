#!/usr/bin/env python3

def main():
    original = [2, 8, 9, 48, 8, 22, -12, 2]
    # Önce filtrele ve 2 ekle, sonra set() ile tekrarları kaldırmamız gerekir
    res = {x + 2 for x in original if x > 5}
    
    print(original)
    print(res)

if __name__ == "__main__":
    main()
