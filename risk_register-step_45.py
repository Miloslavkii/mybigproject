# === Stage 45: Добавь восстановление из резервной копии ===
# Project: RiskRegister
import pickle, os

def load_backup(file_path):
    """Загрузка резервной копии реестра из файла pickle."""
    if not os.path.exists(file_path):
        print(f"Резервная копия не найдена: {file_path}")
        return None
    try:
        with open(file_path, 'rb') as f:
            data = pickle.load(f)
        return data
    except Exception as e:
        print(f"Ошибка восстановления из {file_path}: {e}")
        return None

def save_backup(risk_register, file_path):
    """Сохранение текущего реестра в резервную копию."""
    try:
        with open(file_path, 'wb') as f:
            pickle.dump(risk_register, f)
        print(f"Резервная копия сохранена: {file_path}")
    except Exception as e:
        print(f"Ошибка сохранения резервной копии: {e}")
