#!/usr/bin/env python3

# Metot tanımı: 'name' parametresine varsayılan değer atıyoruz
def greetings(name="noble stranger"):
    # Gelen 'name' bir string (metin) mi kontrol et
    if isinstance(name, str):
        print(f"Hello, {name}.")
    else:
        # String değilse (mesela sayıysa) bu hatayı ver
        print("Error! It was not a name.")

# istediği test çağırmaları:
if __name__ == "__main__":
    greetings('Alexandra')
    greetings('Wil')
    greetings()    # Hiçbir şey yazmazsak varsayılanı kullanır
    greetings(42)  # Sayı yazarsak hata mesajı verir
