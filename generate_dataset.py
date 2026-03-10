import os

from generators.products import generate_products
from generators.users import generate_users
from generators.interactions import generate_iterations


def main():
    """
    Fungsi utama untuk menghasilkan dan menyimpan semua dataset sintetis.

    Fungsi ini akan:
    1. Membuat direktori output jika belum ada
    2. Menghasilkan dataset products dan menyimpannya ke CSV
    3. Menghasilkan dataset users dan menyimpannya ke CSV
    4. Menghasilkan dataset interactions dan menyimpannya ke CSV

    Returns:
        None
    """
    print("Mulai generate dataset sintetis florist...\n")

    output_dir = "data/generated"
    os.makedirs(output_dir, exist_ok=True)

    # Generate Products
    products_df = generate_products()
    products_path = os.path.join(output_dir, "products.csv")
    products_df.to_csv(products_path, index=False)
    print(f"Products berhasil dibuat: {products_path}")

    # Generate Users
    users_df = generate_users()
    users_path = os.path.join(output_dir, "users.csv")
    users_df.to_csv(users_path, index=False)
    print(f"Users berhasil dibuat: {users_path}")

    # Generate Interactions
    interactions_df = generate_iterations(products_df, users_df)
    interactions_path = os.path.join(output_dir, "interactions.csv")
    interactions_df.to_csv(interactions_path, index=False)
    print(f"Interactions berhasil dibuat: {interactions_path}")

    print("\nSemua dataset berhasil dibuat.")


if __name__ == "__main__":
    main()