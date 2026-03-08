#!/usr/bin/env python3

def main():
    original = [2, 8, 9, 48, 8, 22, -12, 2]
    # List Comprehension kullanarak filtreleme ve işlem yapma kısmını yaptık sadece 5 den buyuk olan sayılara iki ekleme
    new_array = [x + 2 for x in original if x > 5]
    
    print(original)
    print(new_array)

if __name__ == "__main__":
    main()
