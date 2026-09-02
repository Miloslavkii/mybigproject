# === Stage 39: Добавь документационную строку с описанием сценариев использования ===
# Project: RiskRegister
def demo_scenarios() -> None:
    """
    Сценарии использования RiskRegister:

    1. Регистрация нового риска с оценкой вероятности и влияния.
    2. Назначение ответственного владельца риска.
    3. Определение мер реагирования (избегание, снижение, передача, принятие).
    4. Обновление статуса риска при изменении ситуации.
    5. Агрегация рисков по категориям и приоритетам.
    6. Экспорт реестра в отчёт для менеджмента.
    """
    risks = [
        {
            "id": "R001",
            "description": "Задержка поставки компонентов",
            "probability": "High",
            "impact": "High",
            "owner": "Procurement Lead",
            "mitigation": "Дублирование поставщиков",
            "status": "Active",
            "category": "Supply Chain",
        },
        {
            "id": "R002",
            "description": "Утечка персональных данных",
            "probability": "Low",
            "impact": "Critical",
            "owner": "Security Manager",
            "mitigation": "Шифрование и аудит",
            "status": "Active",
            "category": "Security",
        },
        {
            "id": "R003",
            "description": "Смена ключевых нормативных актов",
            "probability": "Medium",
            "impact": "Medium",
            "owner": "Legal Counsel",
            "mitigation": "Мониторинг законодательства",
            "status": "Pending",
            "category": "Compliance",
        },
    ]
    for r in risks:
        print(f"{r['id']}: {r['description']} — {r['probability']}×{r['impact']} [{r['status']}]")
