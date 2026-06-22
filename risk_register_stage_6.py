# === Stage 6: Добавь фильтрацию записей по статусу, категории или тегам ===
# Project: RiskRegister
class RiskFilter:
    def __init__(self, risks):
        self.risks = risks

    def filter_by_status(self, status):
        return [r for r in self.risks if r['status'] == status]

    def filter_by_category(self, category):
        return [r for r in self.risks if r.get('category') and r['category'].lower() == category.lower()]

    def filter_by_tags(self, tags):
        if not tags:
            return list(self.risks)
        query_tags = set(t.lower() for t in tags)
        return [r for r in self.risks if any(tag in (r.get('tags') or []) for tag in query_tags)]

    def filter_combined(self, status=None, category=None, tags=None):
        result = list(self.risks)
        if status:
            result = self.filter_by_status(status)
        if category:
            result = self.filter_by_category(category)
        if tags:
            result = self.filter_by_tags(tags)
        return result

    def get_filtered_risks(self, **kwargs):
        return self.filter_combined(**{k: v for k, v in kwargs.items() if v is not None})
