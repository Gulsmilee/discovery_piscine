#!/usr/bin/env python3


def array_of_names(persons):
    full_names = []
    # Sözlükteki anahtar (isim) ve değer (soyisim) üzerinde dönüyoruz
    for first_name, last_name in persons.items():
        # İlk harfleri büyütüp (capitalize) birleştiriyoruz
        full_name = f"{first_name.capitalize()} {last_name.capitalize()}"
        full_names.append(full_name)
    return full_names

# Test kısmı
if __name__ == "__main__":
    persons = {
        "jean": "valjean",
        "grace": "hopper",
        "xavier": "niel",
        "fifi": "brindacier"
    }
    print(array_of_names(persons))

#capitalize demek ilk değerin değerli olduğunu diğer değerlerin değersiz olarak algılıyor.
