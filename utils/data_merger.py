import pandas as pd


def gabungkan_dataset(products_path, users_path, interactions_path):
    """
    Menggabungkan dataset products, users, dan interactions menjadi satu DataFrame.

    Fungsi ini menyatukan data produk, pengguna, dan interaksi 
    berdasarkan ID masing-masing untuk membentuk dataset yang utuh.

    Args:
        products_path (str): Path file CSV produk.
        users_path (str): Path file CSV pengguna.
        interactions_path (str): Path file CSV interaksi.

    Returns:
        pd.DataFrame: DataFrame hasil penggabungan dataset.
    """
    products = pd.read_csv(products_path)
    users = pd.read_csv(users_path)
    interactions = pd.read_csv(interactions_path)

    df = interactions.merge(users, on="user_id", how="left")
    df = df.merge(products, on="product_id", how="left")

    return df


def simpan_training_dataset(
    output_path,
    products_path,
    users_path,
    interactions_path
):
    """
    Menyimpan hasil penggabungan dataset untuk keperluan pelatihan.

    Args:
        output_path (str): Lokasi penyimpanan file CSV hasil akhir.
        products_path (str): Path file CSV produk.
        users_path (str): Path file CSV pengguna.
        interactions_path (str): Path file CSV interaksi.
    """
    df = gabungkan_dataset(products_path, users_path, interactions_path)
    df.to_csv(output_path, index=False)