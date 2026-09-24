# === Stage 52: Добавь экспорт краткого отчёта в текстовом формате ===
# Project: RiskRegister
def export_report(risks, owners, mitigations):
    """Export a short risk report as a text string."""
    lines = ["Risk Register Report", "=" * 40, ""]
    for r in risks:
        lines.append(f"Risk: {r['name']} | Severity: {r['probability'] * r['impact']} | Owner: {r['owner']} | Mitigation: {r['mitigation']}")
    lines.append("")
    lines.append("Summary")
    lines.append("=" * 40)
    high = [r for r in risks if r['probability'] * r['impact'] >= 15]
    medium = [r for r in risks if 5 <= r['probability'] * r['impact'] < 15]
    low = [r for r in risks if r['probability'] * r['impact'] < 5]
    lines.append(f"High Risk: {len(high)} | Medium Risk: {len(medium)} | Low Risk: {len(low)}")
    return "\n".join(lines)
