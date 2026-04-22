import os
from rich.console import Console
from rich.panel import Panel
from rich.status import Status
from utils.data_merger import simpan_training_dataset

console = Console()

def main():
    """
    Menggabungkan seluruh dataset menjadi data pelatihan final.

    Fungsi ini menyatukan file produk, pengguna, dan interaksi yang 
    telah dibuat sebelumnya menjadi satu berkas CSV siap pakai.
    """
    os.system('cls' if os.name == 'nt' else 'clear')

    console.print(
        Panel.fit(
            "[bold cyan]CAERA BOUQUET[/bold cyan] | [dim]Data Merger System[/dim]",
            border_style="cyan",
            padding=(1, 4)
        )
    )

    with Status("[bold]Menggabungkan data dan menyiapkan CSV final...", console=console, spinner="bouncingBar") as status:
        try:
            simpan_training_dataset(
                "data/generated/training_dataset.csv",
                "data/generated/products.csv",
                "data/generated/users.csv",
                "data/generated/interactions.csv"
            )
            console.print("\n[bold green]✓ Dataset pelatihan telah siap digunakan.[/bold green]\n")
        except Exception as e:
            console.print(f"\n[bold red]✗ Terjadi kesalahan saat penggabungan:[/bold red] {e}\n")

if __name__ == "__main__":
    main()