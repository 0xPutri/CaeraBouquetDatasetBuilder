# CaeraBouquetDatasetBuilder – Florist Recommendation System

Generator dataset profesional untuk sistem rekomendasi bouquet bunga. Dataset ini digunakan untuk keperluan pengembangan Machine Learning pada proyek **Web-based Bouquet Ordering System with Recommendation Feature**.

> Dataset yang dihasilkan menyelaraskan katalog produk riil dengan simulasi perilaku pengguna dan interaksi terhadap produk.

## Tujuan

Repository ini dibuat untuk menghasilkan dataset yang akurat untuk kebutuhan:

- eksperimen sistem rekomendasi
- simulasi perilaku pengguna
- pengembangan dan pengujian model machine learning

Dataset dibuat berdasarkan katalog produk bisnis riil dan distribusi probabilitas yang dapat dikonfigurasi sehingga pola interaksi tetap realistis.

## Struktur Project

```
../CaeraBouquetDatasetBuilder
├── config
│   └── distributions.py
├── data
│   └── generated
├── generate_dataset.py
├── generators
│   ├── interactions.py
│   ├── products.py
│   └── users.py
└── utils
    └── sampling.py
```

## Cara Menjalankan Generator

1. Install dependency terlebih dahulu.
   
   ```bash
   pip install -r requirements.txt
   ```

2. Jalankan script generator:
   
   ```bash
   python generate_dataset.py
   ```

3. Setelah dijalankan, dataset akan tersimpan pada folder:
   
   ```
   data/generated/
   ```

Output yang dihasilkan:

```
products.csv
users.csv
interactions.csv
```

## Catatan

Dataset ini mengintegrasikan data produk bisnis nyata. Simulasi interaksi dan pengguna dirancang untuk membantu validasi dan pengujian sistem rekomendasi agar sesuai dengan kondisi operasional di lapangan.

## Lisensi

Digunakan untuk keperluan akademik dan penelitian.