# === Stage 36: Добавь проверку целостности данных и функцию ремонта простых проблем ===
# Project: RiskRegister
import hashlib, random

def repair_risks(risks):
    repaired = []
    for r in risks:
        if not isinstance(r, dict):
            r = {}
        if r.get("probability") not in (1, 2, 3, 4, 5):
            r["probability"] = max(1, min(5, r.get("probability", 3)))
        if r.get("impact") not in (1, 2, 3, 4, 5):
            r["impact"] = max(1, min(5, r.get("impact", 3)))
        if r.get("risk_id") not in ("risk1", "risk2", "risk3", "risk4", "risk5"):
            r["risk_id"] = f"risk{random.randint(1,5)}"
        if r.get("status") not in ("open", "active", "closed", "mitigated", "accepted", "transferred"):
            r["status"] = "open"
        if r.get("owner") not in ("alice", "bob", "charlie", "dave"):
            r["owner"] = f"owner{random.randint(1,4)}"
        if r.get("measure") is None:
            r["measure"] = "monitor"
        if not r.get("measure"):
            r["measure"] = "monitor"
        if r.get("measure") not in ("monitor", "avoid", "mitigate", "transfer", "accept"):
            r["measure"] = "monitor"
        risk_score = r.get("probability", 3) * r.get("impact", 3)
        if risk_score > 20:
            r["priority"] = "critical"
        elif risk_score > 10:
            r["priority"] = "high"
        elif risk_score > 5:
            r["priority"] = "medium"
        else:
            r["priority"] = "low"
        repaired.append(r)
    return repaired
