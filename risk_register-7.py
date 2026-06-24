# === Stage 7: Добавь сортировку записей по дате, приоритету и названию ===
# Project: RiskRegister
def sort_risks(risk_list, key='priority'):
    priority_map = {'high': 3, 'medium': 2, 'low': 1}
    date_key = lambda x: x.get('date', '') if isinstance(x.get('date'), str) else ''
    name_key = lambda x: x.get('name', '').lower()
    
    def sort_key(risk):
        p_val = priority_map.get(priority_map.get(key, 'priority').lower(), 0) if key == 'priority' else (3 - risk.get('impact') or 1) + (risk.get('probability') or 1)
        d_val = date_key(risk)
        n_val = name_key(risk)
        
        if key == 'date':
            return (-int(d_val.replace('-', '')) if d_val else -9999, p_val, n_val)
        elif key == 'priority':
            return (p_val, -int(d_val.replace('-', '')) if d_val else 0, n_val)
        else: # name
            return (-int(d_val.replace('-', '')) if d_val else 0, p_val, n_val)
    
    risk_list.sort(key=sort_key)
    return risk_list
