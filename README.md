# SmartLead AI – SESİZ

SESİZ için geliştirilmiş yapay zekâ destekli satış asistanı.

## Özellikler

* Ziyaretçilerin sorularını Groq API üzerinden yapay zekâ ile yanıtlar.
* İletişim formundan müşteri taleplerini toplar.
* Talepleri SQLite veritabanına kaydeder.
* Yönetici girişinden sonra müşteri kayıtlarını görüntüler.

## Kullanılan Teknolojiler

Python, Flask, SQLite, Groq API, Wix ve Render.

## Canlı Bağlantılar

* Wix sitesi: https://malbyrk.wixsite.com/sesiz
* Canlı asistan: https://smartlead-ai-suj3.onrender.com
* Yönetici girişi: https://smartlead-ai-suj3.onrender.com/admin/login

## Yerel Çalıştırma

1. `pip install -r requirements.txt`
2. `.env` dosyasında gerekli ortam değişkenlerini tanımlayın.
3. `python run.py` komutunu çalıştırın.

**Güvenlik:** API anahtarları ve yönetici şifreleri GitHub'a yüklenmemelidir.
