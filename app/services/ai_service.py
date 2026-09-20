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
                    "Sen SESİZ markasının akıllı satış asistanısın. "
                    "Ziyaretçilerin sorularını Türkçe, nazik ve kısa yanıtla. "
                    "Bilmediğin ürün özelliklerini veya fiyatları uydurma. "
                    "Gerekirse ziyaretçiyi iletişim formunu doldurmaya yönlendir."
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