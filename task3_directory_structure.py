import sys
from pathlib import Path
from colorama import init, Fore, Style

# Ініціалізація colorama
init()

def print_directory_structure(path: Path, indent: str = ""):
    try:
        for item in sorted(path.iterdir()):
            if item.is_dir():
                print(f"{indent}{Fore.BLUE}{item.name}{Style.RESET_ALL}")
                print_directory_structure(item, indent + "    ")
            elif item.is_file():
                print(f"{indent}{Fore.GREEN}{item.name}{Style.RESET_ALL}")
            else:
                print(f"{indent}{Fore.YELLOW}{item.name} (невідомий тип){Style.RESET_ALL}")
    except PermissionError:
        print(f"{indent}{Fore.RED}Permission denied: {path}{Style.RESET_ALL}")

def main():
    if len(sys.argv) < 2:
        print(f"{Fore.RED}Помилка: Не вказано шлях до директорії.{Style.RESET_ALL}")
        print("Використання: python task3.py /шлях/до/директорії")
        sys.exit(1)

    input_path = Path(sys.argv[1])

    if not input_path.exists():
        print(f"{Fore.RED}Помилка: Шлях не існує.{Style.RESET_ALL}")
        sys.exit(1)

    if not input_path.is_dir():
        print(f"{Fore.RED}Помилка: Це не директорія.{Style.RESET_ALL}")
        sys.exit(1)

    print(f"📁 Структура директорії: {input_path}\n")
    print_directory_structure(input_path)

if __name__ == "__main__":
    main()
