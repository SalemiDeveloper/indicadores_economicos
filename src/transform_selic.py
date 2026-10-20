
import csv
import json
from pathlib import Path

from validation import validate_records

PROJECT_DIR = Path(__file__).resolve().parent.parent
INPUT_FILE = PROJECT_DIR / "data" / "raw" / "selic.json"
OUTPUT_FILE = PROJECT_DIR / "data" / "processed" / "selic.csv"


def main():
    try:
        data = json.loads(INPUT_FILE.read_text(encoding="utf-8"))
    except FileNotFoundError:
        print("Arquivo selic.json não encontrado. Execute a extração primeiro.")
        return
    except json.JSONDecodeError:
        print("O arquivo selic.json contém JSON inválido.")
        return

    try:
        processed_records = validate_records(data)
    except ValueError as error:
        print("Não foi possível transformar os dados:")
        print(error)
        return

    OUTPUT_FILE.parent.mkdir(parents=True, exist_ok=True)

    with OUTPUT_FILE.open("w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=["data", "valor"])
        writer.writeheader()
        writer.writerows(processed_records)

    print(f"Registros processados: {len(processed_records)}")
    print(f"Arquivo gerado: {OUTPUT_FILE}")


if __name__ == "__main__":
    main()
