#!/usr/bin/env python3

def find_the_redheads(family_dict):
    # filter(fonksiyon, veri_grubu) yapısını kullanıyoruz
    # Sadece değeri "red" olan anahtarları (isimleri) filtreliyoruz
    redheads = filter(lambda name: family_dict[name] == "red", family_dict)
    return list(redheads)

# Test kısmı
if __name__ == "__main__":
    dupont_family = {
        "florian": "red",
        "marie": "blond",
        "virginie": "brunette",
        "david": "red",
        "franck": "red"
    }
    print(find_the_redheads(dupont_family))

#lambda tek ifadeyi hesaplar ve geri döndürür.
#filter ise zaten filtrelem olur 

