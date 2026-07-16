# === Stage 20: Добавь восстановление записей из архива ===
# Project: RiskRegister
def restore_from_archive(archive_path, risk_db):
    """Восстанавливает записи из JSON-архива в RiskRegister."""
    import json
    if not os.path.exists(archive_path):
        print(f"Файл архива не найден: {archive_path}")
        return 0
    
    with open(archive_path, 'r', encoding='utf-8') as f:
        records = json.load(f)
    
    count = 0
    for record in records:
        try:
            risk_id = record.get('id') or str(count + len(risk_db))
            new_record = {
                'id': risk_id,
                'name': record.get('name', ''),
                'probability': record.get('probability', 0),
                'impact': record.get('impact', 0),
                'risk_level': record.get('risk_level', 'low'),
                'owner': record.get('owner', ''),
                'description': record.get('description', ''),
                'status': 'archived' if record.get('status') == 'archived' else record.get('status', 'new'),
                'measures': record.get('measures', []),
            }
            risk_db.append(new_record)
            count += 1
        except Exception as e:
            print(f"Ошибка восстановления записи: {e}")
    
    print(f"Восстановлено {count} записей из архива.")
    return count
