# === Stage 42: Добавь цветной вывод через ANSI-коды с возможностью отключения ===
# Project: RiskRegister
class Colorizer:
    """ANSI color codes with auto-detection and disable toggle."""

    _enabled = True

    @classmethod
    def detect(cls):
        if os.name != 'posix' or sys.stdout.isatty():
            cls._enabled = True
        else:
            cls._enabled = False

    @classmethod
    def reset(cls):
        return '\033[0m'

    @classmethod
    def red(cls):
        return '\033[31m' if cls._enabled else ''

    @classmethod
    def green(cls):
        return '\033[32m' if cls._enabled else ''

    @classmethod
    def yellow(cls):
        return '\033[33m' if cls._enabled else ''

    @classmethod
    def blue(cls):
        return '\033[34m' if cls._enabled else ''

    @classmethod
    def bold(cls):
        return '\033[1m' if cls._enabled else ''

    @classmethod
    def risk_high(cls):
        return f'{cls.red()}{cls.bold()}'

    @classmethod
    def risk_medium(cls):
        return f'{cls.yellow()}{cls.bold()}'

    @classmethod
    def risk_low(cls):
        return f'{cls.green()}{cls.bold()}'

    @classmethod
    def risk_none(cls):
        return ''
