import json
import os

#: Path metadata produk
PRODUCTS_METADATA_PATH = "data/raw/products_metadata.json"

def load_real_products():
    """
    Memuat daftar produk dari file eksternal.

    Fungsi ini mengambil data produk riil dalam format JSON. Jika file 
    tidak ditemukan, data contoh akan digunakan sebagai cadangan.

    Returns:
        list: Daftar produk riil atau data contoh.
    """
    if os.path.exists(PRODUCTS_METADATA_PATH):
        with open(PRODUCTS_METADATA_PATH, "r") as f:
            return json.load(f)
    return [
        {"name": "Mock Flower A", "price": 50000, "size": "small"},
        {"name": "Mock Flower B", "price": 150000, "size": "medium"}
    ]

#: Daftar produk riil
REAL_PRODUCTS = load_real_products()

#: Konfigurasi dasar
JUMLAH_INTERACTIONS = 8000
JUMLAH_USERS = 400
JUMLAH_PRODUCTS = len(REAL_PRODUCTS)

#: Distribusi tema produk
PRODUCT_THEMES = [
    ("graduation", 0.35),
    ("romantic", 0.10),
    ("birthday", 0.25),
    ("anniversary", 0.05),
    ("wedding", 0.15),
    ("condolence", 0.10),
]

#: Distribusi jenis acara
EVENT_TYPES = [
    ("graduation", 0.35),
    ("birthday", 0.25),
    ("anniversary", 0.15),
    ("wedding", 0.15),
    ("condolence", 0.10),
]

#: Distribusi ukuran buket
BOUQUET_SIZES = [
    ("small", 0.30),
    ("medium", 0.40),
    ("large", 0.20),
    ("premium", 0.10),
]

#: Rentang harga buket
PRICE_RANGES = {
    "small": (100000, 150000),
    "medium": (150000, 300000),
    "large": (300000, 600000),
    "premium": (600000, 1000000),
}

#: Distribusi gender pengguna
GENDER_DISTRIBUTION = [
    ("female", 0.55),
    ("male", 0.45),
]

#: Rentang usia pengguna
AGE_RANGE = (18, 40)

#: Distribusi jenis interaksi
INTERACTION_TYPES = [
    ("view", 0.7),
    ("click", 0.2),
    ("purchase", 0.1),
]

#: Daftar kota tersedia
CITIES = [
    "Banjarnegara", "Bandung", "Jakarta", "Surabaya", "Yogyakarta",
    "Semarang", "Malang", "Wonosobo", "Purbalingga", "Banyumas", "Cilacap"
]