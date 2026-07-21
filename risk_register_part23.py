# === Stage 23: Добавь форматированный вывод таблицей в консоль ===
# Project: RiskRegister
def print_risk_table(risks):
    if not risks:
        print("Список рисков пуст.")
        return
    headers = ["ID", "Описание", "Вероятность", "Влияние", "Мера", "Статус"]
    widths = [len(h) for h in headers]
    for r in risks:
        row = [str(getattr(r, h)) if hasattr(r, h) else getattr(r, 'name', '')[:widths[i]] for i, h in enumerate(headers)]
        for j, w in enumerate(widths):
            widths[j] = max(widths[j], len(row[j]))
    print(f"{'ID':<{widths[0]}}  {'Описание':<{widths[1]}}  {'Вероятность':<{widths[2]}}  {'Влияние':<{widths[3]}}  {'Мера':<{widths[4]}}  {'Статус':<{widths[5]}}")
    print("-" * sum(widths))
    for r in risks:
        row = [str(getattr(r, h)) if hasattr(r, h) else getattr(r, 'name', '')[:widths[i]] for i, h in enumerate(headers)]
        print(f"{row[0]:<{widths[0]}}  {row[1]:<{widths[1]}}  {row[2]:<{widths[2]}}  {row[3]:<{widths[3]}}  {row[4]:<{widths[4]}}  {row[5]:<{widths[5]}}")

def main():
    risks = [
        Risk(id=1, name="Задержка поставки", probability=0.7, impact=3, measure="Резервный поставщик", owner="Иванов И.", status="Active"),
        Risk(id=2, name="Сбой оборудования", probability=0.4, impact=5, measure="Плановое ТО", owner="Петров П.", status="Mitigated"),
    ]
    print_risk_table(risks)

if __name__ == "__main__":
    main()
