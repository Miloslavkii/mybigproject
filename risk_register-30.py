# === Stage 30: Добавь поддержку нескольких пользовательских профилей внутри приложения ===
# Project: RiskRegister
class Profile:
    def __init__(self, name="", role="user", permissions=None):
        self.name = name
        self.role = role
        if permissions is None:
            self.permissions = {"read": True, "write": False}
        else:
            self.permissions = dict(permissions)

    def can(self, action):
        return self.permissions.get(action, False)


PROFILES = {
    "admin": Profile("Admin", "admin", {"read": True, "write": True}),
    "editor": Profile("Editor", "user", {"read": True, "write": True}),
    "viewer": Profile("Viewer", "user", {"read": True}),
}

def get_profile(username):
    return PROFILES.get(username) or Profile(username)
