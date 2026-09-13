# === Stage 46: Добавь миграцию версии структуры данных ===
# Project: RiskRegister
def migrate_v2():
    """Migration v2: add status column to risks table."""
    global risks
    if 'status' not in risks[0]:
        risks.append(['status', 'active'])
        print("Migration v2 completed: status column added.")

migrate_v2()
