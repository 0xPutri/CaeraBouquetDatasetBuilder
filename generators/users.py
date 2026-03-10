import pandas as pd
import random

from config.distributions import (
    JUMLAH_USERS,
    AGE_RANGE,
    GENDER_DISTRIBUTION,
    CITIES
)

from utils.sampling import (
    ambil_berdasarkan_bobot,
    ambil_angka_range
)


def generate_users():
    """
    Menghasilkan DataFrame pengguna sintetis.

    Fungsi ini membuat data pengguna dengan atribut demografis
    seperti ID, usia, jenis kelamin, dan kota tempat tinggal.

    Returns:
        pd.DataFrame: DataFrame pengguna dengan kolom:
            - user_id (str): ID unik pengguna (format: U0001, U0002, dst).
            - age (int): Usia pengguna dalam rentang yang ditentukan.
            - gender (str): Jenis kelamin pengguna (female/male).
            - city (str): Kota tempat tinggal pengguna.
    """
    data = []
    for i in range(JUMLAH_USERS):
        user_id = f"U{i+1:04}"
        age = ambil_angka_range(AGE_RANGE[0], AGE_RANGE[1])
        gender = ambil_berdasarkan_bobot(GENDER_DISTRIBUTION)
        city = random.choice(CITIES)

        data.append({
            "user_id": user_id,
            "age": age,
            "gender": gender,
            "city": city
        })

    df = pd.DataFrame(data)

    return df


def simpan_users(path_output):
    """
    Menghasilkan dan menyimpan dataset pengguna ke file CSV.

    Args:
        path_output (str): Path file output untuk menyimpan dataset CSV.

    Returns:
        None
    """
    df = generate_users()
    df.to_csv(path_output, index=False)

    print(f"Users dataset berhasil dibuat: {path_output}")