# === Stage 40: Добавь CLI-параметры через argparse для основных операций ===
# Project: RiskRegister
import argparse

def main():
    parser = argparse.ArgumentParser(description="RiskRegister CLI")
    sub = parser.add_subparsers(dest="command", required=True)

    add_p = sub.add_parser("add", help="Добавить риск")
    add_p.add_argument("id", help="ID риска")
    add_p.add_argument("name", help="Название")
    add_p.add_argument("probability", type=int, help="Вероятность (1-5)")
    add_p.add_argument("impact", type=int, help="Влияние (1-5)")
    add_p.add_argument("owner", help="Владелец")
    add_p.add_argument("status", help="Статус")
    add_p.add_argument("measures", help="Меры, через запятую")

    show_p = sub.add_parser("show", help="Показать риск")
    show_p.add_argument("id", help="ID риска")

    update_p = sub.add_parser("update", help="Обновить риск")
    update_p.add_argument("id", help="ID риска")
    update_p.add_argument("field", help="Поле для обновления")
    update_p.add_argument("value", help="Новое значение")

    args = parser.parse_args()
    if args.command == "add":
        add_risk(args.id, args.name, args.probability, args.impact,
                 args.owner, args.status, args.measures)
    elif args.command == "show":
        show_risk(args.id)
    elif args.command == "update":
        update_risk(args.id, args.field, args.value)
