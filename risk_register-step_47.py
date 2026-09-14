# === Stage 47: Добавь финальную функцию demo(), которая показывает основной пользовательский сценарий ===
# Project: RiskRegister
def demo():
    """Показать основной сценарий работы с реестром рисков."""
    print("=== RiskRegister Demo ===\n")

    # Создаём несколько рисков
    risks = [
        Risk(prob=0.6, impact=8, owner="Иван", status="Active"),
        Risk(prob=0.2, impact=3, owner="Мария", status="Mitigated"),
        Risk(prob=0.9, impact=10, owner="Петр", status="Active"),
        Risk(prob=0.1, impact=2, owner="Анна", status="Closed"),
        Risk(prob=0.7, impact=7, owner="Сергей", status="Active"),
    ]

    register = RiskRegister()
    register.add_all(risks)

    # Показываем все риски
    print("Все риски:")
    for r in register.list_risks():
        print(f"  [{r.status}] {r.id}: P={r.prob:.0%}, I={r.impact}/10 — {r.owner}")

    print("\n--- Оценка рисков (R = P × I) ---")
    for r in register.list_risks():
        score = r.prob * r.impact
        print(f"  {r.id}: R = {score:.1f}")

    print("\n--- Показатели ---")
    print(f"  Всего: {register.total_risks()}")
    print(f"  Active: {register.count_by_status('Active')}")
    print(f"  Средняя оценка: {register.avg_risk_score():.1f}")

    print("\n--- Топ-3 по риску ---")
    top = register.top_risks(3)
    for r in top:
        print(f"  {r.id}: {r.owner} — R={r.prob * r.impact:.1f}")

    print("\n--- Меры ---")
    for r in register.list_risks():
        if r.has_measures():
            print(f"  {r.id}: {r.owner} → {r.get_measures_summary()}")

    print("\n--- Показатели портфеля ---")
    metrics = register.portfolio_metrics()
    print(f"  Средний P: {metrics['avg_prob']:.0%}")
    print(f"  Средний I: {metrics['avg_impact']:.1f}/10")
    print(f"  Средний R: {metrics['avg_risk_score']:.1f}")

    print("\nДемо завершён.")
