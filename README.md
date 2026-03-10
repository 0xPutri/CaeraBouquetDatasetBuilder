# CaeraBouquetDatasetBuilder – Florist Recommendation System

Generator dataset sintetis untuk simulasi sistem rekomendasi bouquet bunga. Dataset ini digunakan untuk keperluan eksperimen Machine Learning pada proyek **Web-based Bouquet Ordering System with Recommendation Feature**.

> Dataset yang dihasilkan meniru pola dasar e-commerce florist seperti produk bouquet, pengguna, dan interaksi pengguna terhadap produk.

## Tujuan

Repository ini dibuat untuk menghasilkan dataset sintetis yang realistis untuk kebutuhan:

- eksperimen sistem rekomendasi
- simulasi perilaku pengguna
- pengembangan dan pengujian model machine learning

Dataset dibuat berdasarkan distribusi probabilitas yang dapat dikonfigurasi sehingga pola data tidak sepenuhnya random.

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
   
   ```
   pip install -r requirements.txt
   ```

2. Jalankan script generator:
   
   ```
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

Dataset yang dihasilkan bersifat **sintetis** dan tidak merepresentasikan data bisnis nyata. Tujuan utama dataset ini adalah untuk simulasi dan pengujian sistem rekomendasi.

## Lisensi

Digunakan untuk keperluan akademik dan penelitian.