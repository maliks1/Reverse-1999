import csv
import time
import pandas as pd
from google_play_scraper import Sort, reviews

APP_ID = 'com.bluepoch.m.en.reverse1999'
TARGET_COUNT = 20000
BATCH_SIZE = 500
OUTPUT_FILE = 'ulasan_aplikasi.csv'

def main():
    scrapreview = []
    print(f"Mulai mengambil ulasan untuk {APP_ID}...")

    # Batch pertama
    fetched_reviews, continuation_token = reviews(
        APP_ID,
        lang='en',          # Ulasan Bahasa Inggris
        country='us',       # Region US
        sort=Sort.NEWEST,   # Urutan ulasan terbaru
        count=BATCH_SIZE
    )
    scrapreview.extend(fetched_reviews)
    print(f"Berhasil mengambil {len(scrapreview)} ulasan...")

    # Fetching bertahap menggunakan continuation token
    while len(scrapreview) < TARGET_COUNT and continuation_token:
        time.sleep(0.5)
        fetched_reviews, continuation_token = reviews(
            APP_ID,
            continuation_token=continuation_token
        )
        if not fetched_reviews:
            break
        scrapreview.extend(fetched_reviews)
        print(f"Berhasil mengambil {len(scrapreview)} ulasan...")

    # Membatasi hasil tepat 100.000 data
    scrapreview = scrapreview[:TARGET_COUNT]
    
    # Menyimpan ke CSV
    df = pd.DataFrame(scrapreview)
    df.to_csv(OUTPUT_FILE, index=False, encoding='utf-8')
    print(f"\nSelesai! Total {len(df)} ulasan disimpan ke '{OUTPUT_FILE}'.")

if __name__ == '__main__':
    main()