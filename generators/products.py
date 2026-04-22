import pandas as pd
import random

from config.distributions import (
    PRODUCT_THEMES,
    EVENT_TYPES,
    BOUQUET_SIZES,
    REAL_PRODUCTS
)

from utils.sampling import ambil_berdasarkan_bobot


def generate_products():
    """
    Menghasilkan data produk bunga berdasarkan katalog nyata.

    Fungsi ini memetakan daftar produk riil dari Founder ke dalam format
    dataset agar kompatibel dengan proses pemrosesan data lainnya.

    Returns:
        pd.DataFrame: DataFrame yang memuat informasi lengkap produk.
    """
    data = []
    
    for i, product in enumerate(REAL_PRODUCTS):
        product_id = f"B{i+1:03}"
        product_type = product["name"] 
        price = product["price"]
        
        product_theme = ambil_berdasarkan_bobot(PRODUCT_THEMES)
        event_type = ambil_berdasarkan_bobot(EVENT_TYPES)
        
        size = product.get("size", ambil_berdasarkan_bobot(BOUQUET_SIZES))
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
        path_output (str): Lokasi penyimpanan file CSV hasil generate.
    """
    df = generate_products()
    df.to_csv(path_output, index=False)

    print(f"Products dataset berhasil dibuat: {path_output}")