# === Stage 50: Сделай аккуратную финальную полировку сообщений, названий функций и комментариев ===
# Project: RiskRegister
def polish_report(report):
    """
    Формирует отформатированный текстовый отчёт по реестру рисков.
    Каждый риск отображается с номером, статусом, владельцем,
    вероятностью, влиянием и мерой. Финальный блок подводит
    итоги по статусам и уровню влияния.
    """
    lines = [
        "=" * 60,
        "  РЕЕСТР РИСКОВ — ОТЧЁТ",
        "=" * 60,
    ]
    for idx, risk in enumerate(report, start=1):
        lines.append(
            f"{idx:>2}. [{risk['status'].upper():<10}] "
            f"Владелец: {risk['owner']:<15} "
            f"P={risk['probability']:<3}%  "
            f"I={risk['impact']:<3}  "
            f"Мера: {risk['measure']}"
        )
    lines.append("-" * 60)
    status_counts = {}
    for r in report:
        status_counts[r['status']] = status_counts.get(r['status'], 0) + 1
    lines.append("  Статистика статусов:")
    for s, c in status_counts.items():
        lines.append(f"    {s:<10}: {c} риск(а)")
    severity = {'HIGH': 'КРИТИЧНО', 'MEDIUM': 'СРЕДНЕ', 'LOW': 'НИЗКО'}
    if status_counts.get('CLOSED', 0) == len(report):
        lines.append("  Итог: все риски закрыты.")
    else:
        lines.append(f"  Итог: остаётся {len(report) - status_counts.get('CLOSED', 0)} открытых риска.")
    lines.append("=" * 60)
    return "\n".join(lines)
