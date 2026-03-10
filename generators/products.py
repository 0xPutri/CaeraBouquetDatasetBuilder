import pandas as pd
import random

from config.distributions import (
    JUMLAH_PRODUCTS,
    PRODUCT_TYPES,
    PRODUCT_THEMES,
    EVENT_TYPES,
    BOUQUET_SIZES,
    PRICE_RANGES
)

from utils.sampling import (
    ambil_berdasarkan_bobot,
    ambil_angka_range
)


def generate_products():
    """
    Menghasilkan DataFrame produk bunga sintetis.

    Fungsi ini membuat data produk dengan atribut seperti tipe produk,
    tema produk, jenis acara, ukuran buket, harga, dan skor popularitas.

    Returns:
        pd.DataFrame: DataFrame produk dengan kolom:
            - product_id (str): ID unik produk (format: B001, B002, dst).
            - product_type (str): Jenis produk (fresh_flower, artificial_flower, dll).
            - product_theme (str): Tema produk (graduation, romantic, birthday, dll).
            - event_type (str): Jenis acara (graduation, birthday, anniversary, dll).
            - size (str): Ukuran buket (small, medium, large, premium).
            - price (int): Harga produk dalam rupiah.
            - popularity (float): Skor popularitas (0.1 - 1.0).
    """
    data = []
    for i in range(JUMLAH_PRODUCTS):
        product_id = f"B{i+1:03}"
        product_type = ambil_berdasarkan_bobot(PRODUCT_TYPES)
        product_theme = ambil_berdasarkan_bobot(PRODUCT_THEMES)
        event_type = ambil_berdasarkan_bobot(EVENT_TYPES)
        size = ambil_berdasarkan_bobot(BOUQUET_SIZES)
        price_min, price_max = PRICE_RANGES[size]
        price = ambil_angka_range(price_min, price_max)
        popularity = round(random.uniform(0.1, 1.0), 2)

        data.append({
            "product_id": product_id,
            "product_type": product_type,
            "product_theme": product_theme,
            "event_type": event_type,
            "size": size,
            "price": price,
            "popularity": popularity
        })

    df = pd.DataFrame(data)

    return df


def simpan_products(path_output):
    """
    Menghasilkan dan menyimpan dataset produk ke file CSV.

    Args:
        path_output (str): Path file output untuk menyimpan dataset CSV.

    Returns:
        None
    """
    df = generate_products()
    df.to_csv(path_output, index=False)

    print(f"Products dataset berhasil dibuat: {path_output}")