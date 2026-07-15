# === Stage 19: Добавь функцию архивации завершённых или старых записей ===
# Project: RiskRegister
def archive_risks(register, max_age_days=None):
    """Archives risks that are closed or older than max_age_days (if specified)."""
    now = datetime.datetime.now()
    archived = []
    for risk in register:
        if risk['status'] == 'closed':
            archived.append(risk)
            risk['status'] = 'archived'
        elif max_age_days and (now - risk.get('created_at', now)).days > int(max_age_days):
            archived.append(risk)
            risk['status'] = 'archived'
    return archived
