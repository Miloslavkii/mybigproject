# === Stage 27: Добавь функции сброса демо-данных и очистки состояния ===
# Project: RiskRegister
def reset_demo_data():
    """Заполняет реестр тестовыми данными."""
    for risk in demo_risks:
        RiskRegister.add(risk)

def clear_state():
    """Полностью очищает все риски и сбрасывает демо-данные."""
    while len(RiskRegister.risks) > 0:
        RiskRegister.remove_next()
