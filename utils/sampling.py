import random


def ambil_berdasarkan_bobot(data):
    """
    Mengambil nilai secara acak berdasarkan distribusi bobot.

    Args:
        data (list[tuple]): Daftar pasangan (nilai, bobot).

    Returns:
        Any: Nilai yang terpilih sesuai probabilitas.
    """
    nilai = [item[0] for item in data]
    bobot = [item[1] for item in data]

    return random.choices(nilai, weights=bobot, k=1)[0]


def ambil_angka_range(min_val, max_val):
    """
    Mengambil angka acak dalam rentang nilai tertentu.

    Args:
        min_val (int): Batas minimum angka.
        max_val (int): Batas maksimum angka.

    Returns:
        int: Angka acak yang terpilih dalam rentang.
    """
    return random.randint(min_val, max_val)
