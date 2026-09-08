# === Stage 43: Добавь пагинацию длинных списков ===
# Project: RiskRegister
def paginate_items(items, page_size=10):
    """Делит список на страницы по page_size элементов."""
    pages = []
    for start in range(0, len(items), page_size):
        pages.append(items[start:start + page_size])
    return pages
