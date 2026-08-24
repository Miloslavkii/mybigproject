# === Stage 32: Добавь журнал действий пользователя ===
# Project: RiskRegister
class UserActionLog:
    def __init__(self):
        self.entries = []
    
    def log(self, user, action, risk_id=None, details=""):
        entry = {
            "user": user,
            "action": action,
            "risk_id": risk_id,
            "timestamp": datetime.now().isoformat(),
            "details": details
        }
        self.entries.append(entry)
        return entry
    
    def get_by_user(self, user):
        return [e for e in self.entries if e["user"] == user]
    
    def get_all(self):
        return self.entries
    
    def clear(self):
        self.entries.clear()
