#: Jumlah interaksi yang akan dihasilkan
JUMLAH_INTERACTIONS = 8000

#: Jumlah produk yang akan dihasilkan
JUMLAH_PRODUCTS = 120

#: Jumlah pengguna yang akan dihasilkan
JUMLAH_USERS = 400


#: Distribusi tipe produk dengan bobot probabilitas
#: Format: (nama_produk, bobot)
PRODUCT_TYPES = [
    ("fresh_flower", 0.25),
    ("artificial_flower", 0.35),
    ("money_bouquet", 0.15),
    ("satin_bouquet", 0.15),
    ("mixed_bouquet", 0.10),
]


#: Distribusi tema produk dengan bobot probabilitas
#: Format: (nama_tema, bobot)
PRODUCT_THEMES = [
    ("graduation", 0.35),
    ("romantic", 0.10),
    ("birthday", 0.25),
    ("anniversary", 0.05),
    ("wedding", 0.15),
    ("condolence", 0.10),
]


#: Distribusi jenis acara dengan bobot probabilitas
#: Format: (nama_acara, bobot)
EVENT_TYPES = [
    ("graduation", 0.35),
    ("birthday", 0.25),
    ("anniversary", 0.15),
    ("wedding", 0.15),
    ("condolence", 0.10),
]


#: Distribusi ukuran buket dengan bobot probabilitas
#: Format: (ukuran, bobot)
BOUQUET_SIZES = [
    ("small", 0.30),
    ("medium", 0.40),
    ("large", 0.20),
    ("premium", 0.10),
]


#: Rentang harga berdasarkan ukuran buket dalam rupiah
#: Format: {ukuran: (harga_min, harga_max)}
PRICE_RANGES = {
    "small": (100000, 150000),
    "medium": (150000, 300000),
    "large": (300000, 600000),
    "premium": (600000, 1000000),
}


#: Distribusi gender pengguna dengan bobot probabilitas
#: Format: (gender, bobot)
GENDER_DISTRIBUTION = [
    ("female", 0.55),
    ("male", 0.45),
]


#: Rentang usia pengguna (min, max)
AGE_RANGE = (18, 40)


#: Distribusi jenis interaksi dengan bobot probabilitas
#: Format: (jenis_interaksi, bobot)
INTERACTION_TYPES = [
    ("view", 0.7),
    ("click", 0.2),
    ("purchase", 0.1),
]


#: Daftar kota yang tersedia untuk data pengguna
CITIES = [
    "Banjarnegara",
    "Bandung",
    "Jakarta",
    "Surabaya",
    "Yogyakarta",
    "Semarang",
    "Malang",
    "Wonosobo",
    "Purbalingga",
    "Banyumas",
    "Cilacap"
]