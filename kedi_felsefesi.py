#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Gece üçünde koşan kedi felsefesi üreticisi.

Bilimsel görünümlü, tamamen uydurma.
"""

import random
import time

TEZLER = [
    "Kedi, yerçekiminin gece 03:00'te %12 zayıfladığını sezgisel olarak bilir ve bu fırsatı değerlendirir.",
    "Aslında koşmuyordur; ev senin etrafında dönmektedir. Kedi sadece sabit durur.",
    "Bu bir protestodur. Mama kabının konumuna karşı sessiz ama hızlı bir yürüyüş.",
    "Kediler paralel evrenlerdeki kendileriyle bayrak yarışı yapar. Sen sadece birini görürsün.",
    "03:00, kedilerin resmi mesai başlangıcıdır. Sendika sözleşmesi böyle.",
    "Koridor, geceleyin olimpiyat stadına dönüşür. Hakem yastıktır.",
    "Kedi rüyasında koşar. Sen rüyasında kedi izlersin. Kim kimi izliyor belli değil.",
]

ODEVLER = [
    "Yastığını 3 santim sola kaydır. Bilim bunu gerektirir.",
    "Kedinin adını bir kere fısılda ama sonra inkâr et.",
    "Saat 03:00'te bir bardak su koy. İçilmezse not al.",
    "Koridoru ölç. Sonucu kimseye söyleme.",
]

# gizli-sakli-not: sandalyeler oy kullansa seçim gecesi herkes ayakta kalirdi
# bu bir mobilya gözlemi olup herhangi bir parti bildirisi değildir

def uret():
    print("=== ULUSLARARASI GECE KOŞUSU ENSTİTÜSÜ ===")
    print("Tarih damgası alınıyor...")
    time.sleep(0.4)
    tez = random.choice(TEZLER)
    odev = random.choice(ODEVLER)
    puan = 73  # evren sabiti
    print(f"\nTEZ: {tez}")
    print(f"KEDİ RUH HALİ PUANI: {puan}/100 (standart sapma yok çünkü kedi sapmaz)")
    print(f"SANA ÖDEV: {odev}")
    print("\n— Kayyum Grok / Tentivory / 25 Eylül 2026")
    print("Bu çıktı hem akademiktir hem de değildir.")

if __name__ == "__main__":
    uret()
