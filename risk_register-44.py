# === Stage 44: Добавь функцию резервного копирования файла данных ===
# Project: RiskRegister
def backup_file_data(filepath, backup_dir="backups"):
    """Создаёт резервную копию файла данных RiskRegister.
    
    Аргументы:
        filepath: путь к текущему файлу данных.
        backup_dir: директория для хранения бэкапов (по умолчанию "backups").
    
    Возвращает:
        Полный путь к созданному файлу бэкапа.
    """
    import shutil
    import os
    from datetime import datetime

    if not os.path.exists(backup_dir):
        os.makedirs(backup_dir)

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    backup_path = os.path.join(backup_dir, f"risk_register_{timestamp}.dat")

    try:
        shutil.copy2(filepath, backup_path)
        print(f"Резервная копия создана: {backup_path}")
        return backup_path
    except Exception as e:
        print(f"Ошибка при создании резервной копии: {e}")
        raise
