# === Stage 16: Добавь расчёт месячной статистики по датам ===
# Project: RiskRegister
import datetime as dt

def monthly_stats(records):
    """Month-over-month stats: count, avg risk score, severity distribution."""
    if not records:
        return {"months": [], "avg_score_by_month": {}, "severity_counts": {}}

    def month_key(d):
        return d.replace(day=1)

    grouped = {}
    for r in records:
        m = month_key(r["date"])
        grouped.setdefault(m, []).append(r)

    months = sorted(grouped.keys())
    avg_scores = {}
    severity_counts = {}
    counts_per_month = []
    for m in months:
        items = grouped[m]
        scores = [r.get("impact", 0) + r.get("probability", 0) for r in items]
        counts_per_month.append(len(items))
        avg_scores[m] = sum(scores)/len(scores) if scores else 0.0

    all_items = []
    for m in months:
        all_items.extend(grouped[m])
    severity_dist = {}
    for item in all_items:
        s = item.get("severity", "unknown")
        severity_dist[s] = severity_dist.get(s, 0) + 1

    return {
        "months": [m.isoformat() if isinstance(m, dt.date) else m for m in months],
        "counts_per_month": counts_per_month,
        "avg_score_by_month": avg_scores,
        "severity_counts": severity_dist,
    }
