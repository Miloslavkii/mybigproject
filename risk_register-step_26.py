# === Stage 26: Добавь набор демо-команд для быстрого ручного тестирования ===
# Project: RiskRegister
def demo_risks():
    risks = [
        {"name": "Задержка поставки", "prob": 0.7, "impact": 3, "owner": "IT-менеджер", "status": "active"},
        {"name": "Бюджетное сокращение", "prob": 0.5, "impact": 4, "owner": "Финансовый директор", "status": "active"},
        {"name": "Смена приоритетов", "prob": 0.3, "impact": 2, "owner": "Руководитель проекта", "status": "monitored"},
    ]
    for r in risks:
        score = round(r["prob"] * r["impact"], 1)
        print(f"{r['name']:<25} | {score:>6.1f} | Статус: {r['status']}")

demo_risks()
