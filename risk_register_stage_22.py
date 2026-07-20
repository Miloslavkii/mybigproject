# === Stage 22: Добавь проверку просроченных напоминаний ===
# Project: RiskRegister
def check_overdue_reminders(risks, today=None):
    if today is None:
        from datetime import date as _date
        today = _date.today()
    overdue = []
    for risk in risks:
        due_date_str = getattr(risk, 'reminder_due', None)
        if not due_date_str:
            continue
        try:
            due_date = _parse_date(due_date_str)
        except Exception:
            continue
        if due_date < today and risk.get('status') != 'resolved':
            overdue.append(risk)
    return overdue
