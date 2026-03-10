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
    Menghasilkan DataFrame interaksi pengguna dengan produk.

    Fungsi ini membuat data interaksi sintetis yang mencakup view, click,
    dan purchase antara pengguna dan produk dalam periode waktu tertentu.

    Args:
        products_df (pd.DataFrame): DataFrame produk yang berisi kolom 'product_id'.
        users_df (pd.DataFrame): DataFrame pengguna yang berisi kolom 'user_id'.

    Returns:
        pd.DataFrame: DataFrame interaksi dengan kolom:
            - interaction_id (str): ID unik untuk setiap interaksi.
            - user_id (str): ID pengguna yang melakukan interaksi.
            - product_id (str): ID produk yang diinteraksikan.
            - interaction_type (str): Jenis interaksi (view, click, purchase).
            - timestamp (datetime): Waktu interaksi terjadi.
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
    Menghasilkan dan menyimpan dataset interaksi ke file CSV.

    Args:
        product_df (pd.DataFrame): DataFrame produk sebagai referensi.
        users_df (pd.DataFrame): DataFrame pengguna sebagai referensi.
        path_output (str): Path file output untuk menyimpan dataset CSV.

    Returns:
        None
    """
    df = generate_iterations(product_df, users_df)
    df.to_csv(path_output, index=False)

    print(f"Interactions dataset berhasil dibuat: {path_output}")