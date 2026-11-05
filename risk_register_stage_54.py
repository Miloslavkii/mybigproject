# === Stage 54: Добавь режим избранных записей и быстрый доступ к ним ===
# Project: RiskRegister
class Favorites:
    def __init__(self):
        self.favorites = []

    def is_favorited(self, risk_id):
        return risk_id in self.favorites

    def toggle_favorite(self, risk_id):
        if risk_id in self.favorites:
            self.favorites.remove(risk_id)
        else:
            self.favorites.append(risk_id)

    def get_favorites(self):
        return self.favorites

    def clear_favorites(self):
        self.favorites = []

    def save_favorites(self, path):
        with open(path, 'w') as f:
            json.dump(self.favorites, f)

    def load_favorites(self, path):
        if os.path.exists(path):
            with open(path, 'r') as f:
                self.favorites = json.load(f)

def show_favorite_risks(favorites, risk_list):
    if not favorites:
        print("Избранных рисков нет. Добавьте риски в избранное для быстрого доступа.")
        return
    fav_risks = []
    for risk_id in favorites:
        for risk in risk_list:
            if risk['id'] == risk_id:
                fav_risks.append(risk)
    print("=== Избранные риски ===")
    for risk in fav_risks:
        print(f"  [{risk['id']}] {risk['name']} (П: {risk['probability']}, В: {risk['impact']}, Статус: {risk['status']})")
    print(f"Всего избранных рисков: {len(fav_risks)}")

def quick_access_to_favorites(favorites, risk_list):
    if not favorites:
        print("Нет избранных рисков для быстрого доступа.")
        return
    fav_risks = []
    for risk_id in favorites:
        for risk in risk_list:
            if risk['id'] == risk_id:
                fav_risks.append(risk)
    print("=== Быстрый доступ к избранным рискам ===")
    print("1. Просмотреть список избранных")
    print("2. Редактировать выбранный риск")
    print("3. Удалить выбранный риск")
    print("4. Убрать из избранного")
    print("5. Вернуться назад")
    choice = input("Введите номер действия: ")
    if choice == '1':
        show_favorite_risks(favorites, risk_list)
    elif choice == '2':
        if fav_risks:
            edit_risk(fav_risks[0], risk_list)
        else:
            print("Риск не найден.")
    elif choice == '3':
        if fav_risks:
            del_risk(fav_risks[0]['id'])
            favorites.toggle_favorite(fav_risks[0]['id'])
            favorites.save_favorites('favorites.json')
            print("Риск удалён и убран из избранного.")
        else:
            print("Риск не найден.")
    elif choice == '4':
        if fav_risks:
            favorites.toggle_favorite(fav_risks[0]['id'])
            favorites.save_favorites('favorites.json')
            print("Риск убран из избранного.")
        else:
            print("Риск не найден.")
    elif choice == '5':
        print("Возврат к основному меню.")
    else:
        print("Неверный выбор.")
