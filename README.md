
🐍 Discovery Piscine: Python Journey

Bu depo, Python programlama diline giriş yaptığım ve temel seviyeden başlayarak daha karmaşık veri yapılarına kadar ilerlediğim Discovery Piscine modüllerini içermektedir. Toplam 9 modülde, algoritma mantığından sözlük yönetimine kadar birçok konuyu uygulamalı olarak çözdüm.
🚀 Yolculuk Özeti

Bu proje boyunca basit "Merhaba Dünya" kodlarından, gerçek hayat senaryolarını simüle eden veri işleme scriptlerine kadar bir gelişim izledim:
🔹 Temel Seviye (Module 00 - 04)

    Değişkenler ve Tipler: Python'da sayısal ve metinsel verilerle çalışma.

    Kontrol Akışı: if, else ve elif yapılarıyla karar mekanizmaları kurma.

    Döngüler: while ve for döngüleri ile tekrarlayan işlemleri yönetme.

🔹 Orta Seviye (Module 05 - 08)

    Fonksiyonlar: Kodun tekrar kullanılabilirliğini sağlayan metotlar yazma.

    Listeler ve Tuple'lar: Veri dizilerini saklama, ekleme ve çıkarma işlemleri.

    Hata Yönetimi: Programın çökmesini engelleyen try-except blokları.

🔹 Gelişmiş Temeller (Module 09)

    Sözlükler (Dictionaries): Anahtar-değer (key-value) ilişkisiyle veri depolama.

    Fonksiyonel Programlama: filter(), map() ve lambda ifadeleriyle verileri filtreleme.

    Sıralama Algoritmaları: sorted() fonksiyonu ile karmaşık veri yapılarını (iç içe geçmiş sözlükler) belirli kriterlere göre düzenleme.

📁 Klasör Yapısı

Proje, her modülün kendi içinde egzersizlere (ex00, ex01...) ayrıldığı düzenli bir yapıya sahiptir:
Plaintext

discovery_piscine/
├── module01/           # Temel giriş
├── ...
└── module09/           # Veri yapıları ve Filtreleme
    ├── ex01/           # Aile içi saç rengi filtreleme (filter & list)
    ├── ex02/           # Sınıf ortalaması hesaplama (sum & values)
    └── ex03/           # Tarihi kişilikleri doğum yılına göre sıralama (sorted & lambda)

🛠️ Nasıl Çalıştırılır?

Herhangi bir scripti çalıştırmak için terminale şu komutu yazmanız yeterlidir:
Bash

python3 module09/ex01/family_affairs.py
