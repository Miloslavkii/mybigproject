# === Stage 14: Добавь генерацию краткой сводки по текущим данным ===
# Project: RiskRegister
def generate_summary():
    if not risks: return "Данных нет."
    total = len(risks)
    high_risk = [r for r in risks if (r.probability * r.impact) > 10]
    by_owner = {}
    statuses = set()
    measures_count = 0
    for r in risks:
        owner = r.owner or "Не назначен"
        by_owner[owner] = by_owner.get(owner, 0) + 1
        statuses.add(r.status)
        if r.mitigation_measures: measures_count += len(r.mitigation_measures.split(";"))
    summary_lines = [f"Всего рисков: {total}", f"Высокий приоритет (P*I>10): {len(high_risk)}", f"Уникальные статусы: {', '.join(statuses)}"]
    if by_owner: summary_lines.append(f"Распределение по владельцам:\n  " + "\n  ".join([f"{o}: {c}" for o, c in sorted(by_owner.items())]))
    if measures_count > 0: summary_lines.append(f"Всего мер реагирования: {measures_count}")
    print("\n".join(summary_lines))
