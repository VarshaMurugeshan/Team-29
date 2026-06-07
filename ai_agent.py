
def analyze(changes):
    results = []
    for c in changes:
        if c["type"] == "removed_column":
            impact = "HIGH"
            mitigation = "Update downstream systems or create compatibility view."
        else:
            impact = "LOW"
            mitigation = "Verify new column usage."

        results.append({
            **c,
            "impact": impact,
            "mitigation": mitigation
        })
    return results
