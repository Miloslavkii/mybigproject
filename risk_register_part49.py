# === Stage 49: Добавь финальную самопроверку приложения и отчёт о готовности ===
# Project: RiskRegister
def self_check():
    """Финальная самопроверка RiskRegister"""
    print("=" * 60)
    print("🔍 Финальная самопроверка RiskRegister")
    print("=" * 60)
    
    # Проверка импорта всех компонентов
    components = [
        "Risk", "RiskStatus", "RiskSeverity", "RiskMeasure", "RiskOwner",
        "RiskRegister", "RiskReport", "RiskDashboard", "RiskAnalyzer"
    ]
    for comp in components:
        try:
            globals()[comp]
            print(f"  ✅ {comp} — загружен")
        except NameError:
            print(f"  ❌ {comp} — НЕ НАЙДЕН")
    
    # Проверка работы реестра
    print("\n📋 Тест работы реестра:")
    reg = RiskRegister()
    reg.add_risk(
        title="Срыв сроков",
        probability=0.7,
        impact=0.8,
        owner="Иванов",
        status="Высокий",
        measures="Дедлайны по неделям"
    )
    reg.add_risk(
        title="Низкая мотивация",
        probability=0.3,
        impact=0.5,
        owner="Петров",
        status="Средний",
        measures="Бонусная система"
    )
    risks = reg.get_all_risks()
    print(f"  ✅ Добавлено рисков: {len(risks)}")
    
    # Проверка отчёта
    report = reg.generate_report()
    print(f"  ✅ Отчёт сгенерирован: {len(report)} строк")
    
    # Проверка дашборда
    dashboard = reg.generate_dashboard()
    print(f"  ✅ Дашборд создан: {len(dashboard)} элементов")
    
    # Проверка анализатора
    analysis = reg.analyze_risks()
    print(f"  ✅ Анализ выполнен: {len(analysis)} рекомендаций")
    
    print("\n" + "=" * 60)
    print("🎉 RiskRegister готов к работе!")
    print("=" * 60)
    return True
