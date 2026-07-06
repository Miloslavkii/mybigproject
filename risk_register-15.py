# === Stage 15: Добавь расчёт недельной статистики по датам ===
# Project: RiskRegister
def weekly_stats(self):
    """Return dict of week -> {total, avg_risk_score}."""
    if not self.risks:
        return {}
    from datetime import datetime, timedelta
    results = {}
    for r in sorted(self.risks, key=lambda x: x.date):
        week_start = r.date - timedelta(days=r.date.weekday())
        key = week_start.strftime("%Y-%W")
        if key not in results:
            results[key] = {"total": 0, "scores": []}
        results[key]["total"] += 1
        results[key]["scores"].append(r.risk_score)
    return {k: {"total": v["total"], "avg_risk_score": round(sum(v["scores"]) / len(v["scores"]), 2)} for k, v in sorted(results.items())}
