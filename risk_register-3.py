# === Stage 3: Реализуй хранение состояния в памяти и функции добавления записей ===
# Project: RiskRegister
class RiskRegister:
    def __init__(self):
        self._risks = []

    def add_risk(self, name, probability, impact, owner, mitigation, status="Open"):
        risk_id = len(self._risks) + 1
        record = {
            "id": risk_id,
            "name": name,
            "probability": float(probability),
            "impact": int(impact),
            "owner": owner,
            "mitigation": mitigation,
            "status": status
        }
        self._risks.append(record)
        return record

    def get_all_risks(self):
        return list(self._risks)
