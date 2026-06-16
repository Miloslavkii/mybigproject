# === Stage 2: Добавь модели данных и функции валидации пользовательского ввода ===
# Project: RiskRegister
class Risk:
    def __init__(self, name, probability, impact, owner, status):
        self.name = name.strip() or "Unnamed"
        self.probability = int(probability) if isinstance(probability, (int, float)) else 0
        self.impact = int(impact) if isinstance(impact, (int, float)) else 0
        self.owner = owner.strip() or "Unknown"
        self.status = status.lower().strip() in ["open", "closed"]

    def risk_score(self):
        return self.probability * self.impact

class RiskRegister:
    _risks = []

    @classmethod
    def add_risk(cls, name, probability, impact, owner, status="Open"):
        if not isinstance(probability, (int, float)) or probability < 0 or probability > 1:
            raise ValueError("Probability must be between 0 and 1")
        if not isinstance(impact, (int, float)) or impact < 0:
            raise ValueError("Impact cannot be negative")
        risk = Risk(name, probability, impact, owner, status)
        cls._risks.append(risk)

    @classmethod
    def get_risks(cls):
        return sorted(cls._risks, key=lambda r: r.risk_score(), reverse=True)
