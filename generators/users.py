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
    Menghasilkan data pengguna fiktif untuk simulasi.

    Fungsi ini menciptakan profil pengguna dengan atribut dasar seperti
    usia, jenis kelamin, dan lokasi kota secara acak namun terstruktur.

    Returns:
        pd.DataFrame: DataFrame yang berisi daftar profil pengguna.
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
    Menyimpan dataset pengguna ke dalam format CSV.

    Args:
        path_output (str): Lokasi penyimpanan file CSV hasil generate.
    """
    df = generate_users()
    df.to_csv(path_output, index=False)

    print(f"Users dataset berhasil dibuat: {path_output}")