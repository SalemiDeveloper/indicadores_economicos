
from datetime import date, datetime
import math


def validate_records(data, today=None):
    if not isinstance(data, list):
        raise ValueError("A entrada precisa ser uma lista.")

    if not data:
        raise ValueError("Não existem registros para validar.")

    if today is None:
        today = date.today()

    errors = []
    seen_dates = set()
    validated_records = []

    for index, record in enumerate(data, start=1):
        if not isinstance(record, dict):
            errors.append(f"Registro {index}: formato inválido.")
            continue

        if "data" not in record or "valor" not in record:
            errors.append(f"Registro {index}: campo obrigatório ausente.")
            continue

        try:
            observation_date = datetime.strptime(
                record["data"], "%d/%m/%Y"
            ).date()
        except (TypeError, ValueError):
            errors.append(f"Registro {index}: data inválida.")
            continue

        try:
            value = float(record["valor"])
        except (TypeError, ValueError):
            errors.append(f"Registro {index}: valor não numérico.")
            continue

        if observation_date > today:
            errors.append(f"Registro {index}: data futura.")

        if observation_date in seen_dates:
            errors.append(f"Registro {index}: data duplicada.")

        if not math.isfinite(value):
            errors.append(f"Registro {index}: valor não finito.")
        elif value < 0:
            errors.append(f"Registro {index}: valor negativo.")

        seen_dates.add(observation_date)

        validated_records.append({
            "data": observation_date.isoformat(),
            "valor": value,
        })

    if errors:
        raise ValueError("\n".join(errors))

    return sorted(validated_records, key=lambda record: record["data"])
