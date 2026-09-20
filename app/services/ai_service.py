import os
import requests


class AIServiceError(Exception):
    pass


class AIService:
    def yanit_uret(self, mesaj, gecmis=None):
        api_key = os.getenv("GROQ_API_KEY")

        if not api_key:
            return "Demo modu: Yapay zekâ API anahtarı henüz tanımlanmadı."

        messages = [
            {
                "role": "system",
                "content": (
                    "Sen SESİZ projesinin yapay zekâ destekli bilgilendirme asistanısın. "
"SESİZ, görme engelli bireylerin günlük yaşamını desteklemeyi amaçlayan bir yardımcı teknoloji projesidir. "
"Metin okuma, nesne tanıma ve sesli komut özellikleri planlanan özelliklerdir; bunları tamamlanmış ürün özellikleri gibi sunma. "
"Türkçe, kısa, açık ve saygılı yanıt ver. Giyim, aksesuar, fiyat, satış tarihi veya doğrulanmamış özellikler uydurma. "
"Bilmediğin konularda kesin bilgi veremediğini söyle ve gerekirse ziyaretçiyi iletişim formuna yönlendir."
                )
            }
        ]

        if gecmis:
            messages.extend(gecmis)

        messages.append({"role": "user", "content": mesaj})

        try:
            response = requests.post(
                "https://api.groq.com/openai/v1/chat/completions",
                headers={
                    "Authorization": f"Bearer {api_key}",
                    "Content-Type": "application/json"
                },
                json={
                    "model": "openai/gpt-oss-120b",
                    "messages": messages
                },
                timeout=30
            )

            response.raise_for_status()
            return response.json()["choices"][0]["message"]["content"]

        except (requests.RequestException, KeyError, IndexError, ValueError) as hata:
            raise AIServiceError(f"Yapay zekâ hatası: {hata}") from hata

ai_service = AIService()
