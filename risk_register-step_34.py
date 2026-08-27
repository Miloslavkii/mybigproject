# === Stage 34: Добавь простую систему шаблонов для быстрого создания записей ===
# Project: RiskRegister
class RiskTemplate:
    def __init__(self, name, description, probability, impact, owner, status, measure=None):
        self.name = name
        self.description = description
        self.probability = probability
        self.impact = impact
        self.owner = owner
        self.status = status
        self.measure = measure

    def create_risk(self):
        return RiskRecord(
            name=self.name,
            description=self.description,
            probability=self.probability,
            impact=self.impact,
            owner=self.owner,
            status=self.status,
            measure=self.measure,
        )

templates = {
    "high_priority": RiskTemplate(
        name="High Priority Risk",
        description="Critical risk requiring immediate attention",
        probability="High",
        impact="High",
        owner="Risk Manager",
        status="Active",
        measure="Implement mitigation plan immediately",
    ),
    "medium_priority": RiskTemplate(
        name="Medium Priority Risk",
        description="Significant risk to be monitored",
        probability="Medium",
        impact="Medium",
        owner="Project Lead",
        status="Active",
        measure="Regular review and monitoring",
    ),
    "low_priority": RiskTemplate(
        name="Low Priority Risk",
        description="Minor risk for future consideration",
        probability="Low",
        impact="Low",
        owner="Team",
        status="Monitor",
        measure="Document and review periodically",
    ),
}
