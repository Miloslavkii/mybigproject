# === Stage 11: Добавь сохранение данных в локальный JSON-файл ===
# Project: RiskRegister
def save_to_json(data, filename="risk_register.json"):
    import json
    try:
        with open(filename, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
        print(f"Данные успешно сохранены в {filename}")
    except Exception as e:
        print(f"Ошибка при сохранении файла: {e}")

def load_from_json(filename="risk_register.json"):
    import json
    try:
        with open(filename, "r", encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        print(f"Файл {filename} не найден.")
        return []

if __name__ == "__main__":
    # Пример использования для проверки сохранения и загрузки
    sample_data = [
        {"id": 1, "risk_name": "Срыв сроков", "probability": 0.7, "impact": 8, "owner": "Иванов И.", "status": "Активен"},
        {"id": 2, "risk_name": "Бюджетное превышение", "probability": 0.4, "impact": 6, "owner": "Петров П.", "status": "В работе"}
    ]
    
    # Сохранение тестовых данных
    save_to_json(sample_data)
    
    # Загрузка и вывод сохраненных данных
    loaded_data = load_from_json()
    print(f"Загружено рисков: {len(loaded_data)}")
