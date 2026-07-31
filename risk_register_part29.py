# === Stage 29: Добавь конфигурацию приложения через словарь настроек ===
# Project: RiskRegister
def create_app_config():
    config = {
        "app_name": "RiskRegister",
        "version": 2,
        "risk_statuses": ["pending", "active", "mitigated", "closed"],
        "default_risk_priority": "medium",
        "log_level": "INFO",
        "max_risks_per_project": 50,
    }
    return config
