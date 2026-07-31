# Mengimpor pustaka google_play_scraper untuk mengakses ulasan dan informasi aplikasi dari Google Play Store.
from google_play_scraper import app, reviews_all, Sort
# Mengambil semua ulasan dari aplikasi dengan ID 'com.byu.id' di Google Play Store.
# Proses scraping mungkin memerlukan beberapa saat tergantung pada jumlah ulasan yang ada.
scrapreview = reviews_all(
    'com.bluepoch.m.en.reverse1999',  # ID aplikasi
    lang='id',                        # Bahasa ulasan (default: 'en')
    country='id',                     # Negara (default: 'us')
    sort=Sort.NEWEST,            # Urutan ulasan (default: Sort.MOST_RELEVANT)
    count=10000                       # Jumlah maksimum ulasan yang ingin diambil
)

# Menyimpan ulasan dalam file CSV
import csv

with open('ulasan_aplikasi.csv', mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(['Review']) # Menulis header kolom
    for review in scrapreview:
        writer.writerow([review['content']])    # Menulis konten ulasan ke dalam file CSV