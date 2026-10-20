
import json
from datetime import datetime
from pathlib import Path
from urllib.request import urlopen


URL = (
    "https://api.bcb.gov.br/dados/serie/bcdata.sgs.432/dados"
    "?formato=json&dataInicial=01/09/2026&dataFinal=19/10/2026"
)


PROJECT_DIR = Path(__file__).resolve().parent.parent
RAW_DIR = PROJECT_DIR / "data" / "raw"
OUTPUT_FILE = RAW_DIR / "selic.json"


def main():
    RAW_DIR.mkdir(parents=True, exist_ok=True)

    try:
        with urlopen(URL, timeout=30) as response:
            data = json.loads(response.read().decode("utf-8"))
    except Exception as error:
        raise RuntimeError(f"Não foi possível obter os dados do Banco Central: {error}") from error

    if not isinstance(data, list):
        raise ValueError("A resposta da API não é uma lista.")

    for item in data:
        datetime.strptime(item["data"], "%d/%m/%Y")
        float(item["valor"])

    OUTPUT_FILE.write_text(
        json.dumps(data, ensure_ascii=False, indent=2),
        encoding="utf-8",
    )

    print(f"Registros recebidos: {len(data)}")
    print(f"Arquivo salvo em: {OUTPUT_FILE}")


if __name__ == "__main__":
    main()
