# === Stage 53: Добавь импорт отчёта или списка записей из простого текстового формата ===
# Project: RiskRegister
def export_risks(path, risks, fmt="csv"):
    lines = []
    if fmt == "csv":
        header = "ID;Risk;Probability;Impact;Measure;Owner;Status"
        lines.append(header)
        for r in risks:
            lines.append(";".join([str(r["id"]), str(r["risk"]), str(r["probability"]), str(r["impact"]), str(r["measure"]), str(r["owner"]), str(r["status"])]))
    else:
        for r in risks:
            lines.append(f"ID={r['id']} Risk={r['risk']} Probability={r['probability']} Impact={r['impact']} Measure={r['measure']} Owner={r['owner']} Status={r['status']}")
    content = "\n".join(lines)
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)
    return content

def import_risks(path):
    records = []
    with open(path, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            if line.startswith("ID="):
                d = dict(part.split("=", 1) for part in line.split() if "=" in part)
                records.append({"id": int(d["ID"]), "risk": d["Risk"], "probability": int(d["Probability"]), "impact": int(d["Impact"]), "measure": d["Measure"], "owner": d["Owner"], "status": d["Status"]})
            elif ";" in line:
                parts = [p.strip() for p in line.split(";")]
                records.append({"id": int(parts[0]), "risk": parts[1], "probability": int(parts[2]), "impact": int(parts[3]), "measure": parts[4], "owner": parts[5], "status": parts[6]})
    return records
