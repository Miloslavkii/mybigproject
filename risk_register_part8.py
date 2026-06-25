# === Stage 8: Реализуй текстовый интерфейс команд с меню действий ===
# Project: RiskRegister
def main_menu():
    while True:
        print("\n=== Risk Register CLI ===")
        print("1. Добавить риск")
        print("2. Показать список рисков")
        print("3. Изменить статус риска")
        print("4. Выход")
        choice = input("Выберите действие (1-4): ")
        if choice == "1":
            name = input("Название: ")
            prob = int(input("Вероятность (1-5): "))
            impact = int(input("Влияние (1-5): "))
            owner = input("Владелец: ")
            risk_register.add_risk(name, prob, impact, owner)
        elif choice == "2":
            if not risk_register.risks:
                print("Список пуст.")
            else:
                for r in risk_register.risks:
                    print(f"{r.name} | P:{r.prob} I:{r.impact} O:{r.owner} S:{r.status}")
        elif choice == "3":
            idx = int(input("Индекс риска для изменения (0-based): "))
            if 0 <= idx < len(risk_register.risks):
                new_status = input("Новый статус: ")
                risk_register.set_status(idx, new_status)
        elif choice == "4":
            break
