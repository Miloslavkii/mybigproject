# === Stage 35: Добавь рекомендации следующего действия на основе текущего состояния ===
# Project: RiskRegister
def next_action_advice(risk):
    """Recommend next step based on risk state."""
    if risk.status == "open" and risk.assigned:
        return "Follow up with owner for update."
    elif risk.status == "open" and not risk.assigned:
        return "Assign a responsible owner."
    elif risk.status == "open" and risk.severity == "high":
        return "Prioritize mitigation plan immediately."
    elif risk.status == "open" and risk.severity == "medium":
        return "Schedule review in next iteration."
    elif risk.status == "open" and risk.severity == "low":
        return "Monitor passively, no immediate action."
    elif risk.status == "in_progress":
        return "Track progress and prepare for status update."
    elif risk.status == "resolved":
        return "Document resolution details and close record."
    elif risk.status == "closed":
        return "Archive for compliance and lessons learned."
    elif risk.status == "escalated":
        return "Report to management and initiate escalation procedure."
    else:
        return "No specific action needed at this time."
