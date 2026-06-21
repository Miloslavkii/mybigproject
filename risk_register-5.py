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

# === Stage 5: Добавь удаление записей и аккуратную обработку отсутствующих идентификаторов ===
# Project: RiskRegister
def remove_risk(risk_id: int) -> bool:
    try:
        index = next((i for i, r in enumerate(RISK_REGISTRY) if r['id'] == risk_id), None)
        if index is not None:
            del RISK_REGISTRY[index]
            print(f"Риск #{risk_id} успешно удален.")
            return True
        else:
            print(f"Ошибка: Риск с идентификатором {risk_id} не найден в реестре.")
            return False
    except Exception as e:
        print(f"Произошла непредвиденная ошибка при удалении риска #{risk_id}: {e}")
        return False

def get_risk_by_id(risk_id: int) -> dict | None:
    try:
        for risk in RISK_REGISTRY:
            if risk['id'] == risk_id:
                return risk.copy()
        return None
    except Exception as e:
        print(f"Ошибка при поиске риска #{risk_id}: {e}")
        return None

def get_all_risks() -> list[dict]:
    try:
        return [r.copy() for r in RISK_REGISTRY]
    except Exception as e:
        print(f"Ошибка при получении списка рисков: {e}")
        return []
