# === Stage 48: Проведи рефакторинг: разнеси крупные функции, сохрани совместимость публичных команд ===
# Project: RiskRegister
def _severity_label(p, impact):
    score = p * impact
    if score >= 0.64:
        return "Critical"
    if score >= 0.32:
        return "High"
    if score >= 0.10:
        return "Medium"
    return "Low"

def _status_label(status):
    return {
        "Open": "Open",
        "In Progress": "Open",
        "Closed": "Closed",
        "Mitigated": "Closed",
        "Accepted": "Open",
        "Transferred": "Open",
        "Escalated": "Open",
    }.get(status, status)

def _format_risk(r):
    return (
        f"[{r['id']}] {r['name']}"
        f" | P={r['probability']:.0%} I={r['impact']:.0%}"
        f" | Severity={_severity_label(r['probability'], r['impact'])}"
        f" | Status={_status_label(r['status'])}"
        f" | Owner={r['owner']}"
        f" | Measures={r['measures']}"
    )
