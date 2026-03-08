#!/usr/bin/env python3

def famous_births(scientists_dict):
    # Sözlükteki öğeleri (items) doğum tarihine göre sıralıyoruz
    # x[1] içteki sözlüğü (değeri), x[1]['date_of_birth'] ise tarihi temsil eder
    sorted_scientists = sorted(scientists_dict.values(), key=lambda x: x['date_of_birth'])
    
    for person in sorted_scientists:
        print(f"{person['name']} is a great scientist born in {person['date_of_birth']}.")

# Test kısmı
if __name__ == "__main__":
    women_scientists = {
        "ada": { "name": "Ada Lovelace", "date_of_birth": "1815" },
        "cecilia": { "name": "Cecila Payne", "date_of_birth": "1900" },
        "lise": { "name": "Lise Meitner", "date_of_birth": "1878" },
        "grace": { "name": "Grace Hopper", "date_of_birth": "1906" }
    }
    famous_births(women_scientists)
#lambda genellikle bir veya daha fazla fonksiyonu argüman olarak alan veya bir veya daha fazla fonksiyon döndüren üst düzey
# fonksiyonlarla birlikte kullanılır.
#values de ise direk kelimeyi alabilmek için yani sözcükdeki isimleri boşverir
#sorted fonksiyou listeyi veya sözlüğü sıralar
