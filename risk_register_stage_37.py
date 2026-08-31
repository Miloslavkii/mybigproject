# === Stage 37: Добавь мини-набор unit-тестов без внешних зависимостей ===
# Project: RiskRegister
import unittest


class TestRisk(unittest.TestCase):
    def test_risk_creation(self):
        risk = Risk("R1", "Задержка поставки", 0.7, 3, "Владимир", "Высокий")
        self.assertEqual(risk.id, "R1")
        self.assertEqual(risk.name, "Задержка поставки")
        self.assertEqual(risk.probability, 0.7)
        self.assertEqual(risk.impact, 3)
        self.assertEqual(risk.owner, "Владимир")
        self.assertEqual(risk.status, "Высокий")

    def test_risk_score(self):
        risk = Risk("R1", "Задержка", 0.8, 4, "Олег", "Высокий")
        self.assertEqual(risk.score, 32)

    def test_risk_add_to_register(self):
        reg = RiskRegister()
        reg.add(Risk("R1", "Задержка", 0.7, 3, "Владимир", "Высокий"))
        reg.add(Risk("R2", "Бюджет", 0.3, 2, "Мария", "Средний"))
        self.assertEqual(len(reg), 2)

    def test_risk_register_filter_by_status(self):
        reg = RiskRegister()
        reg.add(Risk("R1", "Задержка", 0.7, 3, "Владимир", "Высокий"))
        reg.add(Risk("R2", "Бюджет", 0.3, 2, "Мария", "Средний"))
        high_risks = reg.filter_by_status("Высокий")
        self.assertEqual(len(high_risks), 1)
        self.assertEqual(high_risks[0].name, "Задержка")

    def test_risk_register_sort_by_score(self):
        reg = RiskRegister()
        reg.add(Risk("R1", "Задержка", 0.7, 3, "Владимир", "Высокий"))
        reg.add(Risk("R2", "Бюджет", 0.3, 2, "Мария", "Средний"))
        sorted_risks = reg.sort_by_score()
        self.assertEqual(sorted_risks[0].name, "Задержка")
        self.assertEqual(sorted_risks[1].name, "Бюджет")


if __name__ == "__main__":
    unittest.main()
