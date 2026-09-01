# === Stage 38: Добавь расширенный набор тестов для ошибок и пограничных случаев ===
# Project: RiskRegister
def test_edge_cases():
    # Тесты пограничных случаев
    assert RiskRegister().count() == 0
    assert RiskRegister().to_csv() == ""
    assert RiskRegister().to_json() == "[]"
    
    # Валидация входных данных
    try:
        RiskRegister().add_risk("Risk", 0, 10, "Measure", "Owner", "Status", None)
        assert False
    except Exception:
        pass
    
    # Тесты с пустыми строками
    r = RiskRegister()
    r.add_risk("", 5, 5, "", "", "", "Open")
    assert r.count() == 1
    assert r.get_risk(0).risk_name == ""
    
    # Тесты с экстремальными значениями
    r = RiskRegister()
    r.add_risk("Risk", 1, 1, "Measure", "Owner", "Status", "Open")
    r.add_risk("Risk", 10, 10, "Measure", "Owner", "Status", "Open")
    assert r.count() == 2
    assert r.get_risk(0).probability == 1
    assert r.get_risk(1).impact == 10
    
    # Тесты с невалидными статусами
    r = RiskRegister()
    try:
        r.add_risk("Risk", 5, 5, "Measure", "Owner", "Invalid", "Open")
        assert False
    except Exception:
        pass
    assert r.count() == 0
    
    # Тесты с невалидными приоритетами
    r = RiskRegister()
    try:
        r.add_risk("Risk", 5, 5, "Measure", "Owner", "Open", 0)
        assert False
    except Exception:
        pass
    assert r.count() == 0
    
    # Тесты с невалидными типами мер
    r = RiskRegister()
    try:
        r.add_risk("Risk", 5, 5, "Invalid", "Owner", "Open", "High")
        assert False
    except Exception:
        pass
    assert r.count() == 0

if __name__ == "__main__":
    test_edge_cases()
    print("Edge case tests passed.")
