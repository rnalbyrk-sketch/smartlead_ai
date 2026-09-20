import os
import hmac
from flask import Blueprint, jsonify, request, render_template, session, redirect, url_for
from app.database import tum_leadler, lead_ekle
from app.services.ai_service import ai_service, AIServiceError
main_bp = Blueprint("main", __name__)


@main_bp.route("/health")
def health():
    return jsonify({"durum": "calisiyor"})

@main_bp.route("/")
def ana_sayfa():
    return render_template("index.html")

@main_bp.route("/api/sohbet", methods=["POST"])
def sohbet():
    veri = request.get_json(silent=True) or {}
    mesaj = veri.get("mesaj", "").strip()

    if not mesaj:
        return jsonify({
            "basari": False,
            "hata": "Mesaj boş olamaz."
        }), 400

    try:
        yanit = ai_service.yanit_uret(mesaj)
    except AIServiceError:
        return jsonify({
            "basari": False,
            "hata": "Yapay zekâ servisine şu anda ulaşılamıyor. Lütfen tekrar deneyin."
        }), 503

    return jsonify({
        "basari": True,
        "yanit": yanit
    })

@main_bp.route("/api/leads", methods=["POST"])
def yeni_lead():
    veri = request.get_json(silent=True) or {}

    isim = str(veri.get("isim") or "").strip()
    telefon = str(veri.get("telefon") or "").strip()
    mesaj = str(veri.get("mesaj") or "").strip()

    if not isim or not telefon:
        return jsonify({
            "basari": False,
            "hata": "İsim ve telefon zorunludur."
        }), 400

    lead_ekle(isim, telefon, mesaj)

    return jsonify({
        "basari": True,
        "mesaj": "Müşteri talebi kaydedildi."
    }), 201
@main_bp.route("/dashboard")
def dashboard():
    if not session.get("admin_giris"):
        return redirect(url_for("main.admin_giris"))

    leadler = tum_leadler()
    return render_template("dashboard.html", leadler=leadler)
@main_bp.route("/admin/login", methods=["GET", "POST"])
def admin_giris():
    if request.method == "POST":
        kullanici = request.form.get("kullanici", "")
        sifre = request.form.get("sifre", "")

        dogru_kullanici = os.environ.get("ADMIN_USERNAME")
        dogru_sifre = os.environ.get("ADMIN_PASSWORD")

        if (
            dogru_kullanici
            and dogru_sifre
            and hmac.compare_digest(kullanici, dogru_kullanici)
            and hmac.compare_digest(sifre, dogru_sifre)
        ):
            session.clear()
            session["admin_giris"] = True
            return redirect(url_for("main.dashboard"))

        return render_template("login.html", hata="Kullanıcı adı veya şifre hatalı.")

    return render_template("login.html")

@main_bp.route("/admin/logout", methods=["POST"])
def admin_cikis():
    session.clear()
    return redirect(url_for("main.admin_giris"))
