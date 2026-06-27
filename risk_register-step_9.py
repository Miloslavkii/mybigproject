# === Stage 9: Добавь импорт начальных данных из JSON-строки ===
# Project: RiskRegister
import json, sys
try:
    initial_data = """{
        "risks": [
            {"id": 101, "name": "Задержка поставки", "probability": 0.7, "impact": 8, "owner": "Иванов И.", "status": "Активен", "mitigation": "Диверсификация поставщиков"},
            {"id": 102, "name": "Бюджетное переполнение", "probability": 0.4, "impact": 9, "owner": "Петрова А.", "status": "Мониторинг", "mitigation": "Резервный фонд"},
            {"id": 103, "name": "Технический сбой", "probability": 0.2, "impact": 5, "owner": "Сидоров К.", "status": "Закрыт", "mitigation": "Плановое ТО"}
        ],
        "statuses": ["Активен", "Мониторинг", "В работе", "Закрыт"],
        "owners": {"Иванов И.": "+79001234567", "Петрова А.": "+79007654321"}
    }"""
    with open("data.json", "w", encoding="utf-8") as f:
        json.dump(json.loads(initial_data), f, ensure_ascii=False, indent=2)
except Exception as e:
    print(f"Ошибка импорта данных: {e}", file=sys.stderr)
    sys.exit(1)
