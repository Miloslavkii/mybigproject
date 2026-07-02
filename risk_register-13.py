# === Stage 13: Добавь поиск по нескольким полям без учёта регистра ===
# Project: RiskRegister
def search_risks(query: str, fields: list[str] = None) -> list[dict]:
    if not query or not fields:
        return []
    query_lower = query.lower().strip()
    results = []
    for risk in risks_data:
        match_count = 0
        for field_name in fields:
            value = risk.get(field_name)
            if isinstance(value, str):
                if query_lower in value.lower():
                    match_count += 1
        if match_count > 0:
            results.append(risk)
    return results
