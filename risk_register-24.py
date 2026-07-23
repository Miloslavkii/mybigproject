# === Stage 24: Добавь компактный вывод одной записи с деталями ===
# Project: RiskRegister
def print_risk(record):
    """Компактный вывод одной записи реестра рисков."""
    if not record:
        return
    r = record
    status_symbol = {0: "✅", 1: "🔴", 2: "🟡"}.get(r.status, "?")
    print(f"\n{'='*60}")
    print(f"Риск #{r.id} | Статус: {status_symbol} {STATUS_LABELS[r.status]}")
    print(f"{'─'*60}")
    print(f"  Название : {r.name}")
    print(f"  Категория: {r.category or '-'}")
    print(f"  Описание : {r.description[:80] if r.description else '-'}")
    print(f"  {'─'*40}")
    print(f"  Вероятность : {PROB_LABELS[r.probability]} ({r.probability_value})")
    print(f"  Влияние    : {IMPACT_LABELS[r.impact]} ({r.impact_value})")
    risk_score = r.probability * r.impact
    print(f"  Риск-оценка: {risk_score:.1f}")
    if r.mitigation_measures:
        print(f"  Меры       : {'; '.join(r.mitigation_measures)}")
    owner = r.owner or "Не назначен"
    print(f"  Владелец   : {owner}")
    print(f"{'='*60}\n")

# Пример использования:
if __name__ == "__main__":
    risk_1 = Risk(
        name="Высокая нагрузка на сервер",
        category="Технический",
        description="Сервер может не выдержать пиковую нагрузку в час пик.",
        probability=0.7, impact=3, status=2, owner="Иванов И.И."
    )
    risk_1.mitigation_measures = ["Масштабирование", "Кэширование"]
    print_risk(risk_1)
