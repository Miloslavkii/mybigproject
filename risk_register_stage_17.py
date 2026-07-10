# === Stage 17: Добавь группировку записей по категориям ===
# Project: RiskRegister
def group_risks_by_category(risk_list):
    """Group risk records by their category field."""
    categories = {}
    for r in risk_list:
        cat = getattr(r, 'category', getattr(r, '_category', None)) or 'Uncategorized'
        if cat not in categories:
            categories[cat] = []
        categories[cat].append(r)
    return {k: sorted(v, key=lambda x: x.get('priority', 0), reverse=True) for k, v in categories.items()}
