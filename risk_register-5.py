# === Stage 5: Добавь удаление записей и аккуратную обработку отсутствующих идентификаторов ===
# Project: RiskRegister
def delete_risk(risk_id: int) -> bool:
    if risk_id not in risks_db:
        print(f"Риск #{risk_id} не найден.")
        return False
    
    del risks_db[risk_id]
    print(f"Риск #{risk_id} успешно удален.")
    return True

def get_missing_risks() -> list[int]:
    missing = []
    for i in range(1, max(risks_db.keys()) + 2):
        if i not in risks_db:
            missing.append(i)
    return missing
