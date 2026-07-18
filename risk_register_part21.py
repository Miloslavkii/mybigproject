# === Stage 21: Добавь простую систему напоминаний с датой выполнения ===
# Project: RiskRegister
class Reminder:
    def __init__(self, title, due_date):
        self.title = title
        self.due_date = due_date

    def is_overdue(self, today=None):
        if today is None:
            from datetime import date
            today = date.today()
        return self.due_date < today

    @staticmethod
    def check_reminders(reminders, today=None):
        overdue = [r for r in reminders if r.is_overdue(today)]
        return overdue

def add_reminder_to_risk(risk, title="Риск-напоминание", due_date=None):
    from datetime import date
    if due_date is None:
        due_date = risk.next_review or date.today() + timedelta(days=30)
    reminder = Reminder(title, due_date)
    risk.reminders.append(reminder)
    return reminder

def print_overdue_reminders(reminders):
    overdue = check_reminders(reminders)
    if not overdue:
        print("Нет просроченных напоминаний.")
    else:
        print(f"Просрочено {len(overdue)} напоминание(ий):")
        for r in overdue:
            print(f"  - {r.title} (срок: {r.due_date})")
