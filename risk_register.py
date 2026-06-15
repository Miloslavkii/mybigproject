# === Stage 1: Создай базовую структуру файла приложения, точку входа и демонстрационные данные ===
# Project: RiskRegister
import json, random
from dataclasses import asdict
from typing import List, Dict, Any

class Risk:
    def __init__(self, id: str, name: str, probability: float, impact: float, owner: str, status: str = "Active"):
        self.id = id
        self.name = name
        self.probability = probability
        self.impact = impact
        self.owner = owner
        self.status = status

    def score(self) -> int:
        return round((self.probability * 10 + self.impact * 5))

def generate_demo_data() -> List[Risk]:
    risks = [
        Risk("R-001", "Сбой сервера БД", random.uniform(0.2, 0.8), random.uniform(3, 9), "IT_Ops"),
        Risk("R-002", "Утечка данных клиентов", random.uniform(0.1, 0.5), random.uniform(7, 10), "Security_Team"),
        Risk("R-003", "Задержка поставки ПО", random.uniform(0.4, 0.9), random.uniform(2, 6), "Procurement"),
    ]
    for r in risks:
        if random.random() > 0.5:
            r.status = "Mitigated"
    return risks

if __name__ == "__main__":
    demo_risks = generate_demo_data()
    print(json.dumps([asdict(r) for r in demo_risks], indent=2))
