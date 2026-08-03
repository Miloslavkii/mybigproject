# === Stage 31: Добавь переключение активного пользовательского профиля ===
# Project: RiskRegister
class ProfileSwitcher:
    def __init__(self, profiles):
        self.profiles = profiles or {}
        self.active_profile = None

    def add(self, name, **kwargs):
        self.profiles[name] = kwargs
        return self

    def switch(self, profile_name):
        if profile_name not in self.profiles:
            raise ValueError(f"Profile '{profile_name}' does not exist")
        self.active_profile = profile_name
        return self.profiles[profile_name]

    @property
    def active(self):
        return getattr(self, 'active_profile', None) or list(self.profiles.keys())[0] if self.profiles else None

    def get_config(self):
        return {self.active: self.profiles[self.active]} if self.active and self.active in self.profiles else {}
