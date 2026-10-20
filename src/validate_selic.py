
import json
from pathlib import Path

from validation import validate_records

PROJECT_DIR = Path(__file__).resolve().parent.parent
INPUT_FILE = PROJECT_DIR / "data" / "raw" / "selic.json"


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
        records = validate_records(data)
    except ValueError as error:
        print("Validação falhou:")
        print(error)
        return

    print("Validação concluída sem problemas.")
    print(f"Registros válidos: {len(records)}")


if __name__ == "__main__":
    main()
