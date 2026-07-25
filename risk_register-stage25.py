# === Stage 25: Добавь обработку некорректных дат и понятные сообщения об ошибках ===
# Project: RiskRegister
def validate_date(date_str):
    """Проверяет корректность дат в формате YYYY-MM-DD, возвращает True/False."""
    try:
        year, month, day = map(int, date_str.split('-'))
        if not (1 <= year <= 9999 and 1 <= month <= 12 and 1 <= day <= 31):
            return False
        import calendar
        max_day = calendar.monthrange(year, month)[1]
        if day > max_day:
            return False
        return True
    except (ValueError, AttributeError):
        return False

def format_error(message, field=""):
    """Формирует понятное сообщение об ошибке."""
    if field:
        return f"Ошибка в поле '{field}': {message}"
    return message

class RiskRegister:
    def __init__(self):
        self._risks = []

    def add_risk(self, title, description="", probability=None, impact=None, owner=None,
                 mitigation=None, target_date=None, status="Активен", risk_id=None):
        """Добавляет риск в реестр с проверкой дат и обработкой ошибок."""
        if not validate_date(target_date):
            return format_error("Некорректная дата. Используйте формат YYYY-MM-DD.", "target_date")

        if probability is None or impact is None:
            return format_error("Необходимо указать вероятность (probability) и влияние (impact).", "")

        risk = {
            "id": risk_id,
            "title": title,
            "description": description,
            "probability": probability,
            "impact": impact,
            "owner": owner,
            "mitigation": mitigation,
            "target_date": target_date,
            "status": status
        }

        self._risks.append(risk)
        return risk
