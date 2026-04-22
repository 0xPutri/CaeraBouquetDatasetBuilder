import pandas as pd
import random
from datetime import datetime, timedelta

from config.distributions import (
    JUMLAH_INTERACTIONS,
    INTERACTION_TYPES
)

from utils.sampling import ambil_berdasarkan_bobot


def generate_iterations(products_df, users_df):
    """
    Menghasilkan data interaksi antara pengguna dan produk.

    Fungsi ini mensimulasikan aktivitas seperti melihat, mengklik, 
    atau membeli produk dalam rentang waktu satu tahun.

    Args:
        products_df (pd.DataFrame): Referensi data produk.
        users_df (pd.DataFrame): Referensi data pengguna.

    Returns:
        pd.DataFrame: DataFrame yang memuat riwayat interaksi.
    """
    data = []

    product_ids = products_df["product_id"].tolist()
    user_ids = users_df["user_id"].tolist()
    start_date = datetime(2024, 1, 1)

    for i in range(JUMLAH_INTERACTIONS):
        interaction_id = f"I{i+1:06}"
        user_id = random.choice(user_ids)
        product_id = random.choice(product_ids)
        interaction_type = ambil_berdasarkan_bobot(INTERACTION_TYPES)
        random_days = random.randint(0, 365)
        timestamp = start_date + timedelta(days=random_days)

        data.append({
            "interaction_id": interaction_id,
            "user_id": user_id,
            "product_id": product_id,
            "interaction_type": interaction_type,
            "timestamp": timestamp
        })

    df = pd.DataFrame(data)

    return df


def simpan_interactions(product_df, users_df, path_output):
    """
    Menyimpan dataset interaksi ke dalam format CSV.

    Args:
        product_df (pd.DataFrame): Data produk sebagai referensi.
        users_df (pd.DataFrame): Data pengguna sebagai referensi.
        path_output (str): Lokasi penyimpanan file CSV.
    """
    df = generate_iterations(product_df, users_df)
    df.to_csv(path_output, index=False)

    print(f"Interactions dataset berhasil dibuat: {path_output}")