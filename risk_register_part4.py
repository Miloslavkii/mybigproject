# === Stage 4: Добавь функцию редактирования существующих записей по идентификатору ===
# Project: RiskRegister
def edit_risk(risk_id: int, updates: dict) -> RiskRecord | None:
    for i, record in enumerate(RISK_REGISTRY):
        if record.id == risk_id:
            if not updates.get('status'):
                updates['status'] = record.status
            if not updates.get('probability') and 'probability' in record.__dict__:
                updates['probability'] = record.probability
            if not updates.get('impact') and 'impact' in record.__dict__:
                updates['impact'] = record.impact
            for key, value in updates.items():
                if hasattr(record, key):
                    setattr(record, key, value)
            return record
    raise ValueError(f"Риск с ID {risk_id} не найден")
