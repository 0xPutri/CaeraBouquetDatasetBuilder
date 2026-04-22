import os
import time
from rich.console import Console
from rich.panel import Panel
from rich.status import Status
from rich.theme import Theme

from generators.products import generate_products
from generators.users import generate_users
from generators.interactions import generate_iterations

custom_theme = Theme({
    "info": "cyan",
    "success": "green",
    "warning": "yellow",
    "error": "red",
    "dim": "grey50"
})

console = Console(theme=custom_theme)

def main():
    """
    Menjalankan alur pembuatan dataset dengan tampilan Rich CLI.

    Proses ini mengoordinasikan pembuatan data produk, pengguna, dan
    interaksi dengan feedback visual yang interaktif.
    """
    os.system('cls' if os.name == 'nt' else 'clear')
    
    console.print(
        Panel.fit(
            "[bold cyan]CAERA BOUQUET[/bold cyan] | [dim]Dataset Builder Generator[/dim]",
            border_style="cyan",
            padding=(1, 4)
        )
    )

    output_dir = "data/generated"
    os.makedirs(output_dir, exist_ok=True)

    # 1. Products
    with Status("[bold]Menyusun katalog produk riil...", console=console, spinner="dots") as status:
        time.sleep(1)
        products_df = generate_products()
        products_path = os.path.join(output_dir, "products.csv")
        products_df.to_csv(products_path, index=False)
        console.print(f"[success]✔[/success] Katalog produk berhasil disiapkan [dim]({products_path})[/dim]")

    # 2. Users
    with Status("[bold]Menciptakan profil pengguna fiktif...", console=console, spinner="dots") as status:
        time.sleep(1)
        users_df = generate_users()
        users_path = os.path.join(output_dir, "users.csv")
        users_df.to_csv(users_path, index=False)
        console.print(f"[success]✔[/success] Profil pengguna berhasil dibuat [dim]({users_path})[/dim]")

    # 3. Interactions
    with Status("[bold]Mensimulasikan aktivitas pelanggan...", console=console, spinner="dots") as status:
        time.sleep(1)
        interactions_df = generate_iterations(products_df, users_df)
        interactions_path = os.path.join(output_dir, "interactions.csv")
        interactions_df.to_csv(interactions_path, index=False)
        console.print(f"[success]✔[/success] Simulasi interaksi selesai [dim]({interactions_path})[/dim]")

    console.print("\n[bold green]✓ Seluruh proses generator berhasil diselesaikan.[/bold green]\n")

if __name__ == "__main__":
    main()