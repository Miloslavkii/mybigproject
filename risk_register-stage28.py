# === Stage 28: Добавь подсчёт ключевых метрик проекта ===
# Project: RiskRegister
def calculate_metrics(risks):
    """Count key project metrics from the risks list."""
    total = len(risks)
    closed = sum(1 for r in risks if r['status'] == 'closed')
    open_ = sum(1 for r in risks if r['status'] in ('open', 'in_progress'))
    average_risk_score = (
        sum(r.get('probability', 0) * r.get('impact', 0) for r in risks) / total
        if total else 0.0
    )
    return {
        'total': total,
        'open': open_,
        'closed': closed,
        'average_risk_score': round(average_risk_score, 2),
    }

if __name__ == '__main__':
    risks = [
        {'probability': 0.4, 'impact': 3, 'status': 'open', 'owner': 'A'},
        {'probability': 0.7, 'impact': 5, 'status': 'in_progress', 'owner': 'B'},
        {'probability': 0.1, 'impact': 2, 'status': 'closed', 'owner': 'C'},
    ]
    print(calculate_metrics(risks))
