# === Stage 12: Добавь загрузку данных из локального JSON-файла с обработкой ошибок ===
# Project: RiskRegister
def load_from_json(file_path):
    try:
        import json
        with open(file_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
        if isinstance(data, list):
            risks = [Risk(r['name'], r.get('probability', 3), r.get('impact', 3), 
                          r.get('owner'), r.get('status', 'Open')) for r in data]
        else:
            raise ValueError("Ожидается массив рисков в JSON")
        print(f"Загружено {len(risks)} рисков из '{file_path}'")
        return risks
    except FileNotFoundError:
        print(f"Файл не найден: {file_path}")
        return []
    except json.JSONDecodeError as e:
        print(f"Ошибка парсинга JSON в '{file_path}': {e}")
        return []
    except KeyError as e:
        print(f"Отсутствует поле в данных риска: {e}")
        return []
