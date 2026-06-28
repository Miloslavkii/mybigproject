# === Stage 10: Добавь экспорт текущего состояния в JSON-строку ===
# Project: RiskRegister
def export_to_json(risks, measures, owners):
    import json
    data = {
        "risks": risks,
        "measures": measures,
        "owners": owners
    }
    return json.dumps(data, ensure_ascii=False, indent=2)
