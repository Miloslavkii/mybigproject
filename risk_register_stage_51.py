# === Stage 51: Добавь журнал изменений данных с отметками времени ===
# Project: RiskRegister
import json
from datetime import datetime

class ChangeLog:
    def __init__(self):
        self._entries = []

    def record(self, entity, field, old_value, new_value, actor):
        self._entries.append({
            "entity": entity,
            "field": field,
            "old_value": old_value,
            "new_value": new_value,
            "actor": actor,
            "timestamp": datetime.now().isoformat()
        })
        return self._entries[-1]

    def to_json(self):
        return json.dumps(self._entries, indent=2, ensure_ascii=False)

    def load(self, data):
        self._entries = json.loads(data)
