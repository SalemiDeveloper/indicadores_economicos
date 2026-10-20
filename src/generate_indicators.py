
import csv
import json
from pathlib import Path

PROJECT_DIR = Path(__file__).resolve().parent.parent
INPUT_FILE = PROJECT_DIR / "data" / "processed" / "selic.csv"
OUTPUT_FILE = PROJECT_DIR / "data" / "processed" / "indicators.json"


def main():
    try:
        with INPUT_FILE.open("r", newline="", encoding="utf-8") as file:
            records = list(csv.DictReader(file))
    except FileNotFoundError:
        print("Arquivo selic.csv não encontrado. Execute a transformação primeiro.")
        return

    if len(records) < 2:
        raise ValueError("São necessários pelo menos dois registros.")

    records.sort(key=lambda record: record["data"])

    first_record = records[0]
    last_record = records[-1]

    initial_rate = float(first_record["valor"])
    final_rate = float(last_record["valor"])

    indicators = {
        "data_inicial": first_record["data"],
        "data_final": last_record["data"],
        "selic_inicial": initial_rate,
        "selic_final": final_rate,
        "variacao_pontos_percentuais": round(
            final_rate - initial_rate, 4
        ),
        "quantidade_observacoes": len(records),
    }

    OUTPUT_FILE.write_text(
        json.dumps(indicators, ensure_ascii=False, indent=2),
        encoding="utf-8",
    )

    print(json.dumps(indicators, ensure_ascii=False, indent=2))
    print(f"\nIndicadores salvos em: {OUTPUT_FILE}")


if __name__ == "__main__":
    main()
