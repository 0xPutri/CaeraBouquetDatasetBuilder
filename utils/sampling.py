import random


def ambil_berdasarkan_bobot(data):
    """
    Mengambil satu nilai dari daftar tuple (nilai, bobot) berdasarkan distribusi bobot.

    Args:
        data (list[tuple]): Daftar tuple yang berisi (nilai, bobot).
            Contoh: [("rose", 0.4), ("tulip", 0.2), ("lily", 0.2)]

    Returns:
        Any: Nilai yang dipilih sesuai dengan distribusi bobot yang diberikan.

    Contoh:
        >>> ambil_berdasarkan_bobot([("rose", 0.4), ("tulip", 0.6)])
        'tulip'  # kemungkinan lebih besar terpilih
    """
    nilai = [item[0] for item in data]
    bobot = [item[1] for item in data]

    return random.choices(nilai, weights=bobot, k=1)[0]


def ambil_angka_range(min_val, max_val):
    """
    Mengambil angka acak dalam rentang tertentu (inklusif).

    Args:
        max_val (int): Nilai maksimum dari rentang (inklusif).
        min_val (int): Nilai minimum dari rentang (inklusif).

    Returns:
        int: Angka acak yang dipilih dari rentang [min_val, max_val].

    Contoh:
        >>> ambil_angka_range(1, 10)
        7  # contoh output
    """
    return random.randint(min_val, max_val)