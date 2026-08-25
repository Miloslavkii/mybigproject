# === Stage 33: Добавь откат последнего действия там, где это разумно ===
# Project: RiskRegister
import sys
import os

try:
    while True:
        try:
            with open(sys.argv[1]) as f:
                content = f.read()
        except FileNotFoundError:
            print("Файл не найден")
            sys.exit(1)

        with open(sys.argv[1], 'w') as f:
            f.write(content)
            print(f"Файл {sys.argv[1]} успешно создан")
except KeyboardInterrupt:
    print("Прервано пользователем")
    sys.exit(1)
