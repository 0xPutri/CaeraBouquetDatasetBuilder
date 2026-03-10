import pandas as pd


def gabungkan_dataset(products_path, users_path, interactions_path):
    """
    Menggabungkan dataset products, users, dan interactions menjadi satu DataFrame.

    Fungsi ini membaca ketiga dataset CSV dan melakukan merge berdasarkan
    user_id dan product_id untuk menghasilkan dataset yang lengkap.

    Args:
        products_path (str): Path ke file CSV dataset products.
        users_path (str): Path ke file CSV dataset users.
        interactions_path (str): Path ke file CSV dataset interactions.

    Returns:
        pd.DataFrame: DataFrame hasil merge yang berisi semua informasi
            dari interactions, users, dan products.
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
    Menggabungkan dan menyimpan dataset training ke file CSV.

    Fungsi ini menggabungkan dataset products, users, dan interactions,
    kemudian menyimpan hasilnya sebagai file CSV untuk keperluan training.

    Args:
        products_path (str): Path ke file CSV dataset products.
        users_path (str): Path ke file CSV dataset users.
        interactions_path (str): Path ke file CSV dataset interactions.
        output_path (str): Path file output untuk menyimpan dataset training.

    Returns:
        None
    """
    df = gabungkan_dataset(products_path, users_path, interactions_path)
    df.to_csv(output_path, index=False)

    print(f"Training dataset berhasil dibuat: {output_path}")